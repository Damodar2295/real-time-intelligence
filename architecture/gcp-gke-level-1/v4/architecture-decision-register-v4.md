# V4 architecture decision register

**Architecture:** VANTAGE Intelligence | Enterprise Technical Level 1 | V4. **Status:** DRAFT for EARB review. **Target:** GCP/GKE. **Owner:** unassigned. **Review date:** 12 October 2026. **Decision baseline:** latest local V3 including process containers; logical model v1.2, D01–D54 with later entries taking precedence. Earlier source disputes are not silently erased.

CONFIRMED = agreed target behavior, not deployed. PROPOSED = recommendation awaiting approval. OPEN = unresolved contract, owner or choice. V4 review requests authorize representation refinements, not the unresolved implementation decisions below. Stakeholder roles are proposed assignments.

| ID | Decision / disposition | Status | Authority / source | Owner to assign / next evidence |
|---|---|---|---|---|
| V4-D01 | GCP/GKE target retained; no infrastructure readiness asserted | CONFIRMED target | GCP/GKE brief; V3 | Architecture / platform owner; verified environment inventory |
| V4-D02 | Separate emulator; queued transcript ingress precedes scalable ingestion workers | CONFIRMED behavior | U06; D49,D51,D52 | Ingestion owner; concurrency and failure tests |
| V4-D03 | Audio acquisition and streaming STT remain proposed target capabilities | PROPOSED integration | D50; Q49–Q51 | Provider / speech owner; audio and transcription contracts |
| V4-D04 | Applicability-based selective invocation of deterministic, semantic and LLM methods; top-K + reranker retained | CONFIRMED behavior; scheduling OPEN | D13,D30,D35; V3 | Detection owner; completion/fallback policy |
| V4-D05 | All invoked methods feed shared threshold resolution | CONFIRMED acceptance boundary | D46 | Signal/ML owners; calibrated evidence and acceptance contract |
| V4-D06 | Threshold scope, score interpretation, conflict/duplicate handling, rejection/abstention and finality | OPEN | D48; Q47,Q48; V4-R07/R08 | Signal owner; business SME sign-off and evaluation |
| V4-D07 | Context is bounded and same-call; prior signals are required context, writer/expiry/recovery unspecified | CONFIRMED scope; ownership OPEN | D31; Q36,Q45,Q54 | Data + detection + ingestion owners; state lifecycle contract |
| V4-D08 | Pub/Sub, Memorystore, Cloud SQL hosting, Vertex AI, cloud telemetry, IAM/WIF/secrets/network controls retain prior recommendation | PROPOSED | Prior technical decision record | Respective enterprise service owners; approval and capability fit |
| V4-D09 | Existing PostgreSQL remains alternative; full-call/audit/result authority, retention and publication consistency require approval | OPEN | Q40,Q42,Q45; V3 persistence mapping | Data/records owner; authoritative data lifecycle |
| V4-D10 | BigQuery reference-only; no new response-cache tier, graph dependency, classifier runtime or API gateway | Retained scope; no selection | U06; D14; V3 | Architecture owner; explicit change decision if needed |
| V4-D11 | Later contextual generation/activation distinct from detection; consumer contracts unresolved | CONFIRMED concern; integration OPEN | C27–C29; D01 | Product/downstream owners; activation contract |
| V4-D12 | Signal, prompt, model and index version coordination, golden datasets and review workflow | PROPOSED discipline; implementation OPEN | D18,D21,Q42; V4-R06/R17/R18 | Business SME / AI governance; approved evaluation plan |
| V4-D13 | Architecture owner, formal enterprise standards and control inheritance are not established by provided artifacts | OPEN | Baseline-review limits | EARB / enterprise security; named accountable owners and standards |
| V4-D14 | Preserve stable draw.io IDs; correct source refs; add status metadata, separate telemetry notation and boundary qualifications | Applied representation refinement | V4 user request; V4-R21/R22 | EARB reviewer to assess; no runtime behavior changed |

## Data authority and recovery register

“Candidate” storage below is a proposal, not the source of truth by default.

| Data category | Current representation | Authoritative source / owner | Retention, classification, recovery decision |
|---|---|---|---|
| Audio | Genesys stream / proposed STT session | Provider source identified; access/recording owner OPEN | Capture/replay, legal authorization, encoding and permitted storage OPEN |
| Transcript event/revision | Ingress → queue → workers | Canonical revision authority and schema OPEN | Partial/final corrections, timestamps, idempotency key, retention and replay OPEN |
| Microbatch/session window | Ingestion workers | Assembly responsibility confirmed; ownership protocol OPEN | Window size/flush/overlap, call handoff and reconstruction OPEN |
| Bounded conversation context | Memorystore proposed | Derived working state; not automatically durable authority | TTL, eviction, prior-signal writer and restart behavior OPEN |
| Signal catalog / applicability | Signal Management; SQL proposed | Business authoring/approval authority OPEN | Required schema, activation, rollback and active-call consistency OPEN |
| Examples / vector representations | PostgreSQL/pgvector direction; Cloud SQL hosting proposed | Approved examples owner OPEN; index is derived | Embedding/version lineage, rebuild source and deletion propagation OPEN |
| Detector evidence / decisions | Shared resolution | Acceptance responsibility confirmed; durable provenance owner OPEN | Evidence retention, input/config/model versions, abstention/rejection semantics OPEN |
| Accepted signals / event history | Publisher; SQL result mapping proposed | Persistence owner and authoritative record OPEN | Write/publish consistency, retries, duplicates and replay OPEN |
| Full conversation / audit history | No selected system; BigQuery reference-only | Records/data owner OPEN | Classification, permitted fields, duration, deletion and access OPEN |
| Logs / metrics / traces | Cloud Observability proposed | Observability owner OPEN; not business truth by assumption | Redaction, sampling, identity correlation, retention and access OPEN |

## Security responsibility proposal

These are candidate responsibilities to ratify, not evidence of inherited controls.

| Enterprise/platform-owned control candidates | VANTAGE application-owned control candidates | Joint decisions |
|---|---|---|
| Organization policies, project/network foundations, workload identity platform, approved key/secret services, cluster baseline and enterprise audit sinks | Per-workload least privilege requests, source/consumer authorization enforcement, safe transcript/model/log handling, call-context isolation, schema validation and decision provenance | Trust boundaries; service-to-service authentication; egress/model approval; data classification; encryption/key policy; retention/deletion; audit access; incident and change ownership |

GCP and GKE borders indicate platform/runtime placement. Dotted process groups are visual organization. Neither constitutes a confirmed trust boundary. No private endpoint, mTLS, gateway, customer-managed key or production authentication implementation is implied.

## Proposed performance evaluation objectives — no new SLO

Agree a workload envelope (concurrent calls, event rate, utterance length, method mix) and measure event age plus stage P50/P95/P99 under normal and failure conditions. Instrument audio arrival, usable/final transcription, publish acknowledgement, queue wait, normalization/window wait, applicability, each invoked detector including vector/model wait, resolution, publication and agent-visible delivery. These are proposed measurement points, not verified instrumentation.

Distinguish event timestamps from local processing duration; clock/correlation strategy is OPEN. Track queue backlog/age, model/database saturation, cache latency and dropped/duplicate/revised events alongside quality. Approval criteria should jointly cover false positives/negatives and latency. Earlier internal deterministic POC targets remain historical engineering targets, not a measured V4 SLA or a budget automatically applicable to STT/reranking/LLM. No arbitrary numerical objective is added.
