# V3 → V4 change summary

Baseline: latest local V3 with the three dotted, lightly shaded process groups, not only the earlier GitHub snapshot. V3 is unchanged byte for byte. V4 is a separate review package.

## Representation changes applied

| Change | Reason / review reference | Technical effect |
|---|---|---|
| Added architecture level/version, DRAFT review status, target, date, unassigned owner and decision-baseline metadata | V4-R21 | No implied EARB or production approval |
| Preserved stable component IDs; added component/interface/status metadata and complete matrix | V4-R21 | Traceability without visible reference-number clutter |
| Corrected generic detector source references and erroneous workbench R40 reference | V4-R21 | More accurate evidence attribution; identical endpoints |
| Marked model-call and storage-hosting links as prior technical proposals | V4-R21 | No new requirement or approved contract inferred |
| Added explicit role/proposal micro-labels and separate deployment qualification | V4-R09/R21 | Functional confirmation no longer conflated with implementation readiness |
| Added history-writer/recovery OPEN and scheduling/completion OPEN labels | V4-R05/R11 | Existing gaps made visible; no invented cache writer or scheduling policy |
| Clarified runtime/grouping versus trust boundaries | V4-R13/R22 | Security policy remains OPEN; no selected ingress or gateway |
| Distinguished dash-dot telemetry from dotted configuration | V4-R21 | Same aggregate observability dependency |
| Increased interface-label size and moved boundary-overlapping labels | V4-R21 | Readability improvement |
| Removed 40 pixels of unused space above runtime | V4-R21 | Shorter dependency routes; card dimensions and process layout preserved |

## Preserved

- 38 prior baseline vertices, all 25 stable connector IDs/source-target pairs, and 26 embedded icons.
- The three shaded process groups; ingestion worker pool inside ingestion and coordinator inside detection.
- Provider/emulator distinction; proposed audio/STT; queue-before-workers; bounded same-call context.
- Catalog applicability; selective deterministic, semantic top-K/reranker and LLM detection; common resolution.
- Later selective generation/activation; proposed storage/products/protocols; BigQuery reference-only.
- Existing blue palette and official Google legacy service artwork. No logos introduced from unrelated reference technologies.

## Decisions not made

No change to thresholds, evidence/abstention/finality, detector parallelism/fallback, authoritative stores, cache write-back ownership, queue semantics, retry or recovery behavior, model selection, deployment units, network trust policy, authentication, data classification, retention, service quotas or numeric SLOs. These remain in the review and decision registers. No new runtime box, service or data interface was added.

## Validation outcome and limits

XML/ID/endpoint/icon/parent checks pass. V3 hashes match. The generated view passes geometry and text-fit checks; routing avoids unrelated component interiors. V3 and V4 were rendered and compared side by side. Native organizational draw.io import and runtime behavior are not tested. Formal compliance with enterprise standards cannot be asserted because those standards were not supplied.

## Files for review

- `vantage-gcp-gke-technical-level-1-v4.drawio` — editable diagram
- `vantage-gcp-gke-technical-level-1-v4.svg` / `.png` — presentation exports
- `architecture-review-register.md` — 22 findings across all ten domains, with priorities and stakeholders
- `architecture-decision-register-v4.md` — retained decisions, open data/security ownership and performance evaluation plan
- `component-interface-matrix-v4.md` — stable-ID component and interface mapping plus runtime considerations
- `enterprise-architecture-compliance-checklist.md` — validation and review limitations

Recommended EARB disposition: review the target representation and assign decision owners; do not interpret V4 as implementation readiness approval. Critical questions concern resolution semantics, signal-history ownership and live-data security/privacy controls. Only Level 1 is generated. V4 has not been pushed to GitHub.
