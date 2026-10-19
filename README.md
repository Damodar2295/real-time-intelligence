# Vantage Real Time Intelligence

## Overview

VANTAGE identifies meaningful business signals during active customer conversations and delivers accepted detections with evidence to a signal workbench and authorized downstream consumers. Responsibilities are source acquisition, transcript ingress, bounded same-session context, catalog-driven selective deterministic/semantic/LLM detection, shared signal resolution and delivery. Later contextual generation and activation remain separate from core detection.

**Redis Streams is the authoritative real-time ingress requirement. SafeChain is the mandatory internal secure integration for every LLM invocation.** Non-LLM components do not need SafeChain in their execution path. Technical interfaces and runtime implementation are not established by these architectural requirements.

This is the single authoritative README for the V4 review branch. It retains the existing V4 structure and incorporates the approved Redis Streams, SafeChain and presentation corrections in place. The previous diagram remains recoverable in Git commit `65bdd04`. The repository contains architecture tooling, not a demonstrated application runtime. Named owners and production approval remain outstanding. Review date: 19 October 2026.

## Final Level 1 Architecture

![Final VANTAGE Real-Time Intelligence Level 1 Architecture — V4](architecture/gcp-gke-level-1/v4/vantage-gcp-gke-technical-level-1-v4.png)

**Architecture baseline:** V4 — Final

**Ingress:** Redis Streams

**Secure LLM Integration:** SafeChain Integration

[Editable V4 draw.io](architecture/gcp-gke-level-1/v4/vantage-gcp-gke-technical-level-1-v4.drawio) · [SVG](architecture/gcp-gke-level-1/v4/vantage-gcp-gke-technical-level-1-v4.svg)

The approved corrections are applied to the existing V4 diagram: the title is **Vantage Real Time Intelligence**, `queue` is Redis Streams, and `model` is SafeChain Integration. All 38 graph elements, 25 interface IDs, endpoint relationships and process groups are retained. AR-01/02 visual inconsistencies are resolved; API contracts, hosting and runtime verification remain open. AR-03 is clarified by “V4 — Final reference”; this is not production approval.

V4 groups interaction ingestion, detection/orchestration and resolution/output within the GKE target. Platform services and the logical enterprise integration boundary appear outside the workload grouping. SafeChain's position preserves V4's layout and does not establish its physical hosting or ownership in GCP. It provides secure access to enterprise-approved LLM models; no additional model node or provider bypass is introduced. Future contextual generation must use SafeChain whenever it invokes an LLM.

## 3. Architecture Objectives

Identify signals soon enough to influence the active conversation; preserve call identity, evidence and version lineage; support concurrent calls; select relevant signals from metadata; keep business configuration separate from runtime processing; deliver understandable outcomes and latency information. Discussed cases include semantic product claims, verbatim disclosures and prior-event-dependent checks. They require SME-approved examples and acceptance criteria before implementation.

The supplied catalog is currently Sales Compliance. Domain scope is not expanded to new business capabilities. No production latency SLA, throughput target, model, trained classifier, response-cache tier or graph platform is introduced. Reuse comes from source adapters, versioned definitions and common contracts, not a new framework.

## 4. Guiding Principles

| Principle | Application to VANTAGE | Evidence/status |
|---|---|---|
| Scalability and isolation | Concurrent calls with bounded work and per-session state integrity | Target; ownership/recovery/load tests required |
| Modularity and contracts | Catalog configures; detectors provide evidence; resolver accepts; publisher delivers | Established responsibility model; payload bindings incomplete |
| Security and privacy | Mandatory SafeChain for LLMs, least privilege, permitted transcript handling | Required path; implementation/controls unverified |
| Performance and cost | Select methods, bound expensive inference and measure stage/tail latency and usage | No arbitrary SLO or cost budget selected |
| Resilience | Redis groups, ack, retry, pending recovery, dead-letter and replay policies | Required; executable integration absent |
| Interoperability | Stable IDs, snapshot/schema versions and explicit producer/consumer boundaries | Supplied detection input/output fields; transport details TBD |
| User-centric review | Evidence, multi-label results, freshness and feedback | Workbench role established; user validation pending |
| Sustainability/maintainability | Reproducible artifacts and bounded resource use | Tooling exists; runtime efficiency not demonstrated |

These are design principles, not compliance certification. The supplied enterprise reference does not establish inherited Lumi controls or operating approvals.

## 5. Architecture Scope and Boundaries

Lumi is the internal GCP platform; GKE is the target runtime. Provider integration and the separate emulator are upstream. Audio acquisition/STT are proposed, not proven live integrations. Managed database/context/model products in V4 remain proposed hosting choices; public product availability is not Lumi approval. Redis Streams is selected; Redis stream delivery and conversation state remain distinct responsibilities.

No application source, deployment configuration, Redis runtime, SafeChain client or application test suite exists in the inspected sharing baseline. Signal Catalog demo behavior is documented in supplied images, but catalog.json, server.py, index.html and the workbook were not provided as executable artifacts. Do not infer implemented services from architecture Python generators.

SafeChain's required role comes from the latest explicit user instruction. Its internal API, credentials, enforcement and deployment model remain **TBD — Detailed Design Decision Required**. No new intermediate service is invented. Non-LLM embedding/reranking does not acquire an LLM dependency by inference; any selected implementation that actually invokes an LLM must use SafeChain.

## 6. V4 Architecture Walkthrough

1. Genesys source and proposed audio/STT acquisition supply transcripts; emulator supplies test transcripts over the documented WebSocket path. The exact provider contract is open.
2. Transcript ingress frames updates and preserves call/session identity. Its handoff must use Redis Streams under the current requirement; V4 now represents this as Redis Streams.
3. Ingestion workers normalize, handle same-call ordering and prepare windows/microbatches. Worker-side windowing remains the baseline; no relocation to ingress has been approved.
4. Bounded context is updated by workers and supplied to coordination. Accepted-history writer, expiry and recovery remain open.
5. Signal Management supplies versioned applicability and detector configuration. Coordination invokes configured methods; all three do not run for every event.
6. Deterministic and semantic paths produce evidence. The LLM adapter must invoke approved models through SafeChain and validate returned output; V4 now explicitly represents SafeChain Integration.
7. Shared resolution determines acceptance from evidence and agreed threshold semantics. Publication supplies accepted results; later generation/activation is selective and also must use SafeChain if it invokes LLMs.
8. Operational instrumentation and enterprise controls apply across the flow. Product names and arrows do not establish deployed security or reliability guarantees.

## 7. Major Components and Responsibilities

Status **P** means Planned / Contract Required; **D** means local demo behavior documented but not execution-verified. No runtime component is claimed implemented. GCP/GKE are target boundaries. Owner names are TBD; roles are suggested reviewers. Stable IDs map to the original graph; visual headings and legend cards are notation, not components.

