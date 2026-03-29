"""Decision analysis helpers for the CEO skill.

Provide small, dependency-free financial and prioritization utilities that can be
used from Python code execution during decision analysis.
"""

from __future__ import annotations

import argparse
import json
import math
import random
import sys
from pathlib import Path
from typing import Iterable, Sequence


DEFAULT_SIMULATIONS = 10_000


class ValidationError(ValueError):
    """Raised when inputs are structurally invalid for analysis."""


def _ensure_non_empty(items: Sequence, label: str) -> None:
    if not items:
        raise ValidationError(f"{label} must not be empty")


def _quantile(sorted_values: Sequence[float], q: float) -> float:
    """Return an interpolated quantile for q in [0, 1]."""
    if not sorted_values:
        raise ValidationError("Cannot compute quantile of empty data")
    if q <= 0:
        return float(sorted_values[0])
    if q >= 1:
        return float(sorted_values[-1])

    position = (len(sorted_values) - 1) * q
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return float(sorted_values[lower])

    weight = position - lower
    return float(sorted_values[lower] * (1 - weight) + sorted_values[upper] * weight)


def monte_carlo_simulation(
    scenarios: Sequence[dict],
    num_simulations: int = DEFAULT_SIMULATIONS,
    *,
    seed: int | None = None,
) -> dict:
    """Run a Monte Carlo simulation on decision outcomes.

    Args:
        scenarios: Iterable of dicts with keys:
            - name: str
            - probability: float in (0, 1]
            - outcome_range: [min_value, max_value]
        num_simulations: Number of simulation runs.
        seed: Optional random seed for deterministic runs.

    Returns:
        Summary statistics including mean, median, percentiles, and loss odds.
    """
    _ensure_non_empty(scenarios, "scenarios")
    if num_simulations <= 0:
        raise ValidationError("num_simulations must be > 0")

    rng = random.Random(seed)
    total_probability = 0.0
    normalized_scenarios = []

    for scenario in scenarios:
        probability = float(scenario["probability"])
        outcome_range = scenario["outcome_range"]
        if len(outcome_range) != 2:
            raise ValidationError("outcome_range must contain exactly two values")
        low, high = float(outcome_range[0]), float(outcome_range[1])
        if probability <= 0:
            raise ValidationError("scenario probability must be > 0")
        if low > high:
            raise ValidationError("outcome_range min must be <= max")
        total_probability += probability
        normalized_scenarios.append(
            {
                "name": scenario["name"],
                "probability": probability,
                "outcome_range": (low, high),
            }
        )

    if not math.isclose(total_probability, 1.0, rel_tol=1e-9, abs_tol=1e-9):
        raise ValidationError(
            f"scenario probabilities must sum to 1.0, got {total_probability:.6f}"
        )

    cumulative = []
    running = 0.0
    for scenario in normalized_scenarios:
        running += scenario["probability"]
        cumulative.append((running, scenario))

    results: list[float] = []
    for _ in range(num_simulations):
        pick = rng.random()
        chosen = cumulative[-1][1]
        for threshold, candidate in cumulative:
            if pick <= threshold:
                chosen = candidate
                break
        low, high = chosen["outcome_range"]
        results.append(rng.uniform(low, high))

    results.sort()
    n = len(results)

    return {
        "num_simulations": n,
        "mean": round(sum(results) / n, 4),
        "median": round(_quantile(results, 0.5), 4),
        "p5": round(_quantile(results, 0.05), 4),
        "p25": round(_quantile(results, 0.25), 4),
        "p75": round(_quantile(results, 0.75), 4),
        "p95": round(_quantile(results, 0.95), 4),
        "min": round(results[0], 4),
        "max": round(results[-1], 4),
        "probability_of_loss": round(sum(1 for value in results if value < 0) / n, 4),
    }


def decision_matrix(criteria: Sequence[dict], options: Sequence[dict]) -> list[dict]:
    """Return a weighted decision matrix ranking."""
    _ensure_non_empty(criteria, "criteria")
    _ensure_non_empty(options, "options")

    total_weight = sum(float(criterion["weight"]) for criterion in criteria)
    if not math.isclose(total_weight, 1.0, rel_tol=1e-9, abs_tol=1e-9):
        raise ValidationError(f"criteria weights must sum to 1.0, got {total_weight:.6f}")

    results = []
    for option in options:
        total_score = 0.0
        breakdown = {}
        for criterion in criteria:
            criterion_name = criterion["name"]
            score = float(option["scores"].get(criterion_name, 5))
            weighted = score * float(criterion["weight"])
            breakdown[criterion_name] = {"raw": score, "weighted": round(weighted, 4)}
            total_score += weighted
        results.append(
            {
                "option": option["name"],
                "total_score": round(total_score, 4),
                "breakdown": breakdown,
            }
        )

    return sorted(results, key=lambda item: item["total_score"], reverse=True)


