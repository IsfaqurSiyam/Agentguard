# Architecture overview

AgentGuard is a modular monolith that provides a server-authoritative control
plane between autonomous agents and registered tools. Phase 1 establishes its
local development structure only.

```mermaid
flowchart LR
  A[Agent / SDK] --> G[AgentGuard Gateway]
  G --> I[Identity and authorization]
  I --> P[Deterministic policy]
  P --> D[Detection and risk]
  D --> H[Approval when required]
  H --> E[Controlled HTTP adapter]
  E --> T[Registered HTTP tool]
  G --> AU[Audit and provenance]
  UI[Operator console] --> G
```

The dashboard is never on the authorization or execution path. Future modules
remain in-process initially so their interfaces and database transactions can
be tested together; they may be separated only when an isolation boundary
requires it.
