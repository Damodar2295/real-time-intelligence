# VANTAGE Intelligence — GCP/GKE Technical Level 1

**12 October 2026 · Implementation proposal for review**

## Scope and evidence

This single technical view maps the existing VANTAGE v1.2 behavior to the GCP/GKE target requested in the latest brief. It is a separate proposal; it does not replace the approved layered baseline. Sources reviewed: workspace architecture artifacts, the meeting decisions supplied in this conversation, the latest attached GCP/GKE brief, and its reference image. No application implementation or enterprise infrastructure standards were available to verify deployment or product approval.

The reference image supplies presentation context, not approval to import Salesforce, Appian, Tableau, RTF, Azure, OpenAI, or its other technology choices. No source JPEGs are included in this output. Diagram source-reference metadata is hidden, not displayed as component numbering.

**Confirmed** means target platform or agreed application behavior, not deployed infrastructure. **Proposed** means an implementation recommendation. **Open** means an unresolved contract, technology, owner, or parameter. GKE subdivisions are proposed workload boundaries, not a deployment topology or a requirement that every module be its own microservice.

## Preserved decisions

- GCP and GKE are the target cloud and runtime in the latest brief.
- The emulator is a separate test module/service, visually distinguished from the production source.
- Audio acquisition and speech-to-text are represented explicitly. Audio-native detection is not selected.
- Transcript ingestion is decoupled from parallel processing by a queue. Call/session identity scopes processing and context; one queue per call is not assumed.
- Workers perform normalization, session management, segmentation/windowing, and microbatch preparation. Ingress performs source adaptation and identity propagation before publication.
- Coordination selects applicable catalog signals and their configured detection methods; methods are not mandatory sequential stages.
- Deterministic, semantic with top-K retrieval and reranking, and LLM-based detection feed shared threshold-based Signal Resolution. Threshold values, score calibration, combination rules, and finality are unresolved.
- Conversation context is bounded and belongs to the same call. Prior signals are part of the intended context, but writer ownership, expiry, and recovery remain unresolved.
- Signal Management manages the catalog. The schema, activation, and embedding publication details remain under design.
- Evidence and latency are visible in the workbench. Follow-on contextual generation/activation is separate from detection.
- BigQuery remains a reference-design option. Exact and semantic LLM-response caches have not been added as approved components. The deferred trained classifier has not been reintroduced.

## Component mapping

All named managed cloud products below are **proposals**, except GKE itself as the requested target runtime.