def ice_scoring(initiatives: Sequence[dict]) -> list[dict]:
    """Return ICE (Impact, Confidence, Ease) scores in descending order."""
    _ensure_non_empty(initiatives, "initiatives")

    results = []
    for item in initiatives:
        impact = float(item["impact"])
        confidence = float(item["confidence"])
        ease = float(item["ease"])
        ice = impact * confidence * ease
        results.append(
            {
                "name": item["name"],
                "impact": impact,
                "confidence": confidence,
                "ease": ease,
                "ice_score": round(ice, 4),
            }
        )

    return sorted(results, key=lambda item: item["ice_score"], reverse=True)


def expected_value(options: Sequence[dict]) -> list[dict]:
    """Calculate expected value and downside risk for each option."""
    _ensure_non_empty(options, "options")

    results = []
    for option in options:
        outcomes = option["outcomes"]
        _ensure_non_empty(outcomes, f"outcomes for {option['name']}")
        probability_sum = sum(float(outcome["probability"]) for outcome in outcomes)
        if not math.isclose(probability_sum, 1.0, rel_tol=1e-9, abs_tol=1e-9):
            raise ValidationError(
                f"outcome probabilities for {option['name']} must sum to 1.0, got {probability_sum:.6f}"
            )

        ev = sum(float(o["probability"]) * float(o["value"]) for o in outcomes)
        values = [float(outcome["value"]) for outcome in outcomes]
        downside = sum(
            float(o["probability"]) * float(o["value"]) for o in outcomes if float(o["value"]) < 0
        )

        results.append(
            {
                "option": option["name"],
                "expected_value": round(ev, 4),
                "best_case": max(values),
                "worst_case": min(values),
                "downside_risk": round(downside, 4),
                "outcomes": outcomes,
            }
        )

    return sorted(results, key=lambda item: item["expected_value"], reverse=True)


def npv(cash_flows: Iterable[float], discount_rate: float) -> float:
    """Calculate Net Present Value."""
    cash_flows = list(cash_flows)
    _ensure_non_empty(cash_flows, "cash_flows")
    if discount_rate <= -1:
        raise ValidationError("discount_rate must be greater than -1")
    return round(
        sum(float(cash_flow) / (1 + discount_rate) ** period for period, cash_flow in enumerate(cash_flows)),
        4,
    )


def irr(cash_flows: Iterable[float], precision: float = 0.0001, max_iterations: int = 1000) -> float:
    """Calculate Internal Rate of Return using bisection.

    Raises ValidationError when the cash flows do not cross zero and therefore do
    not contain a valid IRR in the search interval.
    """
    cash_flows = [float(cash_flow) for cash_flow in cash_flows]
    _ensure_non_empty(cash_flows, "cash_flows")
    if precision <= 0:
        raise ValidationError("precision must be > 0")
    if not any(value < 0 for value in cash_flows) or not any(value > 0 for value in cash_flows):
        raise ValidationError("cash_flows must include at least one negative and one positive value")

    def _npv(rate: float) -> float:
        return sum(cash_flow / (1 + rate) ** period for period, cash_flow in enumerate(cash_flows))

    low, high = -0.9999, 10.0
    low_npv = _npv(low)
    high_npv = _npv(high)
    if low_npv == 0:
        return round(low, 4)
    if high_npv == 0:
        return round(high, 4)
    if low_npv * high_npv > 0:
        raise ValidationError("IRR not bracketed in search interval; try a wider range or inspect cash flows")

    mid = 0.0
    for _ in range(max_iterations):
        mid = (low + high) / 2
        mid_npv = _npv(mid)
        if abs(mid_npv) < precision:
            return round(mid, 4)
        if low_npv * mid_npv <= 0:
            high = mid
            high_npv = mid_npv
        else:
            low = mid
            low_npv = mid_npv

    return round(mid, 4)