| V4 ID / component | Purpose and responsibilities | State ownership | Owner role / status |
|---|---|---|---|
| `gcp` — Google Cloud / Lumi boundary | Define target platform scope | Platform configuration; operational owner TBD | Lumi / enterprise architecture; P |
| `gke` — GKE application runtime | Host target application workloads | Cluster configuration; application state owned separately | Platform / SRE; P |
| `genesys` — Genesys Cloud | Provide live interaction source | Provider call identity and source lifecycle | Integration / Genesys; P |
| `test` — Transcript emulator | Exercise concurrent calls as a separate test source | Fixture/session progression | Test / ingestion; P |
| `provider` — Provider integration | Describe source authentication, format and reconnect responsibilities | Credential references and session continuity; owner TBD | Integration; P |
| `bridge` — Audio acquisition | Adapt permitted live audio for speech recognition | Active audio/STT session state | Integration / speech; P |
| `stt` — Speech-to-Text | Produce transcript updates for proposed audio path | Recognition sessions; retention unspecified | Speech / Lumi; P |
| `ingress` — Transcript ingress | Adapt and frame identifiable transcript updates | Source-to-session mapping; publication work | Ingestion; P |
| `queue` — Redis Streams | Authoritative real-time stream handoff | Pending delivery and retained entries; not conversation truth | Architecture / platform; P |
| `worker` — Ingestion worker pool | Prepare coherent per-session detection input | Per-call progress, buffers and window state | Ingestion / detection; P |
| `state` — Memorystore for Redis | Provide bounded same-call working context | Derived context; prior accepted-history writer unassigned | Data / ingestion; P |
| `management` — Signal Management UI / API | Maintain versioned taxonomy and detection configuration | Catalog authority and snapshot lifecycle; owner TBD | Catalog / business SME; D |
| `sql` — Cloud SQL · PostgreSQL | Candidate catalog, vector and result storage | Separate data categories; authority and transaction boundaries TBD | Data / Lumi; P |
| `coord` — Detector coordination | Select applicable signals and configured methods | In-flight evaluation/version references | Detection; P |
| `rules` — Deterministic detection | Evaluate configured rules/matching | Rule/config version; does not own call history | Detection / SME; P |
| `semantic` — Semantic detection | Embed, retrieve top-K and rerank | Model/index/example provenance | ML / data; P |
| `llm` — LLM detection adapter | Evaluate scoped requirement/context through mandatory SafeChain | Prompt/model/catalog/evaluation provenance | AI platform / security; P |
| `model` — SafeChain Integration | Mandatory enterprise integration for secure access to approved LLM models | Integration/model version; no new credentials/config invented | AI platform / Lumi; P |
| `resolver` — Shared Signal Resolution | Accept method evidence under configured signal rules | Decision identity, dedup and finality owner TBD | SME / ML; P |
| `publisher` — Signal publication API | Deliver accepted signals | Delivery progress; authoritative result store TBD | API / data; P |
| `workbench` — Signal workbench | Display actionable evidence and latency for review | Display session state; not business source of truth | UI / product; P |
| `later` — Contextual generation / activation | Provide selective later follow-on after acceptance | Action/effect tracking and context authority TBD | Product / downstream; P |
| `consumers` — Downstream consumers | Consume later intelligence/activation under agreed contracts | Consumer-side effect/dedup responsibility TBD | Downstream; P |
| `telemetry` — Cloud Observability | Collect logs, metrics and traces | Operational retention and audit access TBD | SRE / application owners; P |
| `controls` — Identity, secrets & network controls | Provide agreed enterprise/application control boundary | Control configuration and secret references | Security / Lumi; P |
| `governance` — Enterprise governance | Define access, retention, privacy and audit accountability | Policy decisions, approval evidence and retention authority | Enterprise governance / privacy; P |

## 8. Component Interaction Matrix

All 25 original interface IDs and endpoint pairs are retained in V4. The approved Redis and SafeChain labels are reflected below. Unrelated proposed protocols remain proposals; SafeChain transport and API details are not inferred.

| Interface | Source → destination | Contract/mechanism and success responsibility | Failure / open binding |
|---|---|---|---|
| `edge-1` | genesys → bridge | Live audio source; provider interface OPEN | Reconnect, source permissions and encoding |
| `edge-2` | bridge → stt | Audio request / transcript response; gRPC/TLS proposed | Finality, correction, speech ownership and timeout |
| `edge-3` | bridge → ingress | Identifiable transcript events | Canonical source envelope and continuity |
| `edge-4` | test → ingress | Documented WebSocket emulator input | Fixture conformity, disconnect/revision cases |
| `edge-5` | ingress → queue | Redis Streams entry publication | Envelope, names, publish retry identity and durability |
| `edge-6` | queue → worker | Redis Streams consumer-group delivery | Ownership, pending recovery, idempotency and ack boundary |
| `edge-7` | worker → coord | Microbatch / detection input; gRPC remains original proposal | Utterance-to-window mapping and completion contract |
| `edge-8` | worker → state | Recent conversation-state update; Redis/TLS proposed | Atomicity, expiry and reconstruction |
| `edge-9` | state → coord | Same-call context; read packaging OPEN | Missing state versus empty history |
| `edge-10` | coord → rules | Configured deterministic request | Invalid config, deadline and evidence schema |
| `edge-11` | coord → semantic | Selected semantic evaluation | Index/model compatibility and timeout |
| `edge-12` | coord → llm | Selected scoped LLM evaluation | SafeChain request/response binding and deadline |
| `edge-13` | rules → resolver | Deterministic evidence | Do not invent confidence probability |
| `edge-14` | semantic → resolver | Reranked semantic evidence | Score semantics/calibration and missing candidates |
| `edge-15` | llm → resolver | Validated LLM evidence | Malformed output, missing evidence and late results |
| `edge-16` | llm → model | Secure LLM invocation through SafeChain Integration | No bypass; API/auth/config/error contracts not supplied |
| `edge-17` | semantic → sql | Vector query/results; SQL/TLS proposed | Compatible index, retrieval failures and data access |
| `edge-18` | management → coord | Versioned catalog configuration; fetch/push OPEN | Snapshot selection/pinning/rollback |
| `edge-19` | management → sql | Proposed catalog/example persistence | Authority, validation and publication consistency |
| `edge-20` | resolver → publisher | Accepted multi-label output | Finality, duplicates and internal failure statuses |
| `edge-21` | publisher → workbench | Delivery; SSE/WebSocket over HTTPS proposed | Access, reconnect, latency and corrected outcomes |
| `edge-22` | publisher → sql | Proposed accepted-result persistence | Write/publish ordering and evidence retention |
| `edge-23` | resolver → later | Selective follow-on after acceptance | Trigger and action authorization; SafeChain for any LLM calls |
| `edge-24` | later → consumers | Later activation delivery; contract OPEN | Idempotent effects, authorization and failure visibility |
| `edge-25` | gke → telemetry | Logs/metrics/traces; cross-cutting collection | Redaction, retention, correlation and alert ownership |

