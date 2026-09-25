# Local setup

Install Python 3.12+, Node.js LTS, Docker Desktop with Compose, Git, and pnpm
via Corepack. Then copy `.env.example` to `.env`, choose a local PostgreSQL
password, run `corepack enable`, `pnpm install`, and `make dev`.

The Compose backend receives `DATABASE_URL` and `REDIS_URL` from `.env` and
connects to the Compose service names. Run `make compose-config` before startup
to validate interpolation. Use `make db-migrate` after the services are healthy.

On Windows PowerShell use `Copy-Item .env.example .env`. If Make is unavailable,
use `docker compose up --build`, `docker compose run --rm backend alembic upgrade
head`, `python -m pytest`, and the equivalent `pnpm` commands directly.
To run the browser navigation test locally, install its browser once with
`pnpm --filter @agentguard/frontend exec playwright install chromium`.
