# Component and interface matrix — V4

Stable IDs are the existing V3 draw.io IDs, preserved in V4. Canonical Cxx/Rxx references relate them to the logical v1.2 source model; a technical-view component may combine several logical capabilities. IDs remain XML metadata and matrix references rather than crowding the presentation. They are inspectable in the editable file. This choice retains earlier requests to remove visible reference numbering.

Status describes architecture intent, not deployment. A PROPOSED workload label describes packaging, not a reversal of a confirmed capability. Technical controls absent from the logical model are traced to the earlier technical proposal, not manufactured logical IDs. Boundaries and explanatory panels are notation, not independently deployed services.

## Components

| Stable ID | Name | Diagram parent | Status | Responsibility / qualification | Source |
|---|---|---|---|---|---|
| gcp | GOOGLE CLOUD  |  Confirmed target platform | 1 | CONFIRMED target; deployment NOT VERIFIED | Target platform boundary | Prior GCP/GKE technical proposal / V4 representation |
| gke | GKE APPLICATION RUNTIME  |  Confirmed target; workload boundaries proposed | gcp | CONFIRMED target; deployment NOT VERIFIED | Target platform boundary | Prior GCP/GKE technical proposal / V4 representation |
| genesys | Genesys Cloud | 1 | CONFIRMED behavior; implementation OPEN | Live call source; Audio interface OPEN | C01 |
| test | Transcript emulator | 1 | CONFIRMED behavior; implementation OPEN | Separate TEST service; Concurrent call streams | C02 |
| provider | Provider integration | 1 | OPEN ownership / controls | Authentication • format • reconnect; Contracts OPEN | Prior GCP/GKE technical proposal / V4 representation |
| stt | Speech-to-Text | gcp | PROPOSED implementation | Streaming recognition; gRPC / TLS • PROPOSED | C72 |
| queue | Cloud Pub/Sub | gcp | PROPOSED implementation | Transcript topic + subscription; Call ordering semantics OPEN | C74 |
| state | Memorystore for Redis | gcp | PROPOSED implementation | Bounded same-call context; History writer / recovery OPEN | C47 |
| sql | Cloud SQL · PostgreSQL | gcp | PROPOSED implementation | pgvector • catalog • results; Hosting and storage PROPOSED | C61 |
| model | Vertex AI endpoint | gcp | PROPOSED implementation | LLM inference • PROPOSED; Enterprise gateway alternative | C60 |
| bridge | Audio acquisition | ingestion-zone | PROPOSED implementation | Genesys stream / STT client; Transcript event output | C71 |
| ingress | Transcript ingress | ingestion-zone | PROPOSED implementation | Source adaptation; Call / session identity | C57,C73 |
| worker | Ingestion worker pool | ingestion-zone | PROPOSED implementation | Normalize • sessions; Segmentation / microbatches | C08,C56 |
| coord | Detector coordination | detection-zone | PROPOSED implementation | Select applicable method(s); Scheduling / completion OPEN | C54,C59 |
| rules | Deterministic detection | detection-zone | PROPOSED implementation | Rules • regex • fuzzy; Entity checks | C39 |
| semantic | Semantic detection | detection-zone | PROPOSED implementation | Embed → top-K → rerank; Model / hosting OPEN | C18,C19,C36 |
| llm | LLM detection adapter | detection-zone | PROPOSED implementation | Candidate + requirement; Conversation context | C60 |
| resolver | Shared Signal Resolution | resolution-zone | CONFIRMED behavior; implementation OPEN | Threshold-based acceptance; Calibration / combination OPEN | C22 |
| publisher | Signal publication API | resolution-zone | PROPOSED implementation | Accepted signal events; Delivery + persistence proposed | C24,C40 |
| management | Signal Management UI / API | gke | PROPOSED implementation | Catalog • definitions • curated examples; Activation / versioning workflow OPEN | C53,C13,C52 |
| later | Contextual generation / activation | resolution-zone | PROPOSED implementation | LATER • selective follow-on | C27,C28 |
| workbench | Signal workbench | 1 | CONFIRMED behavior; implementation OPEN | Evidence + latency display; Hosting / access OPEN | C25 |
| consumers | Downstream consumers | 1 | PROPOSED implementation | LATER integration; Delivery contract OPEN | C29 |
| telemetry | Cloud Observability | gcp | PROPOSED implementation | Logging • Monitoring • Trace; Application instrumentation required | C44 |
| controls | Identity, secrets & network controls | gcp | PROPOSED implementation | Workload Identity / IAM • Secret Manager; Private connectivity and network policy | Prior GCP/GKE technical proposal / V4 representation |
| governance | ENTERPRISE GOVERNANCE | gcp | OPEN ownership / controls | Access • retention • privacy • audit; Ownership and policies OPEN | Prior GCP/GKE technical proposal / V4 representation |

