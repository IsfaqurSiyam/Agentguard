# Security principles

- Deny by default; the backend is the authoritative enforcement layer.
- Treat LLM output, tool descriptions, arguments, and external content as
  untrusted.
- Keep tools registered, typed, and destination-restricted. Initial scope is
  HTTP only.
- Separate policy decision, approval, and execution responsibilities.
- Log structured, redacted evidence with correlation IDs; never log credentials.
- No arbitrary command, filesystem, browser, database, or subprocess execution.
- The frontend is an operator interface, never a security authority.