## 9. High-Level End-to-End Processing Flows

**Ingestion:** provider/emulator → transcript ingress → required Redis Streams → consumer-group workers → normalization and bounded same-session preparation. Raw Redis envelope and detection request are separate boundaries. The V4 broker labels now reflect Redis Streams.

**Intelligence:** prepared request plus catalog snapshot/context → applicability → selected methods → evidence → shared resolution → accepted detections. Concurrency can exist across calls and evaluations; no automatic fixed rule → semantic → LLM chain is selected.

**Secure LLM execution:** calling VANTAGE component → SafeChain integration → enterprise-approved LLM model → SafeChain response → caller validation/evidence. This is the mandatory conceptual boundary, not an invented API or a new deployment. Its actual endpoint/SDK/configuration remains TBD. No direct-to-provider fallback is allowed as a proposed alternative.

**Failure/recovery:** processing interruption → retained pending work → safe ownership recovery and repeat-safe processing → acknowledgement after completion or verified durable handoff. Failed processing uses agreed bounded retry and dead-letter handling; operational visibility must remain. Exact mechanics are not implemented.

**Delivery:** accepted envelope → publication → authorized workbench/consumer. Consumer logic uses IDs and versions; actions use catalog mappings. Evidence acceptance does not authorize an external action. Later LLM-based generation must follow SafeChain.

**Concurrent sessions:** A1, B1, A2 and B2 remain isolated by session identity and ordering policy. Call-based partitioning was a recommendation, not an approved count/topology. Partial/final corrections, multi-utterance disclosures, delayed model evidence and worker restart must be covered by contract tests. One call does not imply one thread, pod or Redis stream.

## 10. Redis Streams Ingress and Processing

Redis Streams is mandatory, not an alternative. No runtime broker code exists in the inspected repository. This task updates only the existing diagram, exports and supporting documentation/tooling; Redis processing is not implemented here.

All unspecified items below are **TBD — Detailed Design Decision Required**. These tables identify the engineering contract to agree; they do not introduce invented production values.

### Producer

| Item | Agreed requirement / unresolved binding |
|---|---|
| Stream names and naming convention | TBD; no actual stream keys exist in repository |
| Source adapter responsibility | Frame identifiable transcript updates; retain session/source metadata; use synthetic data for emulator |
| Event envelope / serialization | TBD; do not assume supplied detection input is the Redis envelope |
| Schema version | Required design concern; field name, registry and compatibility policy TBD |
| Event ID / idempotency | Stable logical identity across publish retries required; field/key derivation TBD; Redis entry ID alone does not define business identity |
| Correlation / source | Preserve source and call/session correlation; mapping to detection request_id/session_id/utterance_id TBD |
| Event timestamp | Preserve actual source time where available; required detection event_timestamp is UTC ISO-8601; missing-source policy TBD |
| Payload | Transcript update and supplied metadata; revision/finality/source sequence and metadata binding TBD |
| Validation | Framing, permitted size and required envelope checks before publication; detector input validation separately at its boundary |
| Publish failure | Do not report successful downstream delivery; stable retry identity, backoff, limits and caller response TBD |
| Partial/final handling | Preserve available finality information; exact buffering, revision and publication behavior TBD |

### Consumer

| Item | Required behavior / unresolved binding |
|---|---|
| Consumer group strategy | Redis groups required; names, group count, partition mapping and assignment TBD |
| Consumer identity | Distinguishable worker identity; format and restart lifecycle TBD |
| Processing ownership | Prevent conflicting same-call state mutation; ownership lease/fencing or equivalent is not selected |
| Acknowledgement | After successful processing or verified durable handoff; exact context/job/output commit boundary TBD |
| Pending recovery | Inspect unfinished work and reclaim safely after ownership/liveness decision; command/version compatibility, idle threshold and batch size TBD |
| Retry | Repeat-safe handling, attempt tracking, retryable versus permanent classification; budgets/backoff TBD |
| Dead-letter | Required target; stream/location, payload minimization, redrive authorization, retention and commit/ack consistency TBD |
| Idempotency | Cover context changes, detector scheduling and publication effects; key, state store and retention TBD |
| Processing timeout | Deadline/claim interaction TBD; avoid recovery taking work from a still-authorized healthy processor |
| Shutdown/restart | Stop intake, complete or durably hand off eligible work, preserve pending recovery; grace period and reassignment TBD |
| Contract failures | Invalid input must remain visible; exact error and dead-letter classification TBD |

### Delivery and operation

| Concern | Contract obligation |
|---|---|
| Delivery semantics | Design for duplicate/redelivered work and at-least-once handling within approved persistence/retention; end-to-end guarantees must be measured |
| Ordering | Stream order is not source event-time order or concurrent completion order; define sequence/revision and same-call processing rules |
| Replay | Distinguish operational recovery, context reconstruction and user-visible redelivery; authorization, start point and stale-event handling TBD |
| Checkpoints | Define processing/context/output progress and commit consistency; acknowledgement alone is not a business checkpoint |
| Retention/trimming | Set bounds after deciding pending recovery, consumer progress, replay window and memory budget; never assume XACK deletes stream payload |
| Lag/pending | Monitor unread backlog, pending age/count, processing age and recoveries; alert thresholds TBD |
| Backpressure | Bound intake and in-flight work; overload admission/throttle behavior TBD; no silent drop policy |
| Capacity/availability | Measure memory, event size/rate, active calls, Redis outages/failover and downstream bottlenecks |

A worker crash after state update but before durable scheduling is a critical consistency case. Another is successful output followed by failure before acknowledgement. Neither is solved merely by adding a retry loop.


## 11. SafeChain — Secure LLM Invocation

**SafeChain is the mandatory internal enterprise integration for secure LLM invocation.** Every VANTAGE component that calls an LLM must use this boundary. It does not replace deterministic detection, ordinary vector retrieval, signal acceptance or enterprise governance. It is not an alternative model gateway choice.

| Concern | Required architecture / actual evidence |
|---|---|
| Architectural responsibility | Secure internal LLM invocation mechanism, as explicitly directed by the user |
| Calling components | LLM detection adapter; later contextual generation/activation if it invokes an LLM; any future LLM-backed component |
| Current interface | No SafeChain API, SDK, request/response schema or configuration supplied or found in the inspected code |
| Request handling | Bind permitted context, requirement and correlation through the actual SafeChain contract once provided; no payload fields invented |
| Response handling | Validate actual SafeChain/model response before treating it as evidence; do not equate model output with accepted signal |
| Errors / timeouts | Preserve failure visibility; policies, deadlines, retryability and error mapping TBD; no direct-provider bypass |
| Configuration dependencies | Endpoint/SDK identity, model allowlisting, credentials and environment binding TBD; no secret names or flags invented |
| Security responsibilities | Mandatory use established; specific auth, filtering, encryption and audit mechanisms not evidenced |
| Observability | Correlate permitted request/utterance/evaluation and model versions; latency/error metrics proposed; SafeChain telemetry fields TBD |
| Implementation / tests | No implementation/configuration found; no calls or SafeChain test execution demonstrated |
| Compliance gap | SafeChain is now explicit in V4; runtime integration and bypass prevention remain unverified |

