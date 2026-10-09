# Diagram coverage — v1.2

Every inventory record is either drawn or has an explicit disposition. This is a logical architecture view; historical experiments and unconfirmed physical structures are retained in records without becoming invented baseline services.

| ID | Name | Diagram / record location | Disposition |
|---|---|---|---|
| C01 | Genesys Cloud | C01 | Independently editable native shape; source/status qualifiers retained. |
| C02 | Transcript Emulator | C02 | Independently editable native shape; source/status qualifiers retained. |
| C03 | Genesys Connector | C58 / sources | Genesys connector preserved as future provider integration; not current default adapter identity. |
| C04 | Demultiplexer | C68; earlier A03 record | Conversation demultiplexing retained; no extra runtime demultiplexer service introduced. |
| C05 | Normalize Transcript Event | C05 | Independently editable native shape; source/status qualifiers retained. |
| C06 | Internal Transcript Stream | scaling-note | Earlier A04 keyed stream architecture retained as scaling reference; broker not selected. |
| C07 | Partition 1 / Partition 2 / Partition 3 | scaling-note | Partitions are illustrative earlier scaling detail, not mandated current instance count. |
| C08 | Ingestion worker pool / service nodes | C08; worker-a / worker-b / worker-n | Current M07 worker pool; three visual instances are illustrative, not a selected count. C56 common responsibilities shown inside. |
| C09 | Conversation Context A / Conversation Context B / Conversation Context C | C47; earlier A04 record | Conversation context requirement retained; physical equivalence of historical contexts remains open. |
| C10 | Event Mapper | C56 responsibility; inventory | Event Mapper historical name retained, not silently asserted as a distinct new service. |
| C11 | Context Buffer | C69 responsibility; inventory | Context Buffer name retained; not asserted identical to entity cache/full log. |
| C12 | Transcript Event / Detection Input | R92 / R67; C59 input | Logical transcript input represented by flow; no new deployable input service. |
| C13 | Signal Catalog | C13 | Independently editable native shape; source/status qualifiers retained. |
| C14 | Rules | C14 | Independently editable native shape; source/status qualifiers retained. |
| C15 | Regex | C15 | Independently editable native shape; source/status qualifiers retained. |
| C16 | Fuzzy | C16 | Independently editable native shape; source/status qualifiers retained. |
| C17 | Entity | C17 | Independently editable native shape; source/status qualifiers retained. |
| C18 | Embedding | C18 | Independently editable native shape; source/status qualifiers retained. |
| C19 | Vector Search | C19 | Independently editable native shape; source/status qualifiers retained. |
| C20 | Classifier | supporting records | Separate configured/trained classifier deferred; not replaced by an asserted model identity. |
| C21 | Signal Evidence | C21 | Independently editable native shape; source/status qualifiers retained. |
| C22 | Signal Resolution | C22 | Independently editable native shape; source/status qualifiers retained. |
| C23 | Detected Signal | C23 | Independently editable native shape; source/status qualifiers retained. |
| C24 | Signal Events | C24 | Independently editable native shape; source/status qualifiers retained. |
| C25 | Real-Time Signal Workbench | C25 | Independently editable native shape; source/status qualifiers retained. |
| C26 | Optional Signal Store | inventory; C63 reference store | Earlier optional signal store retained; no unconfirmed equivalence to BigQuery. |
| C27 | Contextual Generation | C27 | Independently editable native shape; source/status qualifiers retained. |
| C28 | Activation | C28 | Independently editable native shape; source/status qualifiers retained. |
| C29 | Downstream Consumers | C29 | Independently editable native shape; source/status qualifiers retained. |
| C30 | Upstream Utterance / Microbuffered Sentence | C69 | Microbatch output represented by ingestion buffering capability. |
| C31 | Normalize Transcript | C05 / supporting records | Text cleanup proposal retained; precise normalization transformations unconfirmed. |
| C32 | Entity / Target Keyword(s) Extraction | supporting records / C64 | Runtime entity-first extraction remains conflicting; dictionary metadata shown independently. |
| C33 | Conversation Context Cache | inventory / supporting records | Recent-entity cache proposal not silently merged with confirmed Context Cache. |
| C34 | Enrich Transcript | supporting records | Entity-appended transcript not a mandatory baseline dependency. |
| C35 | Top-K Candidate Signals | C35 | Independently editable native shape; source/status qualifiers retained. |
| C36 | BGE Reranker | C36 | Independently editable native shape; source/status qualifiers retained. |
| C37 | Async: Store Detection Data for Classifier Training | inventory / supporting records | Async classifier-training storage remains proposed; no added store in current scope. |
| C38 | Classifier Detector / Load Configured Classifier / Signal Classification | supporting records | Configured classifier branch remains deferred. |
| C39 | Deterministic Detector / Combine Results | C39 | Independently editable native shape; source/status qualifiers retained. |
| C40 | Publish Signal to SSE / WebSocket | transport-note | SSE/WebSocket output proposal retained; not current transport commitment. |
| C41 | VANTAGE signal management | C53 / inventory | VANTAGE-style management reference retained; no established VANTAGE integration drawn. |
| C42 | Mini-based detection mechanism | C60 | LLM method current; specific mini access/model choice not assumed. |
| C43 | Few-shot example retrieval | inventory; C65 | Few-shot-to-LLM proposal retained; curated examples do not imply confirmed RAG wiring. |
| C44 | Latency instrumentation / Observability | C44 | Independently editable native shape; source/status qualifiers retained. |
| C45 | Conversation signal history (descriptive capability) | C47 | Earlier same-call signals explicitly in memory context; no separate history store. |
| C46 | Sequence-dependent detection (descriptive capability) | C55 / scenario register | Sequence-dependent behavior retained as scenario requirement; no separate engine inferred. |
| C47 | Context Cache (earlier label: memory caching) | C47 | Independently editable native shape; source/status qualifiers retained. |
| C48 | Verbatim disclosure detection (descriptive capability) | C39 / scenario register | Verbatim behavior belongs to validation scenarios; no exact algorithm mandated. |
| C49 | Domain-scoped signal/entity evaluation (descriptive capability) | C54 / inventory | Domain-specific eligibility proposal remains distinct from confirmed metadata applicability. |
| C50 | Signal-domain and related-entity associations (descriptive metadata) | C67 / C64 / schema-note | Domain/entity associations shown as planned metadata, not approved runtime filter schema. |
| C51 | interfacing layer (meeting wording) | C57 / C56 | Earlier interface responsibility refined by named adapter and Ingestor. |
| C52 | Signal Definitions / signal schema | C52 | Independently editable native shape; source/status qualifiers retained. |
| C53 | Signal Management UI (earlier: management console) | C53 | Independently editable native shape; source/status qualifiers retained. |
| C54 | Call-metadata signal applicability selection (descriptive capability) | C54 | Independently editable native shape; source/status qualifiers retained. |
| C55 | Prior-signal plus new-signal composition (descriptive capability) | C55 | Independently editable native shape; source/status qualifiers retained. |
| C56 | Ingestor service / Call Ingestor | C56 inside C08 | Common responsibilities across ingestion workers; R100 expressed by containment. |
| C57 | Default WebSocket adapter | C57 | Independently editable native shape; source/status qualifiers retained. |
| C58 | Genesys / outreach adapters | C58 | Independently editable native shape; source/status qualifiers retained. |
| C59 | Detector service / Signal Detector | C59 | Independently editable native shape; source/status qualifiers retained. |
| C60 | LLM-based detection | C60 | Independently editable native shape; source/status qualifiers retained. |
| C61 | Vector DB — PostgreSQL / “p vector” (meeting wording) | C61 | Independently editable native shape; source/status qualifiers retained. |
| C62 | “sales profit” GKE instance | C62 | Independently editable native shape; source/status qualifiers retained. |
| C63 | BigQuery — Utterance & Call Log | C63 | Independently editable native shape; source/status qualifiers retained. |
| C64 | Entity Dictionary | C64 | Independently editable native shape; source/status qualifiers retained. |
| C65 | Curated Examples — Positive / Negative | C65 | Independently editable native shape; source/status qualifiers retained. |
| C66 | Regulatory / Policy Mappings | C66 | Independently editable native shape; source/status qualifiers retained. |
| C67 | Signal Taxonomy — Domain → Group → Signal | C67 | Independently editable native shape; source/status qualifiers retained. |
| C68 | Session management | C68 | Independently editable native shape; source/status qualifiers retained. |
| C69 | Segmentation / buffering / windowing | C69 | Independently editable native shape; source/status qualifiers retained. |
| C70 | Common Git repository / monorepo | C70 | Independently editable native shape; source/status qualifiers retained. |

## v1.2 additions

| ID | Name | Diagram / record location | Disposition |
|---|---|---|---|
| C71 | Live audio hook / connector | C71 | Proposed target capability, amber dashed; access/interface unverified. |
| C72 | Streaming speech-to-text | C72 | Proposed target capability, amber dashed; engine not selected. |
| C73 | Multi-conversation ingress listener | C73 | Concurrent producer responsibility; no separate deployment asserted. |
| C74 | Message queue / broker | C74 | Required buffering boundary before ingestion workers; product and guarantees open. |

R94–R99 are drawn. R100 is C56 containment inside C08. R66 is absent from the active diagram and qualified as superseded in the integration matrix. R05–R08 remain historical A04 references. All 74 inventory IDs have a disposition; visual worker instances map to C08.
