# Meeting 005 — architecture-relevant extract

Recorded 2026-10-08; source is user-supplied latest meeting. Speaker identity, actual date and deployment state are not independently verified. Attached role brief is contextual material, not independent authorization or architecture evidence.

## User direction

**U05:** The user now requests a consolidated/finalized layered architecture and justified draw.io updates. This supersedes U02's diagram hold. “Finalized” is treated as completing this evidence-based design artifact, not inventing unresolved choices or claiming production approval.

- **M05.1 — Prototype modules.** Transcript Emulator, Ingestor, Detector and signal-management UI/capability are discussed; opening count “three modules” does not establish exact deployable-service count. Extend emulator to multiple concurrent streams; prototype single-transcript WebSocket flow is reported, not tested here.
- **M05.2 — Ingestion responsibilities.** Normalize, manage independent interaction sessions, segment/buffer/window utterances, track buffers, maintain per-conversation context and retain larger conversation. Sequencing is raised. Current context versus full conversation storage remains distinct. Speaker/timestamp handling is corroborated by P05. Exact batch sizes, order rules, event contract and storage guarantees absent.
- **M05.3 — Three detection methods.** Deterministic, semantic and LLM-based are explicitly named as current methods; signals predefine their detection method. Semantic configuration can include thresholds and positive/negative examples. Resolves the earlier unnamed third method; does not restore the separate configured/trained classifier implementation or select GPT 4.1 mini. No runtime parallelism/wait policy established.
- **M05.4 — Interface, identity and adapters.** Use call ID as session/correlation ID in the prototype; preserve atomic handling of mini-batches, with atomicity boundary undefined. Default WebSocket adapter first; future Genesys/outreach provider adapters and strategy pattern discussed. Adapter logically precedes ingestion; package may reside inside Ingestor. Emulator separation versus embedding is debated with no unambiguous final packaging decision. Do not assume number of sockets, one socket per call, exactly-once processing or selected provider DTO contract.
- **M05.5 — Signal Management.** Explicitly replace “policy manager” terminology with “signal management.” Unified basic signal definition should cover deterministic, semantic and LLM properties. Schema is still being established; P01/P02 are planned attributes, not approved production schema. Build UI similar to VANTAGE; actual reuse/extension/integration decision absent.
- **M05.6 — Composites.** Two signals leading to a third is recognized as a low-priority task. Prioritize basic signal definitions; no composition operators/window/recursion semantics specified.
- **M05.7 — Observability.** End-to-end logging/tracing of what happened and time taken at each stage required. No backend/tool selected.
- **M05.8 — Infrastructure.** Meeting reports a “p vector Postgres” instance associated with “sales profit,” configuration and first embeddings needed; GKE provisioning reportedly started. PostgreSQL vector use and GKE plan are source-backed, but exact extension, spelling/identity, versions, readiness, cluster mapping and deployment topology are unverified. P05 shows BigQuery persistence as a reference-design option, not an explicit meeting approval.
- **M05.9 — Shared development.** One common Git repo/monorepo with modules and architecture documents together is requested; separate developer ecosystems discouraged. No repo URL, module names, CI/CD or service-to-pod mapping supplied.
- **M05.10 — Auth and ambiguities.** Authentication “may not be required to start” is a suggestion for the initial interface, not a production decision or removal of Genesys OAuth. Mention of “Webhook” is not sufficient to add a second transport alongside the repeatedly specified WebSocket. Missing scope remains open.

## User clarifications

**U06:** User explicitly chooses a separate emulator module/service and confirms BigQuery is a reference-design option for now. This resolves emulator separation while leaving adapter packaging open. BigQuery is not promoted to a prototype dependency.