The previous interpretation of SafeChain as a selectable execution feature is superseded. No existing implementation was removed or disabled. Contract acquisition and tests are prerequisites for coding this integration. If SafeChain fails, the required detection outcome and retry/degradation policy must be agreed; silently calling the provider directly is not a proposed recovery path.

## 12. Intelligence Processing and Delivery

Catalog-driven deterministic, semantic and LLM strategies remain selective. Semantic embedding → top-K retrieval → reranking is retained. The catalog models EXACT_PHRASE, REGEX, FUZZY, NER, SEMANTIC, LLM and CLASSIFIER metadata; that does not approve every family as a runtime component. Classifier execution remains deferred and no mandatory entity-extraction stage is added.

Shared resolution retains threshold-based acceptance as the existing boundary. Method-specific numeric semantics, evidence sufficiency, combination, partial completion, conflicts and finality remain open. Raw score is not automatically a probability. Multi-label means several accepted signals for one utterance; combining evidence for one signal and deriving a composite business signal are different concerns.

The catalog's action mappings describe signal-to-action metadata. Delivery/authorization/version retrieval remain open; mapping enabled state alone is not permission to perform an action. Workbench evidence and latency are established roles. No new API endpoint, acceptance formula or consumer is invented.

## 13. Component Interface and Contract Matrix

**Evidence classification:** no runtime interface is verified Implemented. The supplied specification documents detection fields and a partial local catalog demo; it does not establish enterprise approval of every schema. Confirmed target responsibilities and the mandatory Redis/SafeChain requirements are distinct from proposed deployment/protocol choices. Missing details are **TBD — Detailed Design Decision Required**.

All component inputs/outputs, dependencies and mechanisms below refer to §8's stable edges. §7 assigns state ownership; §17 supplies per-component security, failure/recovery, telemetry and readiness gaps. Together these cover the developer contract for each V4 component without creating separate competing specifications.

| Component / ID | Input contract | Output contract | Mechanism / upstream and downstream dependencies | Contract status |
|---|---|---|---|---|
| Google Cloud / Lumi boundary (`gcp`) | Approved enterprise service requirements | Available platform capabilities | Platform dependency; encloses GKE and candidate managed services | Target responsibility; detailed binding TBD |
| GKE application runtime (`gke`) | Deployable application components, when implemented | Running workloads and platform telemetry | Runtime boundary; owns no business interface by itself | Target responsibility; detailed binding TBD |
| Genesys Cloud (`genesys`) | Active call stream and authorized subscription | Audio/transcript source updates; actual contract TBD | External source; edge-1 to audio acquisition; text route not added to V4 | Target responsibility; detailed binding TBD |
| Transcript emulator (`test`) | Synthetic transcript fixtures | WebSocket transcript updates | edge-4 to ingress; same selected downstream processing path | Target responsibility; detailed binding TBD |
| Provider integration (`provider`) | Provider contract and access configuration | Source integration behavior | V4 support box has no explicit execution connector; boundary with bridge/ingress TBD | Target responsibility; detailed binding TBD |
| Audio acquisition (`bridge`) | Genesys audio; codec/frame format TBD | Transcript updates from STT interaction | edge-1 input; edge-2 STT dependency; edge-3 ingress output | Target responsibility; detailed binding TBD |
| Speech-to-Text (`stt`) | Approved audio stream | Partial/final recognition results; source contract TBD | edge-2 bidirectional dependency; gRPC/TLS shown as proposal | Target responsibility; detailed binding TBD |
| Transcript ingress (`ingress`) | Source/emulator updates | Identifiable processing entries | edges-3/4 input; edge-5 handoff; Redis required, original label conflicts | Target responsibility; detailed binding TBD |
| Redis Streams (`queue`) | Ingress processing entries | Consumer-group delivery under required Redis contract | edges-5/6; publish entries and consumer-group delivery; detailed transport binding open | Target responsibility; detailed binding TBD |
| Ingestion worker pool (`worker`) | Stream deliveries | Normalized windows / detection requests | edge-6 input; edge-7 coordination; edge-8 context update | Target responsibility; detailed binding TBD |
| Memorystore for Redis (`state`) | Worker context updates | Same-call context for coordination | edge-8 update; edge-9 context read; managed product proposed | Target responsibility; detailed binding TBD |
| Signal Management UI / API (`management`) | Curated definitions, patterns, examples and detector metadata | Published catalog snapshot and configuration; action mappings | edge-18 coordination; edge-19 proposed persistence; action delivery binding TBD | Documented demo model; runtime binding TBD |
| Cloud SQL · PostgreSQL (`sql`) | Catalog writes, vector queries, proposed result writes | Snapshot/example/candidate/result data | edges-17/19/22; PostgreSQL/vector direction; Cloud SQL hosting proposed | Target responsibility; detailed binding TBD |
| Detector coordination (`coord`) | Detection request, context, catalog snapshot | Scoped method requests | edges-7/9/18 inputs; edges-10/11/12 methods; schedule open | Target responsibility; detailed binding TBD |
| Deterministic detection (`rules`) | Selected request and rule configuration | Method evidence | edge-10 input; edge-13 resolver; internal protocol TBD | Target responsibility; detailed binding TBD |
| Semantic detection (`semantic`) | Selected input and compatible examples/index | Reranked method evidence | edge-11 input; edge-17 retrieval; edge-14 resolver | Target responsibility; detailed binding TBD |
| LLM detection adapter (`llm`) | Selected request, requirement, permitted context | Validated LLM evidence | edge-12 input; edge-15 resolver; edge-16 requires SafeChain clarification | Target responsibility; detailed binding TBD |
| SafeChain Integration (`model`) | SafeChain-mediated request under contract TBD | Response through SafeChain to caller | edge-16 secure LLM invocation; SafeChain API / protocol open | Target responsibility; detailed binding TBD |
| Shared Signal Resolution (`resolver`) | Method evidence and completion/configuration references | Accepted detections | edges-13/14/15 in; edge-20 publication; edge-23 selective later work | Target responsibility; detailed binding TBD |
| Signal publication API (`publisher`) | Accepted multi-label envelope | Consumer delivery and proposed persisted result | edge-20 input; edge-21 workbench; edge-22 proposed SQL | Target responsibility; detailed binding TBD |
| Signal workbench (`workbench`) | Authorized accepted detections | User-visible signal review | edge-21; SSE/WebSocket over HTTPS remains proposal | Target responsibility; detailed binding TBD |
| Contextual generation / activation (`later`) | Accepted signal and authorized action/context configuration | Downstream activation output | edge-23 input; edge-24 consumers; any LLM invocation must use SafeChain | Target responsibility; detailed binding TBD |
| Downstream consumers (`consumers`) | Authorized output/action request | Consumer outcome or acknowledgement, contract TBD | edge-24; delivery contract open | Target responsibility; detailed binding TBD |
| Cloud Observability (`telemetry`) | Approved runtime operational signals | Correlated operational evidence | edge-25 aggregate telemetry; logging/monitoring/trace proposed | Target responsibility; detailed binding TBD |
| Identity, secrets & network controls (`controls`) | Identity/access/config requirements | Approved auth, secrets and connectivity controls | Cross-cutting; no new gateway/service inferred | Target responsibility; detailed binding TBD |
| Enterprise governance (`governance`) | Data/model/operating requirements | Approved governance decisions and review requirements | Cross-cutting ownership; no automatic runtime workflow implied | Target responsibility; detailed binding TBD |