| Component | Execution / responsibility | Input → output / interface | State and dependency | Security / scaling / reliability |
|---|---|---|---|---|
| Genesys Cloud | External enterprise call source | Live audio → audio acquisition adapter; contract open | Source call identity and metadata | Provider authentication, audio encoding, reconnect, and call lifecycle unresolved |
| Transcript emulator | Separate test service; hosting open | Test transcripts → ingress using WebSocket | Test transcripts and call IDs | Concurrent calls required; do not treat as production source |
| Audio acquisition adapter | Proposed GKE workload; obtain audio and maintain STT client session | Genesys audio → streaming gRPC/TLS STT request; recognition results → ingress | Active source/STT session | Provider credentials and stream limits; reconnect, buffering, and replay open |
| Cloud Speech-to-Text | Proposed managed streaming transcription | Audio stream ↔ recognition results via gRPC | Streaming session | Evaluate language, accuracy, interim/final behavior, latency and quota before selection |
| Transcript ingress | Proposed GKE workload; adapt source envelope and preserve call/session identity | Transcript events → Pub/Sub publish API/TLS | No durable local state selected | IAM publish rights; backpressure and publish failure behavior open |
| Pub/Sub | Proposed managed transcript queue | Publish → subscription → StreamingPull and acknowledgement | Retained pending messages; configuration open | Subscriber IAM; ordering key, redelivery, retries, dead-letter policy and retention require design |
| Ingestion workers | Proposed GKE worker replicas; normalization, sequencing, session windows, segmentation | Queue messages → microbatches to coordination; gRPC proposed | Bounded per-call context via Redis/TLS | Elastic concurrency; acknowledgement boundary, idempotency and same-call serialization unresolved |
| Memorystore for Redis | Proposed managed conversation-state service | Worker state updates; context reads for detection | Bounded utterances and prior signals | Private connectivity and access controls; TTL, ownership, failure/recovery and capacity unresolved |
| Detector coordination | Proposed GKE service boundary | Microbatch + call metadata + context + catalog → selected method inputs | Catalog/configuration access and context | Scheduling, deadlines, method fallback and concurrency limits unresolved |
| Deterministic engine | Proposed GKE module/service | Text and configuration → evidence/scores | Rules, regex, fuzzy and entity-check definitions | Rule versioning and execution limits; no separate entity extraction service assumed |
| Semantic engine | Proposed GKE workload | Text → embedding → SQL/TLS vector top-K → reranking → evidence/scores | PostgreSQL/pgvector examples and representations | Embedding/reranker model, hosting, dimensions and indexing open; not silently assigned to Vertex AI |
| LLM detection adapter | Proposed GKE workload | Candidate + requirement + context → HTTPS inference → evidence/scores | Model endpoint, prompt/configuration | Workload identity where supported, endpoint approval and data controls; timeout/quota/fallback open |
| Vertex AI endpoint | Proposed managed model integration; enterprise model gateway alternative | HTTPS inference request → response | Model/version approval open | Model access permissions, regional availability, data handling and capacity require approval |
| Shared Signal Resolution | Confirmed acceptance responsibility; GKE packaging proposed | Invoked-method evidence → accepted signal | Threshold configuration; method/version-specific interpretation unresolved | Do not compare raw scores as calibrated probabilities; duplicate/finalization policy open |
| Signal publication API | Proposed GKE workload | Accepted events → workbench using proposed SSE or WebSocket over HTTPS; SQL/TLS accepted-record write proposed | Result publication/persistence boundary | Consumer authentication, delivery guarantees, retries and write/publish consistency open |
| Signal Management UI/API | Confirmed capability; proposed GKE packaging | Catalog changes → configuration and SQL/TLS persistence | Definitions, taxonomy, examples and references | Authoring/approval roles, version activation and rollback open |
| Cloud SQL PostgreSQL + pgvector | Proposed managed hosting; existing approved PostgreSQL alternative | SQL/TLS catalog operations, vector search and accepted-record writes | Catalog/examples/results mapping proposed | DB identity/credentials, connection limits, backup/HA/retention open; full-call storage not selected |
| Real-time workbench | Confirmed consumer capability; hosting outside this boundary is illustrative | Accepted signals → evidence and latency display | UI/session state unresolved | User authentication and hosting decision open |
| Contextual generation / activation | Later capability; GKE placement proposed | Selected accepted signals → downstream actions/recommendations | Additional context/contracts unresolved | Consumer authorization and delivery behavior require separate design |
| Cloud Observability | Proposed Logging, Monitoring and Trace | Instrumented workloads → logs, metrics and traces | Telemetry retention/sampling open | Call/event correlation, stage P50/P95/P99; access and sensitive-data handling require policy |
| Shared cloud controls | Proposed WIF/IAM, Secret Manager and network controls | Workload identity and secret access; API/CSI integration choice open | IAM bindings, secrets and network configuration | Least privilege and private access where supported; governance remains an application/enterprise responsibility |

## Why these proposals

