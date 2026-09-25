# Local deployment

Local Compose runs PostgreSQL 16, Redis 7, the FastAPI backend, and Next.js
frontend on an isolated bridge network. It is for development only. Use a
non-default password in `.env`; do not expose the ports to an untrusted network.

The backend readiness endpoint checks PostgreSQL and Redis. Future self-hosted
and SaaS deployments will use externally managed secrets, TLS termination,
backups, monitoring, and stricter network policies.
