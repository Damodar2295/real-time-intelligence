# Architecture changelog

## v0.1 — 2026-10-08

Initial workspace baseline: no previous inventory or draw.io draft existed.

- Added 44 source-indexed component/capability/data records and 54 directed relationship records with separate statuses.
- Recorded the four concerns named in A01; retained the distinction between enterprise concern names and POC groups.
- Captured the explicit mini-based POC action without assuming API availability, performance, few-shot wiring or production approval.
- Retained the simple deterministic path and flagged entity enrichment placement, detector orchestration and classifier sequencing as unresolved.
- Recorded catalog reuse, entity cache/enrichment, reranking, training storage and SSE/WebSocket publication as proposals or conflicting flows.
- Preserved POC latency targets with their original measurement boundaries and qualifications.
- Created one editable draw.io draft and a layout preview; detailed experimental flow stays in the registers until decisions justify baseline changes.
- Source instructions were treated as reference content; only the user's chat request authorized this work. No unrequested architecture from other workspace images was imported.

See validation-report.md for checks and limitations. Future entries should append source-backed deltas and preserve stable IDs.

## v0.2 — 2026-10-08 — documentation/model only

- Added M02 architecture extract and U02 diagram hold; preserved the original v0.1 structured model snapshot.
- Recorded deterministic + semantic implementation as current meeting direction; promoted top-K and reranker role (C35/C36, R45/R46) to CONFIRMED source-backed POC direction. Exact BGE selection, performance and R47 output wiring remain unresolved.
- Marked C20/C38 and classifier relationships as deferred in current scope, without deleting historical evidence or silently cancelling the earlier C42 mini-based action.
- Retained entity-appending disagreement and separated it from the new prior-signal/sequence requirement.
- Added C45/C46 as scenario-level capabilities and C47 as proposed memory caching with ambiguous contents; no service, cache product or layer designed.
- Added R55 utterance input to reranking, R56 pivot occurrence retained for its conversation, and R57 prior occurrence contributing to later detection as logical dependencies only.
- Recorded the three/four real-case validation request and outreach reference-review request; no outreach integration added.
- Updated requirements, questions, decisions, traceability and README. Counts: 47 inventory records, 57 relationships.
- Draw.io, SVG and PNG previews unchanged; their v0.1 content does not incorporate M02 and must not be treated as the final design.

## v0.3 — 2026-10-08 — documentation/model only

- Added M03 architecture extract and scenario register, retaining unclear “preset limit” / “not spending limit” and “gold” wording.
- Recorded the three scenario types and positive verbatim-disclosure trigger; extended sequence capability without assuming the generic disclosure example and ESP transfer are the same case.
- Added C48 (confirmed scenario-level verbatim behavior), C49/C50 (proposed domain-scoped evaluation and associations), R58 (transcript-input dependency), and R59 (proposed scoping-configuration dependency).
- Updated entity-role qualifications; domain/entity metadata does not establish mandatory runtime extraction. No new component provider, catalog schema, detector implementation or filter placement selected.
- Updated questions, requirements, decisions, traceability, inventory and README; preserved v0.2 structured snapshot. Counts: 50 records, 59 relationships.
- Diagram/previews remain v0.1 and unchanged under U02. No final design generated.

## v0.4 — 2026-10-08 — documentation/model only

- Added M04 source extract; preserved v0.3 structured snapshot.
- Promoted independent microbatch input C30 and in-memory same-conversation context C47 to confirmed requirements. Kept recent-entity caching distinct.
- Added C51 interface responsibility, C52 signal schema, C53 management console, C54 call-metadata applicability selection as source-supported logical records; C55 signal composition remains proposed.
- Added R60–R64 logical dependencies (interface input, history access, catalog applicability and proposed prior/new-signal inputs), with no unspecified service/API wiring.
- Recorded the demo's two/three concurrent calls and clarified that call parallelism does not settle detector scheduling or production scale.
- Kept third detector identity, console build/reuse choice, schema, metadata, normalization kind, batch policies and cache lifecycle open.
- Updated related records; totals 55 inventory records and 64 relationships. Draw.io and previews remain unchanged at v0.1 under U02.

## v1.0 — 2026-10-08 — consolidated diagram authorized

- U05 lifts diagram hold; preserve v0.1 diagram/previews under diagrams/archive and v0.4 model snapshot.
- Incorporated M05 and seven newly supplied planning images, retaining earlier assertions and disagreements.
- Clarified three methods including LLM, Ingestor ownership and prototype call-ID convention; preserved classifier deferral and unknown model endpoint.
- Added source-backed service/adapter/management assets, PostgreSQL vector/GKE reports and reference-only BigQuery persistence. No physical topology invented.
- Recorded unified candidate catalog fields, source scenario families, composite low priority, monorepo, logging/tracing and remaining conflicts.
- Consolidated current logical diagram replaces outdated v0.1 while maintaining stable component identities where possible; review qualifiers remain explicit.

- U06 resolves emulator packaging as separate module/service and retains BigQuery as reference-only. Added logical R90–R92 for future provider adapter and applicability ordering; total 92 relationship records.

## v1.1 — 2026-10-08 — user-approved resolution and presentation changes

- Archived v1.0 diagram/preview/renderer and structured model.
- Removed “Not Policy Manager,” unresolved-design panel, and LOW PRIORITY from Composite Signals title; supporting decisions retained.
- Relabeled shared Signal Resolution as threshold-based acceptance. Semantic-to-resolution now confirmed; LLM direct-to-detected-result bypass replaced by R93 to resolver.
- Kept the existing resolver-to-accepted-signal/event publication paths. Did not choose threshold values, per-method semantics or a multi-method aggregation policy.
- Updated inventory, relationships, provenance and questions; retained original review as historical. BigQuery/future qualifiers unchanged.

## v1.2 — 2026-10-09 — live audio vision and concurrent ingestion

- Preserve the latest published v1.1 refined diagram/preview/renderer and model snapshot.
- Add M06/M07 evidence and questions. Mark emulator as a purple test source; add proposed live audio hook and streaming STT producing transcript input.
- Add multi-conversation ingress listener C73 and queue C74; reuse C08 as an illustrative scalable ingestion worker pool executing C56 responsibilities.
- Replace active R66 adapter-to-Ingestor shortcut with R97–R100. Preserve R66 and earlier A04 stream/partition relationships as qualified history.
- Retain every downstream detector/resolver connection and label, reference-only BigQuery and future provider qualifiers. No broker, STT model, replica count, retry guarantee or automatic scaling mechanism selected.
- Model: 74 components and 100 relationships; diagram: 65 editable vertices and 40 connectors. Worker instances are visual examples of C08; R100 is represented by containment.
- Update inventory, integration matrix, coverage, requirements and validation. This local revision is not a deployment or production approval.

## v1.2 presentation cleanup — 2026-10-09

Removed all visible meeting, architecture-image, planning-image and user-decision reference codes from diagram labels and connector captions. Preserved internal IDs, source records, every component/connection, geometry and technical metrics (P50/P95/P99 and latency target). Archived the annotated version; regenerated canonical draw.io/SVG/PNG for demonstration.
