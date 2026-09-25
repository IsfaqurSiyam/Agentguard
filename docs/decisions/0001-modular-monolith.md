# ADR 0001: Begin as a modular monolith

## Status

Accepted.

## Context

AgentGuard needs strong consistency across authorization, policy, decisions,
audit records, and controlled execution. Premature service boundaries would add
failure modes and weaken transaction-level testing.

## Decision

Implement modules within one FastAPI deployment first, with clear interfaces.
PostgreSQL is the system of record and Redis supports transient coordination.

## Consequences

Modules can later be extracted when a concrete scaling or isolation requirement
exists. No current module boundary implies permission to bypass gateway policy.
