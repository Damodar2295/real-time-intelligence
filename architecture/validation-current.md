# Current validation — v1.2

- Native editable draw.io XML parses: one page, 65 vertices and 40 connectors. Model has 74 components and 100 source relationships.
- Every displayed connector references a model relationship; individual connector endpoints match the model. Worker instances are visual examples of C08. R100 is represented by C56 containment within C08.
- Compared with archived published v1.1: every unchanged node label, parent and edge endpoint is preserved. Explicit changes are limited to M06/M07 source/ingestion scope, related annotations and current repository status. No downstream detector/resolver wiring changed.
- Historical R66 direct adapter-to-Ingestor connection is absent. Active adapter → listener → queue → worker-pool flow is present; audio/STT → listener links remain proposed. R82 LLM bypass remains absent.
- Text-height estimates, child containment and sibling-box non-overlap checks pass. SVG-derived PNG visually inspected; native diagrams.net import/rendering has not been verified.
- Prior v1.1 refined presentation and model archived. No broker/STT engine, queue count, thread-per-call implementation, at-most/at-least/exactly-once guarantee or production SLA selected.
- Input preservation, multi-call isolation and elasticity are requirements, not benchmarked guarantees. No runtime code, vendor access or deployment has been tested by this diagram update.

Machine-readable presentation checks: diagrams/layout-validation.json. Reproduce draw.io and SVG with `python3 architecture/tools/render_architecture.py`; PNG is a separate SVG raster export.

## Demonstration label cleanup

All visible source-reference codes removed. Compared with archived v1.2: only labels changed; 65 shapes, 40 connectors, endpoints, containment, styles and layout coordinates remain identical. Technical percentile and latency values retained. XML/text-fit checks passed; updated preview visually inspected. Source references remain in records and internal IDs, not visible labels.
