# Data model direction

Phase 1 creates no business tables. Future tenant-scoped tables will have an
`organization_id`, UUID identity, UTC timestamps, foreign keys, and composite
tenant-first indexes. Planned domains include users/memberships, agents and
keys, tools and immutable versions, policies and rule versions, action requests,
risk assessments, approvals, audit events, incidents, and provenance records.

Audit events will be append-oriented and redacted by default. Secret-bearing
fields must not be persisted in ordinary event payloads.
