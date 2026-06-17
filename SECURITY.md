# Security Policy

## Supported Versions

We currently support the following versions with security updates:

| Version | Supported          |
| ------- | ------------------ |
| Latest  | :white_check_mark: |

## Reporting a Vulnerability

We take the security of CEO Skill seriously. If you believe you have found a security vulnerability, please report it to us as described below.

### How to Report

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via one of the following methods:

1. **GitHub Security Advisories** (preferred): Use the [Security tab](https://github.com/AIPMAndy/CEOskill/security/advisories/new) to privately report a vulnerability
2. **Email**: Send details to andy@aipm.dev (if available) or create a private issue

### What to Include

Please include the following information in your report:

- Type of vulnerability
- Full paths of source file(s) related to the vulnerability
- Location of the affected source code (tag/branch/commit or direct URL)
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit it

### Response Timeline

- We will acknowledge receipt of your vulnerability report within 48 hours
- We will provide a more detailed response within 5 business days
- We will work with you to understand and validate the issue
- We will release a fix as soon as possible, depending on complexity

### Disclosure Policy

- We request that you do not publicly disclose the vulnerability until we have released a fix
- We will credit you in the security advisory (unless you prefer to remain anonymous)
- Once the fix is released, we will publish a security advisory

## Security Best Practices

When using CEO Skill:

1. **Sensitive Information**: Do not include confidential business information, trade secrets, or personal data in public examples or issues
2. **API Keys**: Never commit API keys, tokens, or credentials to the repository
3. **Python Scripts**: Validate all inputs when using the included analysis tools
4. **Dependencies**: Keep dependencies up to date by regularly checking for updates
5. **Code Review**: Review any custom decision analysis scripts before execution

## Scope

This security policy applies to:

- The main CEO Skill codebase (SKILL.md, reference files, scripts)
- Python analysis tools in the `scripts/` directory
- Documentation and examples (to prevent information disclosure)

Out of scope:

- Third-party AI models or runtimes (OpenClaw, Claude Code, etc.)
- User-specific implementations or customizations

## Contact

For questions about this security policy, please open a discussion in the [GitHub Discussions](https://github.com/AIPMAndy/CEOskill/discussions) or contact the maintainer through GitHub.

Thank you for helping keep CEO Skill and its users secure!
