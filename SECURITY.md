# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability, please follow these steps:

1. **Do NOT create a public GitHub issue** for security vulnerabilities
2. Email the maintainer directly at: mtp354@gmail.com
3. Include the following information:
   - Description of the vulnerability
   - Steps to reproduce the issue
   - Potential impact
   - Suggested fix (if any)

We will respond to security reports within 48 hours and will keep you updated on our progress toward a fix.

## Security Considerations for Quantum Computing

This package deals with quantum computing protocols that may have cryptographic implications:

- **Quantum Key Distribution**: Be aware that quantum communication protocols may be sensitive
- **Delegated Computing**: Ensure that sensitive quantum circuits are properly protected
- **Verification Protocols**: The CHSH-based verification should be implemented securely

## Best Practices

When using this package in production:

1. Keep dependencies up to date
2. Use secure communication channels for quantum delegation
3. Validate all input parameters
4. Monitor for timing attacks in verification protocols
5. Follow quantum cryptography best practices