## Interfaces

All 25 stable interface IDs and source/target pairs are preserved. A solid line asserts logical flow, not a confirmed synchronous transport. A line to a dependency denotes invocation/data access, not a complete request-response protocol. Return data are described below. Data classification/access rules apply to every crossing and remain to be approved.

| Interface ID | Source → target | Data / responsibility | Protocol status | Relationship status | Source / qualification |
|---|---|---|---|---|---|
| edge-1 | genesys → bridge | Live audio; provider stream contract OPEN | OPEN / not specified | PROPOSED interface | R94 |
| edge-2 | bridge → stt | Audio request and recognition results; bidirectional STT client dependency | PROPOSED | PROPOSED interface | R95 |
| edge-3 | bridge → ingress | Transcripts returned through adapter; R96 is the logical STT-to-ingress path, not a newly confirmed adapter API | OPEN / not specified | CONFIRMED logical relationship | R96 |
| edge-4 | test → ingress | Simulated call transcripts | DOCUMENTED WebSocket | CONFIRMED logical relationship | R65 |
| edge-5 | ingress → queue | Call-identified transcript event publication | PROPOSED | PROPOSED interface | R98 |
| edge-6 | queue → worker | Subscription consumption and acknowledgement; delivery semantics OPEN | PROPOSED | PROPOSED interface | R99 |
| edge-7 | worker → coord | Microbatch + metadata; gRPC is a retained proposal, scheduling OPEN | PROPOSED | CONFIRMED logical relationship | R92 |
| edge-8 | worker → state | Recent utterance/session state update; accepted-signal writer not assigned | PROPOSED | PROPOSED interface | R68 |
| edge-9 | state → coord | Same-call context available to coordination; Redis client/reader packaging OPEN | OPEN / not specified | PROPOSED interface | R69 |
| edge-10 | coord → rules | Configured deterministic input; applicability required | OPEN / not specified | CONFIRMED logical relationship | R71 |
| edge-11 | coord → semantic | Configured semantic input, including utterance paired with retrieved candidates | OPEN / not specified | CONFIRMED logical relationship | R72 |
| edge-12 | coord → llm | Configured LLM input; independence/fallback/ordering OPEN | OPEN / not specified | CONFIRMED logical relationship | R73 |
| edge-13 | rules → resolver | Deterministic evidence to common resolution | OPEN / not specified | CONFIRMED logical relationship | R50,R30 |
| edge-14 | semantic → resolver | Reranked semantic evidence to common resolution | OPEN / not specified | CONFIRMED logical relationship | R47 |
| edge-15 | llm → resolver | LLM evidence to common resolution | OPEN / not specified | CONFIRMED logical relationship | R93 |
| edge-16 | llm → model | Model request and response; prior technical proposal, not R73 orchestration itself | PROPOSED | PROPOSED interface | C60 |
| edge-17 | semantic → sql | Vector query and retrieved examples/candidates | PROPOSED | PROPOSED interface | R79 |
| edge-18 | management → coord | Catalog applicability and detection configuration; fetch/push contract OPEN | OPEN / not specified | CONFIRMED logical relationship | R62,R70 |
| edge-19 | management → sql | Catalog/example persistence; prior technical proposal, not approved storage ownership | PROPOSED | PROPOSED interface | C13,C52,C53 |
| edge-20 | resolver → publisher | Accepted signal events; finality/duplicate policy OPEN | OPEN / not specified | CONFIRMED logical relationship | R32 |
| edge-21 | publisher → workbench | Workbench display delivery; R33 logical consumer, R51 publication alternatives; historical R40 was an unrelated reference and is removed | PROPOSED | PROPOSED interface | R33,R51 |
| edge-22 | publisher → sql | Accepted-result persistence; R34 optional-store behavior maps to proposed SQL destination | PROPOSED | PROPOSED interface | R34 |
| edge-23 | resolver → later | Selective follow-on after acceptance; not mandatory detector stage | OPEN / not specified | PROPOSED interface | R35 |
| edge-24 | later → consumers | Later activation delivery; protocol and consumer contract OPEN | OPEN / not specified | PROPOSED interface | R36,R37 |
| edge-25 | gke → telemetry | Aggregate runtime telemetry; not a business event or service hop | OPEN / not specified | CONFIRMED telemetry requirement; product PROPOSED | C44 |

