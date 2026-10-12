# VANTAGE Technical Level 1 — V3 presentation decisions

12 October 2026. Presentation enhancement of the existing GCP/GKE technical proposal, not a new solution design or deployment approval.

## Evidence reviewed

Reviewed the prior draw.io, generator, decision notes and validation file; architecture-model.json; component inventory; decision register; integration matrix; architecture README; principal-architect review and audio/queue review; and the supplied V3 brief and technical reference image. The workspace has no root README; the repository README was available in the existing publishing clone and was reviewed there. No approved internal design template, enterprise icon library, application implementation or verified infrastructure inventory was supplied.

## Visual changes

- Deep navy #002663, primary blue #006FCF, pale blue #EAF4FF, white application cards and subtle amber proposal borders follow the supplied design tokens. These are American Express-inspired colors, not a claim of official corporate template compliance. No American Express mark is used.
- Managed dependencies form an upper service row. The GKE runtime contains a left-to-right ingestion, detection and resolution path. Shared observability and controls form the lower row.
- Official Google-provided service SVGs are individually embedded, without recoloring or external URL dependencies. Neutral capability symbols are used for application workloads and the Genesys source; those symbols are not vendor logos.
- Numbered zone headings 1–3 denote presentation stages, not source-reference IDs. There are no visible A01/M02/Cxx reference labels.
- Purple identifies the separate emulator and its test-only connection. Solid blue retains documented processing; amber dashed retains proposed interfaces; dotted blue retains configuration/telemetry.
- Detailed uncertainties move into documentation; compact OPEN and PROPOSED qualifications remain visible. A dashed workload card indicates proposed packaging, not an unconfirmed functional requirement.

## Technical preservation

All 25 prior technical-view source/target connections are retained. No new runtime service or data interface is introduced. Governance is visually separated from the previous shared-controls paragraph; the underlying responsibilities are unchanged. Component source references remain hidden draw.io metadata.

Selective invocation, metadata applicability, bounded same-call context, semantic top-K plus reranking, and shared threshold-based Signal Resolution are unchanged. Raw detector scores are not assumed comparable calibrated probabilities. LLM detection does not bypass resolution. Later contextual generation/activation remains distinct from detection.

GCP/GKE are confirmed targets. Cloud Speech-to-Text, Pub/Sub, Memorystore, Cloud SQL hosting, Vertex AI, observability products, IAM/WIF, Secret Manager, private connectivity and workload/service splits retain their prior proposal status. No new FastAPI, Python runtime, OpenTelemetry, graph database, Graph RAG, image registry, API gateway or consumer product is selected through icon use.

PostgreSQL/pgvector is represented by the Cloud SQL hosting icon and explicit PostgreSQL label; Redis is represented by the Memorystore icon and explicit Redis label. No separate PostgreSQL or Redis brand asset is implied. Google Cloud is identified by its boundary title rather than a corporate logo. The reference's Salesforce, Appian, Tableau, Azure and other marks are not copied into VANTAGE.

For implementation mapping and rationale, see [the prior technical decision record](../technical-level-1-decisions.md). These recommendations were not reapproved by this visual refresh.

## Decisions still required

1. Genesys audio access/authentication, stream format, reconnect behavior and STT model/accuracy/latency evaluation.
2. Broker approval; per-call ordering, acknowledgement, duplicate/replay handling, backpressure and worker scaling semantics.
3. Context writer ownership, accepted-signal history updates, expiry, session serialization and recovery.
4. Embedding/reranker/LLM selection and hosting; method scheduling, timeout behavior, threshold calibration and result-combination/finality rules.
5. Catalog activation/versioning; existing PostgreSQL versus Cloud SQL; accepted-result persistence/publication consistency; full-call retention; consumer authentication and hosting.

BigQuery remains reference-only. LLM exact/semantic response caches are not silently added. Composite and sequence-signal semantics remain in the baseline backlog; no new execution placement is claimed. Provider-produced transcript coexistence remains open. Shared controls apply across the runtime and managed-service access; the lower-row placement is not a data-processing stage.

## Editing and delivery

Open `vantage-gcp-gke-technical-level-1-v3.drawio` in diagrams.net/draw.io. Icons are individually embedded image cells parented to their component; titles, descriptions, containers and connectors remain native editable elements. A component move carries its icon. Icons themselves retain their vendor SVG artwork.

The generator `build_v3.py` reuses the earlier View implementation while keeping all previous files unchanged. Run it from any directory with Python 3. The PNG is rendered separately from SVG. Only one Level 1 diagram is delivered. No GitHub push is part of this request.
