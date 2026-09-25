# Security flow

The future gateway sequence is: authenticate, authorize, validate the pinned
tool schema, evaluate deterministic policy, detect threats and sensitive data,
assess risk, request approval when required, persist a decision, execute a
registered HTTP adapter, and append audit/provenance records.

```mermaid
sequenceDiagram
  participant A as Agent
  participant G as Gateway
  participant P as Policy
  participant X as HTTP adapter
  A->>G: action request
  G->>G: authenticate + authorize + validate
  G->>P: deterministic evaluation
  P-->>G: allow / deny / approval
  alt allowed
    G->>X: registered tool action
    X-->>G: bounded, redacted result
  end
  G-->>A: persisted decision/result
```

Phase 1 implements only health/readiness infrastructure. It does not yet
evaluate or execute actions.