## Runtime, state and failure ownership

All deployment owners are unassigned. Stakeholder roles below are requested decision owners. No resource requests/limits, replicas or separate Deployment-per-card assumption is introduced.

| Workload / group | Candidate runtime type | State / truth requirement | Scaling and failure isolation | Resources / required owner |
|---|---|---|---|---|
| bridge | Long-lived GKE stream adapter/client proposed | Active audio/STT sessions; reconnect state OPEN | Concurrent streams and provider/STT limits; stream restart and backpressure isolation OPEN | Audio/network and STT quota profile unknown; integration lead |
| ingress | GKE listener/publisher proposed | Session identity mapping; durable event handoff OPEN | Publish pressure and source connections; acknowledgement/retry semantics OPEN | Connection/event profile unknown; ingestion lead |
| worker | GKE consumer pool proposed | Call-scoped normalization/window state; cache dependency | Scale across calls; same-call ownership, redelivery, shutdown and recovery OPEN | CPU/memory per active call unmeasured; ingestion + platform |
| coord | GKE coordination module/service proposed | Configuration versions/context snapshots OPEN | Bound detector fan-out and late completion; no mandatory parallel schedule | Concurrency/deadline requirements unknown; detection lead |
| rules | GKE module/service proposed | Rule definitions, evidence; hot-path state ownership OPEN | Rule workload isolation/limits and determinism under revisions OPEN | CPU profile unknown; detection owner |
| semantic | GKE workload proposed | Embedding/index versions and top-K/reranker context | Vector and inference capacity; timeout/degradation OPEN | CPU/GPU need not selected; ML + data owners |
| llm | GKE inference client proposed | Prompt/model/configuration version; request context | Model endpoint quota, timeout/retry and partial evidence OPEN | Client concurrency/token profile unknown; AI platform + detector owner |
| resolver | GKE module/service packaging proposed | Acceptance evidence; decision/dedup state OPEN | Finalization and ordering across arriving evidence OPEN | Workload profile unknown; signal owner |
| publisher | GKE API/publisher proposed | Accepted result persistence mapping; consistency boundary OPEN | Slow clients, reconnect, write failure and replay isolation OPEN | Fan-out/connection profile unknown; API + data owners |
| management | GKE UI/API packaging proposed | Authoritative catalog and activation owner OPEN | Separate authoring/activation concerns from detection performance; isolation boundary OPEN | Usage and index-build requirements unknown; catalog owner |
| later | Later generation/activation; GKE placement proposed | Additional context and delivery records OPEN | Should not be assumed a core detection dependency; failure policy OPEN | Not sized; product/downstream owners |
| workbench / test | Hosting OPEN; separate emulator confirmed | Display sessions / controlled input fixtures | Workbench fan-out and simulator concurrency require validation | No production capacity inferred; UI/test owners |

## Boundary and interface questions

External Genesys and consumer boxes denote external/unknown ownership, not approved trusted networks. The GCP boundary is platform scope; GKE is runtime scope. Managed products are outside GKE. Shared controls apply across workloads and cloud-service access, without selecting a concrete ingress/egress gateway. Enterprise versus application control inheritance is listed in the decision register.

No missing logical-model node is automatically added: historical connector/demultiplexer/partition and context variants are represented through current ingestion responsibilities where documented; deferred classifiers, challenged entity-first enrichment, reference-only BigQuery, and unresolved composite execution are retained in source records rather than promoted to current technical runtime boxes. All significant components in the latest V3 technical view are preserved.