### Supplied detection schemas and versioning

The supplied Signal Catalog Technical Specification v1.0 (2026-10-16) is the source of these fields. Its executable catalog.json/server.py/index.html/workbook were not available. Missing detailed schemas have not been reconstructed from guesses.

### Detection input

| Field | Type | Required | Constraint |
|---|---|---|---|
| request_id | STRING | Yes | Nonempty unique detection request identity |
| session_id | STRING | Yes | Nonempty; partition context by session |
| utterance_id | STRING | Yes | Source utterance identity, unique within session |
| sequence_number | INTEGER | Yes | Within-call order, nonnegative |
| speaker | ENUM | Yes | AGENT / CUSTOMER / UNKNOWN |
| text | STRING | Yes | Final transcript text; nonempty after normalization |
| event_timestamp | TIMESTAMP | Yes | UTC ISO-8601 source event time |
| is_final | BOOLEAN | Yes | False handled by buffering policy, details unspecified |
| context | JSON_ARRAY | No | Prior speaker-tagged utterances; same session only |
| catalog_version | STRING | Yes | Immutable published snapshot identifier |

An utterance-oriented contract does not yet specify multi-utterance window identity, corrections or prior-signal state. Do not append fields or reinterpret sequence_number without agreement.

### Accepted output

| Field | Type | Required | Constraint |
|---|---|---|---|
| request_id, session_id, utterance_id | STRING each | Yes | Same as input |
| catalog_version | STRING | Yes | Snapshot used, consistent in response |
| status | ENUM | Yes | SUCCESS / ERROR; do not mask failures |
| detections | JSON_ARRAY | Yes | Accepted signal objects; multi-label |
| detections[].signal_id | STRING | Yes | Exists in catalog |
| detections[].domain_id, theme_id | STRING each | Yes | Catalog-derived |
| detections[].detection_type | STRING | Yes | Registered detector |
| detections[].score | FLOAT | No | Raw score, may be non-probabilistic |
| detections[].score_type | STRING | Yes | Meaning such as RULE_MATCH / COSINE |
| detections[].evidence | JSON_OBJECT | Yes | Minimize sensitive data; detailed per-method schema missing |
| detections[].latency_ms | INTEGER | Yes | Nonnegative inference latency |
| detections[].signal_version | INTEGER | Yes | Positive version integer |

No additional status enum, partial-error shape, confidence conversion or correction format is invented. Example evidence matched_text/matched_utterance_id is not a complete universal evidence schema. The singular detection_type requires alignment with combined-method evidence.

### Catalog and compatibility

Current catalog taxonomy is **Domain → Theme → Signal**, scoped to `SALES_COMPLIANCE`. A domain has many themes; a theme has many signals; a signal has many patterns, examples, detector records, action mappings and source-audit records. Local catalog.json arrays are domains, themes, signals, patterns, examples, detectors, actions and sources. These are entities, not separate services or an approved production storage choice.

The specification requires immutable IDs, catalog snapshot versioning, signal-version increments when meaning changes, detector metadata version alignment and release notes. Preserve category as the theme-identifier alias until consumers migrate to theme_id. Prefer additive compatible schema changes. Compatibility enforcement and migration ownership require design.

Recommended catalog validation includes reference/uniqueness checks, required fields, current-domain enforcement, numeric type checks and per-detector config_json validation. Full detector schemas are not supplied. Suggested lifecycle DRAFT_REVIEW → APPROVED → ACTIVE → DEPRECATED does not establish an implemented approval workflow.

### Data ownership

| Data | Authority / storage status | Required design |
|---|---|---|
| Source transcript/revision | Provider authority and canonical revision contract open | Identity, revision, source sequence and retention |
| Redis entries / pending delivery | Processing transport state, not catalog/evidence authority | Persistence, retention, retries and checkpoints |
| Bounded context/windows | Derived same-session working state | Ownership, consistency, expiry, recovery |
| Catalog | Business/catalog ownership TBD; demo JSON only reported | Published snapshot source, approval, rollback |
| Examples / vectors | Curated examples plus derived index; PostgreSQL/vector direction retained | Version lineage, rebuild/delete and hosting |
| Decisions / accepted history | Source of truth and writer TBD; SQL mapping proposed | Evidence retention, dedup, write/publish consistency |
| Logs/traces | Operational evidence, not substitute for business history | Redaction, access, retention and sampling |


## 14. Security and Governance

SafeChain is mandatory for LLM invocation. Its specific internal controls are not invented. Lumi and enterprise owners must confirm source permissions, approved services, project/network connectivity, workload identities, secrets/keys, model access, data classification, retention/deletion and audit responsibility.

Proposed platform-owned controls include organization/project/network foundations, cluster baselines and approved identity/secret services. Application-owned concerns include scoped access, call isolation, payload validation, permitted context, evidence handling and failure visibility. Inheritance is not proven by the V4 boxes. Regulatory catalog references are metadata requiring SME validation, not legal conclusions.

Golden datasets, false-positive/negative analysis, human review and prompt/model/index/catalog provenance remain evaluation requirements. No automatic retraining or new governance runtime is introduced. Dead-letter records and logs require permitted minimal data; raw transcript logging is not assumed safe.

## 15. Reliability and Recovery

Redis delivery must support consumer groups, acknowledgement after success/durable handoff, pending recovery, retry/dead-letter, idempotency, ordering considerations, retention/trimming, replay and consumer restart. Actual names, commands/version compatibility, budgets and ownership mechanisms remain TBD.

Define the commit boundary across context updates, detector scheduling, accepted-result persistence, publication and acknowledgement. Recovery can repeat work; protect effects as well as messages. Retained Redis entries are not automatically the business system of record. Approved persistence/failover is required before claiming durable handoff.