def _load_json_input(raw: str | None, file_path: str | None):
    if raw and file_path:
        raise ValidationError("Use either --json or --file, not both")
    if raw:
        return json.loads(raw)
    if file_path:
        return json.loads(Path(file_path).read_text(encoding="utf-8"))
    raise ValidationError("Either --json or --file is required")


def _build_cli() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Decision analysis helpers for CEO Skill",
    )
    subparsers = parser.add_subparsers(dest="command", required=False)

    monte = subparsers.add_parser("monte-carlo", help="Run Monte Carlo simulation")
    monte.add_argument("--json", help="Inline JSON payload containing scenario list")
    monte.add_argument("--file", help="Path to JSON payload file")
    monte.add_argument("--simulations", type=int, default=DEFAULT_SIMULATIONS)
    monte.add_argument("--seed", type=int)

    matrix = subparsers.add_parser("decision-matrix", help="Run weighted decision matrix")
    matrix.add_argument("--json", help='Inline JSON payload with {"criteria": [...], "options": [...]}')
    matrix.add_argument("--file", help="Path to JSON payload file")

    ice = subparsers.add_parser("ice", help="Run ICE scoring")
    ice.add_argument("--json", help="Inline JSON payload containing initiative list")
    ice.add_argument("--file", help="Path to JSON payload file")

    ev = subparsers.add_parser("expected-value", help="Run expected value analysis")
    ev.add_argument("--json", help="Inline JSON payload containing option list")
    ev.add_argument("--file", help="Path to JSON payload file")

    npv_parser = subparsers.add_parser("npv", help="Calculate NPV")
    npv_parser.add_argument("--rate", required=True, type=float, help="Discount rate, e.g. 0.12")
    npv_parser.add_argument("--json", help="Inline JSON array of cash flows")
    npv_parser.add_argument("--file", help="Path to JSON array file")

    irr_parser = subparsers.add_parser("irr", help="Calculate IRR")
    irr_parser.add_argument("--json", help="Inline JSON array of cash flows")
    irr_parser.add_argument("--file", help="Path to JSON array file")
    irr_parser.add_argument("--precision", type=float, default=0.0001)
    irr_parser.add_argument("--max-iterations", type=int, default=1000)

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = _build_cli()
    args = parser.parse_args(argv)

    if not args.command:
        scenarios = [
            {"name": "Success", "probability": 0.4, "outcome_range": [3000000, 8000000]},
            {"name": "Moderate", "probability": 0.35, "outcome_range": [500000, 2000000]},
            {"name": "Failure", "probability": 0.25, "outcome_range": [-3000000, -500000]},
        ]
        criteria = [
            {"name": "revenue", "weight": 0.3},
            {"name": "risk", "weight": 0.25},
            {"name": "speed", "weight": 0.2},
            {"name": "team_fit", "weight": 0.15},
            {"name": "strategic", "weight": 0.1},
        ]
        options = [
            {"name": "Option A", "scores": {"revenue": 8, "risk": 4, "speed": 9, "team_fit": 7, "strategic": 8}},
            {"name": "Option B", "scores": {"revenue": 6, "risk": 8, "speed": 5, "team_fit": 9, "strategic": 7}},
        ]
        print("=== Monte Carlo Example ===")
        print(json.dumps(monte_carlo_simulation(scenarios, seed=42), indent=2))
        print("\n=== Decision Matrix Example ===")
        print(json.dumps(decision_matrix(criteria, options), indent=2))
        print("\nTip: run with --help to use the CLI.")
        return 0

    try:
        if args.command == "monte-carlo":
            payload = _load_json_input(args.json, args.file)
            result = monte_carlo_simulation(payload, num_simulations=args.simulations, seed=args.seed)
        elif args.command == "decision-matrix":
            payload = _load_json_input(args.json, args.file)
            result = decision_matrix(payload["criteria"], payload["options"])
        elif args.command == "ice":
            payload = _load_json_input(args.json, args.file)
            result = ice_scoring(payload)
        elif args.command == "expected-value":
            payload = _load_json_input(args.json, args.file)
            result = expected_value(payload)
        elif args.command == "npv":
            payload = _load_json_input(args.json, args.file)
            result = {"npv": npv(payload, args.rate)}
        elif args.command == "irr":
            payload = _load_json_input(args.json, args.file)
            result = {"irr": irr(payload, precision=args.precision, max_iterations=args.max_iterations)}
        else:
            parser.error(f"Unknown command: {args.command}")
            return 2
    except (ValidationError, KeyError, json.JSONDecodeError, OSError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
