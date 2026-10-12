# Technology icon inventory — V3

Official service artwork comes from [Google Cloud’s icon library](https://cloud.google.com/icons), specifically the [legacy SVG archive](https://services.google.com/fh/files/misc/google-cloud-legacy-icons.zip). It is the Google-provided legacy family, intentionally identified as such rather than represented as the latest icon family. Original colors/aspect ratios are preserved. No reference-photo crops or external image URLs are used in the diagram.

Reuse considerations: Google supplies this collection for architecture/documentation use. Vendor marks remain subject to Google’s applicable brand and reuse terms; no independent permissive license or enterprise approval is asserted. Review those terms for external redistribution. The inventory distinguishes original neutral symbols from vendor artwork. Neutral symbols are project-created SVG geometry and do not represent vendor trademarks. No internal approved icon library was available.

The downloadable draw.io embeds all icons; the adjacent SVG assets support reproducible generation. Each icon is a separate image cell parented to its component. Cloud Monitoring, Trace and IAM are additional icons within the existing aggregate panels, not new services or connections.

| Component ID (internal only) | SVG asset | Source / technology | Architecture status | Embedded |
|---|---|---|---|---|
| gke | google_kubernetes_engine.svg | Google official legacy icon library | Confirmed target | Yes; embedded SVG child cell |
| genesys | neutral-cloud.svg | Original neutral capability symbol | Confirmed capability; hosting open | Yes; embedded SVG child cell |
| test | neutral-service.svg | Original neutral capability symbol | Confirmed capability; hosting open | Yes; embedded SVG child cell |
| stt | speech-to-text.svg | Google official legacy icon library | Proposed packaging / product; see decisions | Yes; embedded SVG child cell |
| queue | pubsub.svg | Google official legacy icon library | Proposed packaging / product; see decisions | Yes; embedded SVG child cell |
| state | memorystore.svg | Google official legacy icon library | Proposed packaging / product; see decisions | Yes; embedded SVG child cell |
| sql | cloud_sql.svg | Google official legacy icon library | Proposed packaging / product; see decisions | Yes; embedded SVG child cell |
| model | vertexai.svg | Google official legacy icon library | Proposed packaging / product; see decisions | Yes; embedded SVG child cell |
| bridge | neutral-audio.svg | Original neutral capability symbol | Proposed packaging / product; see decisions | Yes; embedded SVG child cell |
| ingress | neutral-service.svg | Original neutral capability symbol | Proposed packaging / product; see decisions | Yes; embedded SVG child cell |
| worker | neutral-service.svg | Original neutral capability symbol | Proposed packaging / product; see decisions | Yes; embedded SVG child cell |
| coord | neutral-branch.svg | Original neutral capability symbol | Proposed packaging / product; see decisions | Yes; embedded SVG child cell |
| rules | neutral-service.svg | Original neutral capability symbol | Proposed packaging / product; see decisions | Yes; embedded SVG child cell |
| semantic | neutral-search.svg | Original neutral capability symbol | Proposed packaging / product; see decisions | Yes; embedded SVG child cell |
| llm | neutral-service.svg | Original neutral capability symbol | Proposed packaging / product; see decisions | Yes; embedded SVG child cell |
| resolver | neutral-check.svg | Original neutral capability symbol | Proposed packaging / product; see decisions | Yes; embedded SVG child cell |
| publisher | neutral-service.svg | Original neutral capability symbol | Proposed packaging / product; see decisions | Yes; embedded SVG child cell |
| management | neutral-screen.svg | Original neutral capability symbol | Proposed packaging / product; see decisions | Yes; embedded SVG child cell |
| later | neutral-branch.svg | Original neutral capability symbol | Proposed packaging / product; see decisions | Yes; embedded SVG child cell |
| workbench | neutral-screen.svg | Original neutral capability symbol | Confirmed capability; hosting open | Yes; embedded SVG child cell |
| consumers | neutral-screen.svg | Original neutral capability symbol | Proposed packaging / product; see decisions | Yes; embedded SVG child cell |
| telemetry | cloud_logging.svg | Google official legacy icon library | Proposed packaging / product; see decisions | Yes; embedded SVG child cell |
| controls | secret_manager.svg | Google official legacy icon library | Proposed packaging / product; see decisions | Yes; embedded SVG child cell |
| telemetry | cloud_monitoring.svg | Google official legacy icon library | Proposed packaging / product; see decisions | Yes; embedded SVG child cell |
| telemetry | trace.svg | Google official legacy icon library | Proposed packaging / product; see decisions | Yes; embedded SVG child cell |
| controls | identity_and_access_management.svg | Google official legacy icon library | Proposed packaging / product; see decisions | Yes; embedded SVG child cell |

Limitations: Genesys uses an explicitly neutral cloud symbol because no approved vendor artwork was available in the supplied assets. Application workloads use neutral capability symbols because their language/framework is not selected. Google Cloud uses a named boundary; the GKE boundary uses the official GKE icon. Cloud SQL represents proposed PostgreSQL/pgvector hosting; Memorystore represents the proposed Redis service. No separate PostgreSQL/Redis brand logo is used. Unused helper icon assets do not imply architecture selection.
