# AgentGuard

AgentGuard is an open-source, server-authoritative security gateway for
autonomous AI agents. It evaluates a registered agent action before a registered
tool can execute it. The dashboard is an operator interface, not a security
authority.

> Phase 1 provides project foundation only. It does not yet provide agent
> registration, policy enforcement, tool execution, approvals, audit chains, or
> production authentication.

## Local development

Prerequisites: Git, Python 3.12+, Node.js LTS, Docker Desktop with Compose, and
GNU Make (or a compatible `make` command). Copy `.env.example` to `.env` and
replace the local PostgreSQL password before exposing the stack beyond your
machine.

```sh
git clone <repository-url> agentguard
cd agentguard
cp .env.example .env
corepack enable
pnpm install
make dev
```

The backend is available at `http://localhost:8000/api/v1/health`; the frontend
is available at `http://localhost:3000/dashboard`.

Run checks with:

```sh
make format
make lint
make typecheck
make test
make db-migrate
```

For Windows PowerShell, use `Copy-Item .env.example .env`. If `make` is not
available, use the underlying commands described in
[`docs/development/local-setup.md`](docs/development/local-setup.md).

## Documentation

- [Architecture overview](docs/architecture/overview.md)
- [Security flow](docs/architecture/security-flow.md)
- [Security principles](docs/security/security-principles.md)
- [Local setup](docs/development/local-setup.md)
- [Architecture decision 0001](docs/decisions/0001-modular-monolith.md)

Licensed under [Apache-2.0](LICENSE).

