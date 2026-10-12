# V4 enterprise architecture review checklist

**This is a review-readiness checklist against the user's V4 requirements and available baseline, not certification against an unavailable enterprise control standard.** Formal EARB approval, architecture ownership and enterprise security/control inheritance remain OPEN.

| Check | Result | Evidence / limitation |
|---|---|---|
| V3 reviewed before changes | PASS | Review register produced first; latest local V3 used, including shaded process containers |
| V3 preserved | PASS | SHA-256 verification of every V3 file; saved baseline hashes |
| Architecture metadata | PASS | Name, level, V4, DRAFT status, GCP/GKE target, date, baseline; owner explicitly UNASSIGNED |
| Stable component / interface IDs | PASS | All prior IDs preserved; componentId/interfaceId metadata plus complete matrix |
| Source traceability | PASS with qualifications | Detector refs made specific; incorrect workbench R40 removed; model/storage proposals labeled as such rather than invented source relationships |
| All significant V3 technical components retained | PASS | 38 baseline vertices preserved; historical/deferred logical variants are not made new runtime dependencies |
| Detection semantics | PASS | Selective applicability, three methods and common threshold resolution retained; no mandatory all-method schedule or score calibration asserted |
| Runtime versus managed-service placement | PASS | Managed service parents are GCP, application process groups remain within GKE |
| Trust-boundary correctness | QUALIFIED | Runtime/grouping borders explicitly not trust zones; actual ingress/network/authentication design OPEN |
| State and data authority | OPEN, documented | Data authority, history writer, retention and recovery matrix in decision register |
| Protocol discipline | PASS | Existing proposals remain proposals; unspecified contracts remain OPEN |
| Security/privacy and inherited controls | OPEN, documented | Candidate enterprise/application responsibilities separated; no verification of implemented controls |
| Reliability/delivery guarantees | OPEN, documented | Ack/idempotency/replay/degradation questions retained; no exactly-once or no-loss implementation claim |
| AI governance/evaluation | OPEN / PROPOSED | Versioning, quality datasets, human feedback and drift review described without new platform dependency |
| Performance objectives | OPEN | Stage P50/P95/P99 measurement plan; no arbitrary numerical SLO added |
| Level 1 discipline | PASS | No pod counts, manifests, subnet plan, payload schema or L2 diagram |
| Technology icons | PASS | 26 individual embedded SVG cells, byte-preserved from V3; vendor/neutral provenance retained in V3 icon inventory |
| Editable shape structure | PASS | Native component, container, status-label and connector cells; icons independently selectable under parent components |
| XML integrity | PASS | Parsed successfully; one page; unique IDs; valid connector endpoints |
| Geometry / text fit | PASS for generated view | Bounds, parent containment and sibling overlap checks; generator text-fit check passes |
| Connector routing | PASS for generated view | No route crosses unrelated component card interiors; crossings between separate lines do not imply junctions |
| Visual inspection | PASS for generated view | Final PNG inspected, plus side-by-side V3/V4 comparison; interface labels increased from 14 to 17, boundary-overlapping inference label moved |
| Normal presentation readability | QUALIFIED | Large technical canvas is intended for pan/zoom; body text 20, major title 30, interface labels 17. Status micro-labels supplement border/legend/matrix. Fit-to-screen on a small display reduces detail; do not present as a dense 16:9 slide |
| Native organizational draw.io compatibility | NOT TESTED | Standard native draw.io XML and embedded SVG validated; target editor import/export and font metrics not verified |
| Corporate design-template compliance | NOT VERIFIED | Supplied American Express-inspired palette retained; no approved internal template or complete standard available |
| Implementation / production validation | NOT VERIFIED | No application POC, environment inventory or live measurements available; diagram Python is tooling only |

## Reproduce checks

From the repository root:

```sh
python3 architecture/gcp-gke-level-1/v4/build_v4.py
python3 architecture/gcp-gke-level-1/v4/validate_v4.py
```

The generator emits draw.io, SVG and graph metadata; validator checks IDs, preservation, embedding, parents and routes. The PNG was generated with Sharp from the SVG and visually reviewed. Its rendering shares the source graph with the draw.io; it is not a native draw.io screenshot. Rerender PNG after source changes. No external icon access is needed to open the draw.io.

Icon provenance and reuse qualifications remain in [V3 icon inventory](../v3/technology-icon-inventory.md). V4 copies the same local SVG artwork and preserves its embedded payloads. No input JPEG is included. No GitHub push or infrastructure deployment was performed for this request.
