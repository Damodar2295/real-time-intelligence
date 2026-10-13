# Current Architecture Decisions and Open Questions

13 October 2026. This concise register preserves current dispositions without meeting transcripts or historical reviews. V4 diagrams are unchanged. CONFIRMED describes target intent, not deployed capability. Owners listed are roles to confirm.

| Topic | Disposition | Decision / evidence required | Owner to confirm |
|---|---|---|---|
| Platform | GCP/GKE target; Lumi internal platform context confirmed | Available services and inherited controls | Lumi platform / architecture |
| Sources | Genesys source; separate emulator role retained | Audio/transcript contract, revisions, STT ownership and coexistence | Integration / speech |
| Handoff | Pub/Sub current proposal; Redis Streams alternative | Latency, delivery, retention, recovery, capacity and Lumi fit | Messaging / SRE |
| Local queue | Colocated prototype option only | Packaging, process-loss, overload and cross-instance handling | Application / platform |
| Windowing | Worker-side baseline retained | Whether ingress-side assembly is justified; flush and revision policy | Ingestion / detection |
| Call state | Bounded same-call context required | Ownership, accepted-history writer, expiry and recovery | Data / ingestion / detection |
| Detection | Applicability-based selective methods confirmed | Invocation, concurrency, completion, timeout and fallback | Signal / detection |
| Semantic path | Top-K retrieval and reranking retained | Embedding/reranker/index versions, quality and capacity | ML / data |
| Resolution | Common acceptance and threshold baseline retained | Evidence validation, score semantics, threshold reconsideration, conflict/abstention and finality | SME / ML evaluation |
| Freshness/loss | No general lossy-processing approval | Reconcile usefulness deadlines with context correctness and recovery | Product / data / SRE |
| Storage | PostgreSQL/vector direction retained provisionally | Separate context/catalog/vector/evidence access patterns; hosting approval | Data / Lumi |
| Model access | Vertex AI or approved endpoint proposed | Approved model, gateway requirement, privacy and quotas | AI platform / security |
| Security | Control responsibilities not verified | Cross-project access, data classification, retention and audit | Security / privacy |
| Output | Workbench evidence/latency role retained | Authenticated delivery, replay, duplicates and write/publish consistency | API / product / data |
| Activation | Later, selective capability | Trigger and consumer contract | Product / downstream |
| Validation | No demonstrated production readiness | Quality, load, recovery, security, usability and cost evidence | Architecture / engineering |

No Cloud Run migration, new response caches, graph runtime, trained classifier, automatic dual publishing or shared Redis instance is selected by this package.
