# Current validation — v1.1

- Parsed native draw.io XML successfully: one editable page, 57 vertex shapes, 35 connectors; unique IDs and valid parent/connector references.
- Containers use native parent/child cells. Components and connectors are editable; no embedded flattened diagram.
- Renderer checked conservative text fit, child containment and peer-box overlap. All passed after layout adjustments.
- Model has 70 unique component/capability/metadata IDs and 93 unique relationship IDs, with valid endpoints/status/source references.
- Every inventory record has a disposition in [diagram-coverage.md](diagram-coverage.md). Every visible connector has model relationship evidence. Historical LLM bypass R82 is absent from the current diagram; R93 enters Signal Resolution.
- Preserved v0.1 diagram/preview archive and v0.4 structured snapshot. U07 authorizes this update; v1.0 diagram/model also archived.
- Confirmed emulator is separate. BigQuery and its writes stay reference-only. Future provider adapters remain dashed; semantic and LLM result paths now enter confirmed shared resolution. No GKE deployment topology, unselected classifier, entity-first mandatory preprocessing, authentication removal or telemetry backend invented.
- Source audit distinguishes LLM detection from later Contextual Generation, bounded context from full conversation storage, schema planning from approval, and reported infrastructure from verified readiness.
- A companion SVG/PNG preview is generated from the same geometry and visually inspected. Native diagrams.net rendering/import is not verified; connector routing/text wrapping may differ in that application.
- Graph checks verify that deterministic, semantic and LLM results reach accepted signals and event publication through the resolver, with no bypass. Threshold values/scope, score semantics and multi-method acceptance remain open. No implementation tests, performance benchmarks, vendor access checks, deployment or production approval claimed.

## Presentation refinement

The canonical diagram now uses the reviewed presentation. Exact node/edge IDs, decoded labels, parents and endpoints match the archived v1.1 baseline. XML, text-height fit, containment and sibling-box checks pass. The structured architecture model is unchanged. The SVG-derived PNG was visually reviewed; native diagrams.net rendering remains unverified. See diagrams/layout-validation.json for reproducible check results.
