# Source-supported concerns — v0.1

A01 explicitly names four **primary concerns** in a proposed architecture. They are displayed as logical bands, not inferred deployment tiers or security boundaries.

| ID | Exact name | Supported responsibility | Source | Status |
|---|---|---|---|---|
| L01 | Interaction Streaming | Acquire live interaction, normalize events, manage conversation lifecycle | A01–A04 | CONFIRMED as documented concern |
| L02 | Real-time Signal Detection | Evaluate transcript events through deterministic and semantic mechanisms | A01,A05,A06 | CONFIRMED as documented concern |
| L03 | Contextual Generation | Selectively invoke deeper context assembly when a detected signal warrants it | A01 | CONFIRMED as documented concern |
| L04 | Activation | Deliver signal, recommendation or experience to downstream consumers | A01 | CONFIRMED as documented concern |

“Conversation Sources”, “Detection”, and “Signal Output” are POC group labels in A09, not three additional enterprise layers. Signal Output is shown as a POC group inside the diagram's detection area for readability only; its ownership relative to Activation remains UNKNOWN. Genesys is an upstream system; downstream consumer and VANTAGE boundaries are not established. The diagram does not invent trust zones.

Event Mapper versus Normalize Transcript Event, Context Buffer versus conversation context/microbuffer/cache, and Signal Evidence versus Combine Results remain distinct source names pending confirmation. Cognitive implementation is not automatically equated with Contextual Generation. Observability/instrumentation is a cross-cutting requirement; no monitoring product or service is specified.

## M02 continuation

No layer or runtime boundary changes. Conversation signal history (C45), sequence-dependent detection (C46), and memory caching (C47) are recorded without assigning them to a new or existing implementation layer. Their realization remains open. Existing diagram placement is historical v0.1 and is held under U02.

## M03 continuation

No concern, layer or boundary changes. Scenario categories and the proposed domain model are recorded without creating new layers. C48 is a scenario-level capability; C49/C50 are proposed behavior/metadata with placement UNKNOWN.

## M04 workstreams

“Interfacing layer,” “signal build,” and “execution flow” are recorded as the three named demo responsibilities. They do not replace A01’s four concerns. Normalization is assigned to the interface responsibility, but neither event normalization nor transcript cleanup is silently moved/merged in the diagram. The three detector paths have only two unambiguous names (deterministic and semantic); the remaining “signal detection” label is unresolved.

## v1.0 — consolidated layout and boundaries

L01–L04 remain the four source-named primary concerns. L01 now contains the logical adapter/Ingestor responsibilities; L02 contains Signal Detector and the three methods. L03/L04 remain later selective generation/delivery concerns, not new implementations. Signal Management is an explicitly supported companion capability (M05/P05); stores, GKE, monorepo and observability are supporting groups, not fabricated processing layers.

Diagram uses logical ownership containers, not cloud trust zones or deployment boundaries. Ingestor contains session management, normalization and buffering responsibilities; default adapter is shown at its ingress with packaging noted open. Emulator is a separate module/service per U06. Signal Management contains catalog definition assets. Vector DB supports semantic retrieval; BigQuery remains reference-only per U06. GKE has no inferred pod/service/database placements. Earlier internal keyed stream/partitions/workers remain the A04 scaling reference, not a newly mandated broker in the prototype path.

## v1.1

No layer or service boundary changes. All configured detection methods now use shared threshold-based Signal Resolution. Presentation-only removals do not change stored decisions or composite priority.
