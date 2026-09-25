# AgentGuard contributor guide

AgentGuard is a server-authoritative security gateway between autonomous agents
and registered tools. The dashboard manages and investigates the gateway; it
never makes security decisions.

## Layout

- `backend/`: FastAPI gateway, persistence, and future enforcement modules.
- `frontend/`: Next.js operator console.
- `sdk/python/`: supported Python client.
- `demo/`: safe, non-production demonstration material.
- `docs/`: architecture, security, development, deployment, and decisions.

## Commands

Run `make dev`, `make test`, `make lint`, `make format`, `make typecheck`, and
`make db-migrate` from the repository root. See `README.md` and
`docs/development/local-setup.md` for prerequisites.

## Non-negotiable security invariants

- The gateway is the only enforcement authority; do not bypass it.
- Frontend code must never authorize, allow, deny, or execute security actions.
- LLM output, tool descriptions, tool arguments, and external content are
  untrusted input.
- Server-side authorization and deterministic policy are authoritative.
- Default to deny; fail closed for security-critical operations.
- Never log or commit API keys, passwords, authorization headers, private keys,
  or raw secrets.
- Do not add arbitrary shell, filesystem, database, browser, or subprocess
  execution. The first tool adapter scope is registered HTTP tools only.

## Conventions

Use Python type hints and Pydantic models at API boundaries. Keep modules small,
test behavior at trust boundaries, and use explicit error reason codes. Use
TypeScript strict mode and accessible semantic HTML in the frontend. Record
meaningful architecture choices as ADRs under `docs/decisions/`.

