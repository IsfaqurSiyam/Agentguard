# Preliminary threat model

Primary trust boundaries are agent-to-gateway, gateway-to-registered-tool,
operator-to-control-plane, and persistence-to-audit evidence. Threats include
direct/indirect prompt injection, tool poisoning, unauthorized access,
privilege escalation, secret/PII exfiltration, SSRF, path traversal, malicious
URLs, compromised tools, stolen API keys, replay, audit tampering, approval
manipulation, multi-agent propagation, denial of service, and excessive
autonomy.

Phase 1 mitigations are intentionally limited to safe defaults: narrow CORS,
request correlation, redacted logging, no execution surface, and no hardcoded
credentials. The full threat-to-control matrix is deferred until gateway and
tool contracts exist in later phases.