- **Pub/Sub** provides a managed queue/subscription boundary suitable for the requested worker decoupling. Call ID is proposed as an ordering key. Ordering requires configuration and has documented delivery constraints; it does not establish application idempotency, atomic microbatch execution, or safe concurrent state ownership. [Google Pub/Sub ordering documentation](https://docs.cloud.google.com/pubsub/docs/ordering)
- **Cloud Speech-to-Text** supports bidirectional streaming recognition through gRPC. The arrow denotes client invocation with returned results, not a one-way audio export. Selection depends on a real audio and latency evaluation. [Streaming transcription](https://docs.cloud.google.com/speech-to-text/docs/v1/transcribe-streaming-audio)
- **Cloud SQL with pgvector** is a proposed managed hosting option for the PostgreSQL/vector requirement. It does not imply migration approval for the existing instance or approval of the proposed catalog/result storage mapping. [Supported extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions)
- **Memorystore** is proposed for bounded state shared by elastic workers. Private connectivity between GKE and Redis must be configured; the diagram does not imply the service supplies conversation ownership automatically. [Connect from GKE](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-gke)
- **Vertex AI** is a proposed inference integration, with an approved enterprise model gateway as an alternative. No model, prompt, embedding endpoint, or reranker has been selected. [Vertex AI API reference](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rpc)
- **Workload Identity Federation for GKE** is proposed for workload access to cloud APIs using IAM. Secret Manager handles secrets that remain necessary; exact API versus CSI usage is open. [Workload identity documentation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity)
- **Cloud Observability** is proposed for workload/system telemetry; application-level stage traces still require instrumentation. [GKE observability](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/observability)

Artifact Registry was considered but omitted from this runtime view: an enterprise container supply-chain standard was not available. This omission is not a recommendation to deploy without an approved image registry and delivery process.

## Questions requiring decisions

1. **Audio contract and latency:** Which Genesys audio interface is available and authorized? What are its authentication, format, speaker/channel, reconnect, and interim/final transcript contracts? Which STT model meets accuracy and measured latency requirements?
2. **Queue and processing semantics:** Is Pub/Sub approved? What defines a message and microbatch? When is it acknowledged? How are duplicates, late/corrected transcripts, replays, call ordering and backpressure handled? What limits and metrics drive worker scaling?
3. **Conversation-state ownership:** Which component writes accepted signal history? How is one call serialized across workers? What context window/TTL, recovery behavior and call-end cleanup are required? Does “atomic microbatch” mean only state mutation or also output publication?
4. **Models and resolution:** Which embedding, reranker and LLM models/hosts are approved? How are method-specific thresholds calibrated? Are multi-method signals combined, and when is a result final? What happens on timeout or partial evidence?
5. **Persistence and access:** Can the existing PostgreSQL instance serve catalog/vector workloads, or is Cloud SQL approved? Who owns result persistence and publication consistency? Where are full utterances stored? What retention, user access, network and privacy requirements apply?

Additional decisions: authoritative signal schema and taxonomy; approved examples/requirements and product values; per-call metadata filters; entity extraction placement; composite and omission-signal timing; catalog version changes during active calls; workbench hosting/protocol; downstream activation contracts; exact versus semantic response-cache requirements; enterprise security review and service quotas.

## Latency and evaluation

Keep the earlier 100–150 ms internal deterministic-path target as an initial engineering target, not an end-to-end SLA. Measure transcription, queue wait, windowing, detection, resolution, publication and UI delivery separately, with P50/P95/P99. Reranking, model invocation, queueing and microbatch buffering need measured budgets; previous figures are not proof that this proposed implementation meets them.

Validate at least concurrent independent calls, paraphrase-based semantic detection, verbatim deterministic detection, and a prior-event-dependent scenario. Final scenario selection and expected results require business agreement.

## Artifact verification

- One native editable draw.io page with 31 vertices and 25 connectors; managed services are children of the GCP boundary, outside GKE.
- Text-fit, sibling overlap, containment and connector endpoint checks pass.
- SVG was rendered to a 3000 × 1810 PNG and visually inspected; no input image is embedded.
- Diagram labels identify proposals and open contracts. No visible source-reference numbering is used.
- Draw.io is uncompressed XML using native shapes/connectors and editable labels. The preview is generated from the same model, not a screenshot of the target organization's draw.io installation; native import in that environment remains untested.
- No infrastructure was provisioned, no service approval inferred, and no repository push performed. Only this Level 1 proposal and supporting files were generated.