A slow LLM must not cause unlimited queued work. Completion, timeout, late evidence and SafeChain failures require explicit semantics. No direct-model bypass is proposed. Missing context is not empty context; failed evaluation is not a negative business finding. Freshness for display, context reconstruction and evidence retention are separate policies.

No exactly-once, zero-latency or generally acceptable silent loss guarantee is approved. Test failures around each commit/ack boundary and prevent concurrent ownership after recovery. Prior-signal visibility remains unassigned rather than silently adding a writeback connection.

## 16. Observability and Operational Readiness

Measure source/transcription delay separately from queue/window wait, method execution, resolution, publication and visible delivery. Use P50/P95/P99 under agreed workload and failure conditions; no numerical SLO is inferred from examples. Track Redis lag/pending age, retry/dead-letter rates, memory/capacity, concurrent sessions, state errors, detector completion, evidence quality and resource/model cost.

Propagate request/session/utterance and catalog/signal identifiers; model/prompt/index and trace bindings remain TBD. SafeChain-specific fields must come from its actual contract. Redact sensitive content and assign alert ownership. Logging/Monitoring/Trace in V4 are proposed tooling, not demonstrated instrumentation.

The architecture is ready for contract review, not operational approval. Source evidence, Lumi controls, SafeChain integration, recovery guarantees, quality and capacity results are still required.

## 17. Principal Architect Component Review

The following component-by-component checks cover responsibility, interaction, reliability, security, scaling and observability. **Readiness for every runtime component: detailed design can start; implementation acceptance cannot be claimed.** Named owners are TBD. Absence of documentation is not asserted as a defect in unseen implementation.

| Component | Reliability / error and retry responsibility | Security / governance | Performance and observability | Developer readiness gap |
|---|---|---|---|---|
| Google Cloud / Lumi boundary (`gcp`) | Availability and inherited recovery guarantees must be supplied | Project, network, identity and key controls require Lumi confirmation | Service availability, quotas and cost; limits TBD | Service approvals and control inheritance unverified |
| GKE application runtime (`gke`) | Workload shutdown/restart and failure-isolation contracts missing | Workload identity and network enforcement require approval | Workload saturation, restart and resource consumption; limits TBD | Boxes are not approved independent Deployments |
| Genesys Cloud (`genesys`) | Disconnect/reconnect, gaps and source ordering unverified | Source permissions and permitted capture must be confirmed | Source delay, gaps and reconnects; limits TBD | Selected topic/payload and live audio availability not evidenced |
| Transcript emulator (`test`) | Specify reproducible disconnect, revision and overload cases | Synthetic/redacted inputs; no production secrets | Fixture sequence, call count and emitted/received counts; limits TBD | No emulator code supplied |
| Provider integration (`provider`) | Reconnect ownership must not overlap with ingress/bridge | Do not infer auth scheme from box label | Authentication failures and reconnect outcomes; limits TBD | Responsibility overlaps acquisition and ingress unless assigned |
| Audio acquisition (`bridge`) | Define continuity, buffering and recovery after STT disconnect | Approved audio capture and STT data handling | Audio receipt-to-transcript delay and dropped frames; limits TBD | Audio and STT ownership unclear |
| Speech-to-Text (`stt`) | Specify timeout, reconnect and correction behavior | Approved audio service and permitted processing location | Recognition delay, quality and service errors; limits TBD | Service/protocol/version not confirmed |
| Transcript ingress (`ingress`) | Publish failure, backpressure and stable retry identity required | Validate payload and source authorization; no invented fields | Ingress delay, invalid updates and publish failures; limits TBD | Transport envelope and metadata mapping missing |
| Redis Streams (`queue`) | Ack after success/durable handoff; pending recovery, retry, DLQ, replay and idempotency required | Approved Redis access/hosting and restricted payload retention | Lag, pending age, retries, DLQ, capacity and availability; limits TBD | Redis hosting, ordering and recovery contract unverified |
| Ingestion worker pool (`worker`) | Ownership, revisions, duplicate effects, ack boundary and restart recovery TBD | Strict same-session isolation and minimum retained text | Window wait, throughput, backlog and state failures; limits TBD | Concurrency and utterance/window mapping are incomplete |
| Memorystore for Redis (`state`) | Expiry, eviction, reconstruction and missing-state behavior TBD | Session-scoped access and sensitive-text retention | Read/write latency, misses, eviction and recovery; limits TBD | Store choice and history consistency are not settled |
| Signal Management UI / API (`management`) | Reject invalid config as required; rollback/pinning not defined | Authoring/approval access, source audit and provenance | Validation failures, snapshot activation and version mismatches; limits TBD | Demo validates arrays only; runtime version acquisition absent |
| Cloud SQL · PostgreSQL (`sql`) | Backup, restore, index rebuild and publish/write consistency TBD | Per-category access, retention and deletion controls | Query/index latency, saturation and failed writes; limits TBD | One diagram store does not establish shared schema or authority |
| Detector coordination (`coord`) | Deadlines, partial completion, cancellation and fallback TBD | Supply only allowed same-session context | Selected methods, completion, timeout and in-flight work; limits TBD | Call metadata missing from visible input schema; combined execution undefined |
| Deterministic detection (`rules`) | Invalid regex/config and failed evaluation differ from no match | Safe config validation and evidence minimization | Evaluation duration, rule errors and outcome rates; limits TBD | Per-family schema and evidence requirements incomplete |
| Semantic detection (`semantic`) | No candidates distinct from retrieval/inference failure; deadline TBD | Permitted input and retrieved evidence; LLM-backed dependencies must use SafeChain if selected | Embedding/retrieval/reranking latency and quality; limits TBD | Threshold/index compatibility and hosting undecided |
| LLM detection adapter (`llm`) | SafeChain timeout/error/output contract TBD; no direct-provider bypass fallback | All LLM inference must use SafeChain; actual auth/data controls not supplied | Correlation, latency, timeout and invalid-output counts without sensitive payload leakage; limits TBD | SafeChain API contract and runtime implementation absent |
| SafeChain Integration (`model`) | Quota/timeout/error behavior must be negotiated through SafeChain | No direct application-to-model permission inferred | Permitted endpoint latency/availability and usage metrics; limits TBD | SafeChain represented; integration contract and model approval unverified |
| Shared Signal Resolution (`resolver`) | Conflicts, late evidence, abstention and partial failure TBD | Evidence integrity and decision provenance | Acceptance/rejection, latency and score distributions by method; limits TBD | Threshold scope, score comparability and combined evidence unresolved |
| Signal publication API (`publisher`) | Slow consumer, retry, duplicate delivery and write/publish consistency TBD | Authorized evidence disclosure; consumer access required | Publication lag, failures and duplicates; limits TBD | Protocol alternatives are labels, not approved APIs |
| Signal workbench (`workbench`) | Reconnect, stale views and corrected decisions TBD | Role-appropriate evidence access; no raw transcript exposure by default | Visible latency, usability and display errors; limits TBD | UI hosting/access and feedback contract absent |
| Contextual generation / activation (`later`) | Retries must not repeat side effects; independent failure policy TBD | Action authorization separate from signal acceptance; SafeChain required if LLM used | Follow-on latency, failures and authorized action outcomes; limits TBD | Trigger, action mapping retrieval and LLM use not defined |
| Downstream consumers (`consumers`) | Retry, replay and correction behavior require agreement | Stable-ID access policy and action permission | Delivery/outcome correlation and failures; limits TBD | Consumer identity and guarantees unknown |
| Cloud Observability (`telemetry`) | Collection failure/degradation policy; do not infer business durability | Redact/minimize sensitive data; audit access controls | Lag, quality, P50/P95/P99, failures, capacity and cost; limits TBD | Instrumentation, alert thresholds and owners unverified |
| Identity, secrets & network controls (`controls`) | Rotation, access failure and incident ownership TBD | WIF/IAM/Secret Manager/network labels are proposals; inherited controls unverified | Access denial, secret/control events and audit correlation; limits TBD | Responsibility split and cross-project paths unapproved |
| Enterprise governance (`governance`) | Escalation and exception handling TBD | Data classification, permitted inference, retention/deletion and audit | Quality/review coverage and governance exceptions; limits TBD | Owners and policies not established |

## 18. Recommended Component Improvements

These are recommendations, not applied runtime changes. Critical means correctness/security/data integrity review gate, not a verified production incident. High means important interface/reliability readiness gap. Medium means operational/scaling/usability improvement. Low would denote nonessential refinement. Existing design refers to the updated V4 representation; runtime changes remain recommendations only.

| Component | Existing Design | Identified Gap | Recommended Improvement | Priority | Implementation Impact |
|---|---|---|---|---|---|
| Google Cloud / Lumi boundary (`gcp`) | Define target platform scope | Service approvals and control inheritance unverified | Obtain Lumi capability and operating-responsibility inventory | High | Interface contract clarification; recommendation only |
| GKE application runtime (`gke`) | Host target application workloads | Boxes are not approved independent Deployments | Define workload grouping and scaling ownership without changing component topology | High | Interface contract clarification; recommendation only |
| Genesys Cloud (`genesys`) | Provide live interaction source | Selected topic/payload and live audio availability not evidenced | Capture approved payload samples and define identity/finality contract | High | Interface contract clarification; recommendation only |
| Transcript emulator (`test`) | Exercise concurrent calls as a separate test source | No emulator code supplied | Agree fixtures matching actual provider envelope and isolation cases | High | Interface contract clarification; recommendation only |
| Provider integration (`provider`) | Describe source authentication, format and reconnect responsibilities | Responsibility overlaps acquisition and ingress unless assigned | Assign source-session versus transcript-session responsibility in a contract | High | Documentation-only; recommendation only |
| Audio acquisition (`bridge`) | Adapt permitted live audio for speech recognition | Audio and STT ownership unclear | Define audio format, session mapping and STT responsibility before adapter work | High | Interface contract clarification; recommendation only |
| Speech-to-Text (`stt`) | Produce transcript updates for proposed audio path | Service/protocol/version not confirmed | Agree recognition owner, finality and correction contract | High | Interface contract clarification; recommendation only |
| Transcript ingress (`ingress`) | Adapt and frame identifiable transcript updates | Transport envelope and metadata mapping missing | Separate source framing from worker detection windows; define Redis producer boundary | High | Interface contract clarification; recommendation only |
| Redis Streams (`queue`) | Authoritative real-time stream handoff | Redis hosting, ordering and recovery contract unverified | Agree Redis hosting, ordering, acknowledgement and recovery contracts; visual correction applied | Critical | Architectural change requiring approval; recommendation only |
| Ingestion worker pool (`worker`) | Prepare coherent per-session detection input | Concurrency and utterance/window mapping are incomplete | Agree per-call ownership and processing-to-handoff commit contract | High | Interface contract clarification; recommendation only |
| Memorystore for Redis (`state`) | Provide bounded same-call working context | Store choice and history consistency are not settled | Assign history writer/visibility and context loss behavior independently of stream delivery | Critical | Interface contract clarification; recommendation only |
| Signal Management UI / API (`management`) | Maintain versioned taxonomy and detection configuration | Demo validates arrays only; runtime version acquisition absent | Bind supplied Domain/Theme/Signal contracts to reviewed snapshot lifecycle | High | Interface contract clarification; recommendation only |
| Cloud SQL · PostgreSQL (`sql`) | Candidate catalog, vector and result storage | One diagram store does not establish shared schema or authority | Define source of truth per category before physical-store approval | High | Interface contract clarification; recommendation only |
| Detector coordination (`coord`) | Select applicable signals and configured methods | Call metadata missing from visible input schema; combined execution undefined | Agree applicability metadata binding and completion rules | High | Interface contract clarification; recommendation only |
| Deterministic detection (`rules`) | Evaluate configured rules/matching | Per-family schema and evidence requirements incomplete | Define detector contract and golden matching cases; do not invent numeric probability | High | Interface contract clarification; recommendation only |
| Semantic detection (`semantic`) | Embed, retrieve top-K and rerank | Threshold/index compatibility and hosting undecided | Version the semantic bundle and evaluate precision/recall and latency | High | Interface contract clarification; recommendation only |
| LLM detection adapter (`llm`) | Evaluate scoped requirement/context through mandatory SafeChain | SafeChain API contract and runtime implementation absent | Obtain actual SafeChain integration contract and verify mandatory routing; visual correction applied | Critical | Architectural change requiring approval; recommendation only |
| SafeChain Integration (`model`) | Mandatory enterprise integration for secure access to approved LLM models | SafeChain represented; integration contract and model approval unverified | Validate integration ownership, model access and failure behavior; no direct-provider bypass | Critical | Architectural change requiring approval; recommendation only |
| Shared Signal Resolution (`resolver`) | Accept method evidence under configured signal rules | Threshold scope, score comparability and combined evidence unresolved | Approve method-specific evidence/acceptance contract without changing shared boundary | Critical | Interface contract clarification; recommendation only |
| Signal publication API (`publisher`) | Deliver accepted signals | Protocol alternatives are labels, not approved APIs | Agree delivery/finality contract and persistence ordering | High | Interface contract clarification; recommendation only |
| Signal workbench (`workbench`) | Display actionable evidence and latency for review | UI hosting/access and feedback contract absent | Specify multi-label display, evidence provenance and review feedback | Medium | Interface contract clarification; recommendation only |
| Contextual generation / activation (`later`) | Provide selective later follow-on after acceptance | Trigger, action mapping retrieval and LLM use not defined | Define later contract without blocking core detection or bypassing SafeChain | High | Interface contract clarification; recommendation only |
| Downstream consumers (`consumers`) | Consume later intelligence/activation under agreed contracts | Consumer identity and guarantees unknown | Identify consumer owners and acceptance criteria | High | Interface contract clarification; recommendation only |
| Cloud Observability (`telemetry`) | Collect logs, metrics and traces | Instrumentation, alert thresholds and owners unverified | Define stage measurements and alert ownership with no arbitrary SLO | Medium | Configuration improvement; recommendation only |
| Identity, secrets & network controls (`controls`) | Provide agreed enterprise/application control boundary | Responsibility split and cross-project paths unapproved | Obtain security responsibility matrix and approved identities/paths | Critical | Interface contract clarification; recommendation only |
| Enterprise governance (`governance`) | Define access, retention, privacy and audit accountability | Owners and policies not established | Assign accountable owners and evidence gates before live-data processing | Critical | Documentation-only; recommendation only |

## 19. Architecture Decisions and Trade-offs

| Decision | Current disposition |
|---|---|
| Final reference | Original V4 source, PNG, SVG, graph and generator retained at original paths; no new architecture version |
| Ingress | Redis Streams mandatory; approved V4 correction applied (AR-01) |
| LLM security | SafeChain mandatory; approved V4 correction applied (AR-02) |
| Platform | Lumi/GCP and GKE target retained; service availability and inherited controls open |
| Source / context | Separate emulator, proposed audio/STT; bounded same-session context and worker-side windowing retained |
| Methods | Selective deterministic/semantic/LLM; top-K/reranking retained; classifier execution not added |
| Acceptance | Shared resolution retained; thresholds, completion and evidence semantics require detailed design |
| Catalog | Supplied Domain/Theme/Signal schema, current Sales Compliance domain, immutable snapshot identity and multi-label output |
| Persistence / activation | Hosting and authority open; later action execution does not become core mandatory detection |
| Repository | One root README, existing V4 folder, validation/provenance records; no alternate diagrams or meeting/source-photo content |

The approved visual corrections are applied. Their presence does not demonstrate runtime implementation, enterprise compliance or production readiness.

## 20. Open Design Decisions

| Decision | Required reviewers | Gate |
|---|---|---|
| Redis hosting, publication and consumer-group contracts (AR-01 visual correction completed) | Architect / messaging owner | Before implementation approval |
| SafeChain API, access and model approval (AR-02 visual correction completed) | Architect / AI platform / security | Before secure invocation implementation |
| Production approval distinct from final-reference status (AR-03 clarified) | Architecture owner | Before deployment |
| Provider source contract, STT ownership, finality/revisions | Integration / speech | Before live acquisition |
| Redis keys/envelope/groups, ownership, ack/retry/DLQ/replay/retention | Ingestion / data / SRE | Before reliable consumer implementation |
| Catalog-version acquisition/pinning and call metadata delivery | Catalog / ingestion / detection | Before reproducible applicability |
| Window-to-utterance and prior-signal context binding | Ingestion / data | Before dependent scenarios |
| Method scheduling/completion, evidence schema, calibration and finality | Detection / SME / ML | Before trusted acceptance |
| SafeChain API/SDK/auth/config/error/timeout contract and tests | AI platform / security | Before any LLM integration |
| Result authority, delivery guarantees, action mappings and permissions | API / data / downstream | Before consumer/activation integration |
| Lumi service support, security ownership and quality/capacity/cost criteria | Lumi / security / SME / SRE | Before production approval |

No approved endpoint names, stream keys, credential fields, model IDs, retry counts or timeouts are supplied. Use **TBD — Detailed Design Decision Required** rather than inventing defaults.

## 21. Developer Design Handoff Checklist

- [ ] Assign accountable component and producer/consumer owners.
- [x] Apply authorized AR-01/02 visual corrections; retain prior source in Git history. Runtime compliance is still unverified.
- [ ] Obtain provider samples and agree source identity, sequence and finality/revision semantics.
- [ ] Agree Redis envelope, delivery ownership, acknowledgement and recovery consistency.
- [ ] Bind the supplied input/output schemas to catalog versioning, metadata selection and windows.
- [ ] Obtain the actual SafeChain interface/configuration and ensure all LLM callers use it; no bypass path.
- [ ] Approve method execution, evidence, acceptance and failure semantics with SMEs.
- [ ] Assign history/result authority, retention and publication consistency.
- [ ] Test contracts: required/optional fields, invalid enums, version compatibility, same-session context, multi-label output and explicit errors.
- [ ] Test interleaved calls, revised utterances, worker restart, duplicates, SafeChain timeout/invalid output, state loss and consumer reconnect.
- [ ] Verify quality, latency, load, resource cost and permitted evidence access with documented acceptance criteria.

No executable scaffold, new service, framework migration or infrastructure change is part of this review. Component teams can use §7/8/13/17 as the design checklist, while recording unresolved bindings before coding.

## 22. Existing Setup and Validation Instructions

This is an architecture repository. No application launch command, Redis endpoint, SafeChain configuration, deployment manifest or application test suite exists in the inspected baseline. Do not invent setup commands for an application that is not present.

Run the read-only package checks with Python 3:

```sh
python3 -B architecture/tools/validate_package.py
```

The existing renderer at `architecture/gcp-gke-level-1/v4/build_v4.py` now reads the existing `graph-v4.json` and refreshes draw.io/SVG without reconstructing the architecture. The graph retains original IDs, grouping and endpoints. Rendering writes exports: use a temporary copy for reproduction checks. The high-resolution PNG is rendered from the SVG.

Updated PNG/SVG are provided. The PNG was visually inspected; SVG and editable draw.io XML were structurally checked. Native organization draw.io import remains untested. Validation retains original and current SHA-256 records, checks all 25 endpoint pairs against the prior revision, verifies the exact title and selected labels, checks the 16:9 canvas, and confirms README links and component coverage.

- [Original baseline and approved-correction manifest](architecture/review/v4-preservation.json)
- [Validation results](architecture/review/validation.json)
- [File scope and change audit](architecture/review/change-audit.json)

Superseded options diagrams and competing guide documents are omitted from this branch's current tree; their original commit remains in Git history. No branch/history rewrite or runtime deletion occurs. Existing V4 icon assets and `.gitignore` are preserved; obsolete vendor icons are no longer embedded in the diagram. Input JPEGs, manager reviews and meeting artifacts are not copied. The previous local consolidation checkout remains untouched.

Vendor icons are retained as existing assets from [Google Cloud icons](https://cloud.google.com/icons), subject to vendor/internal usage requirements. No additional license or enterprise compliance is asserted.

**Validation scope:** targeted diagram alignment is complete; implementation and production approval remain open. Redis, SafeChain, API, load and recovery execution tests are unavailable because runtime code/configuration is absent. No existing code bypass has been demonstrated. This branch contains the authoritative updated V4; it does not claim that the runtime is implemented or compliant.
