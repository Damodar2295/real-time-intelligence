# Integration matrix — v1.1

Historical source assertions are retained. R82 is superseded for runtime flow by R93; its CONFIRMED status denotes its historical source, not a current bypass. U07 requires common threshold-based resolution for all configured methods.

| ID | Source | Target | Flow | Mechanism | Evidence | Status | Current scope |
|---|---|---|---|---|---|---|---|
| R01 | C01 | C03 | Notification events; setup: Authenticate OAuth → Create Notification Channel → Subscribe to Required Topics | OAuth setup; Genesys WebSocket | A02 | CONFIRMED | See component qualification |
| R02 | C02 | C03 | Simulated transcript input in POC source diagram | UNKNOWN | A09 | CONFIRMED | See component qualification |
| R03 | C03 | C04 | Multiplexed events for routing | conversation_id | A02,A03 | CONFIRMED | See component qualification |
| R04 | C04 | C05 | Routed events normalized by ingestion | UNKNOWN | A03 | CONFIRMED | See component qualification |
| R05 | C05 | C06 | Publish normalized internal transcript events | UNKNOWN | A03,A04 | CONFIRMED | See component qualification |
| R06 | C06 | C07 | Keyed events to illustrative partitions | interaction_id / conversation_id; broker UNKNOWN | A04 | CONFIRMED | See component qualification |
| R07 | C07 | C08 | Partition events to processing workers | UNKNOWN | A04 | CONFIRMED | See component qualification |
| R08 | C08 | C09 | Maintain conversation context | UNKNOWN | A04 | CONFIRMED | See component qualification |
| R09 | C09 | C12 | Bounded context accessible to detection; logical dependency, not a specified transport | UNKNOWN | A05 | CONFIRMED | See component qualification |
| R10 | C03 | C10 | POC received events | UNKNOWN | A09 | CONFIRMED | See component qualification |
| R11 | C10 | C11 | POC mapped events | UNKNOWN | A09 | CONFIRMED | See component qualification |
| R12 | C11 | C13 | Arrow as drawn in POC; runtime event path versus configuration boundary unclear | UNKNOWN | A09 | CONFLICTING | See component qualification |
| R13 | C13 | C14 | Catalog supplies detection configuration (logical dependency) | UNKNOWN | A09,A10 | CONFIRMED | See component qualification |
| R14 | C13 | C15 | Catalog supplies detection configuration (logical dependency) | UNKNOWN | A09,A10 | CONFIRMED | See component qualification |
| R15 | C13 | C16 | Catalog supplies detection configuration (logical dependency) | UNKNOWN | A09,A10 | CONFIRMED | See component qualification |
| R16 | C13 | C17 | Catalog supplies detection configuration (logical dependency) | UNKNOWN | A09,A10 | CONFIRMED | See component qualification |
| R17 | C12 | C14 | Deterministic evaluation of transcript input; scheduling unspecified | UNKNOWN | A05,A06 | CONFIRMED | See component qualification |
| R18 | C12 | C15 | Deterministic evaluation of transcript input; scheduling unspecified | UNKNOWN | A05,A06 | CONFIRMED | See component qualification |
| R19 | C12 | C16 | Deterministic evaluation of transcript input; scheduling unspecified | UNKNOWN | A05,A06 | CONFIRMED | See component qualification |
| R20 | C12 | C17 | Deterministic evaluation of transcript input; scheduling unspecified | UNKNOWN | A05,A06 | CONFIRMED | See component qualification |
| R21 | C14 | C21 | Detection evidence | UNKNOWN | A05 | CONFIRMED | See component qualification |
| R22 | C15 | C21 | Detection evidence | UNKNOWN | A05 | CONFIRMED | See component qualification |
| R23 | C16 | C21 | Detection evidence | UNKNOWN | A05 | CONFIRMED | See component qualification |
| R24 | C17 | C21 | Detection evidence | UNKNOWN | A05 | CONFIRMED | See component qualification |
| R25 | C12 | C18 | Transcript for semantic embedding; applicability/scheduling unresolved | UNKNOWN | A05,A06 | CONFIRMED | See component qualification |
| R26 | C18 | C19 | Embedding for vector retrieval | UNKNOWN | A05,A06 | CONFIRMED | See component qualification |
| R27 | C19 | C20 | Vector-search output to classifier in A05; independent classifier in A06/S02 | UNKNOWN | A05,A06,S02,M02.2 | CONFLICTING | Earlier reference relationship retained; classifier implementation deferred per M02.2; no active POC classifier wiring newly approved |
| R28 | C12 | C20 | Transcript/context directly to classifier in A06; A05 shows serial retrieval | UNKNOWN | A05,A06,S02,M02.2 | CONFLICTING | Earlier reference relationship retained; classifier implementation deferred per M02.2; no active POC classifier wiring newly approved |
| R29 | C20 | C21 | Classification evidence | UNKNOWN | A05,M02.2 | CONFIRMED | Earlier reference relationship retained; classifier implementation deferred per M02.2; no active POC classifier wiring newly approved |
| R30 | C21 | C22 | Aggregate evidence for resolution | UNKNOWN | A05,A06 | CONFIRMED | See component qualification |
| R31 | C22 | C23 | Publish logical accepted signal after shared threshold-based resolution | UNKNOWN | A05,U07 | CONFIRMED | See component qualification |
| R32 | C22 | C24 | Signal output events | UNKNOWN | A09,A10,U07 | CONFIRMED | Signal output from shared resolution; all configured method results must pass acceptance before this publication path |
| R33 | C24 | C25 | POC signal display | UNKNOWN | A09,A10 | CONFIRMED | See component qualification |
| R34 | C24 | C26 | Optional persistence | UNKNOWN | A09,A10 | PROPOSED | See component qualification |
| R35 | C23 | C27 | Selective deeper context assembly when signal warrants it | UNKNOWN | A01 | CONFIRMED | See component qualification |
| R36 | C27 | C28 | Eventual contextual reasoning → activation; interface not specified | UNKNOWN | A10 | CONFIRMED | See component qualification |
| R37 | C28 | C29 | Signal, recommendation or experience delivery | UNKNOWN | A01 | CONFIRMED | See component qualification |
| R38 | C30 | C31 | Microbuffered transcript for cleanup | UNKNOWN | S01,M01.3 | PROPOSED | See component qualification |
| R39 | C31 | C32 | Pre-detection entity extraction; placement challenged | UNKNOWN | S01,M01.7,M02.3 | CONFLICTING | Entity-appending approach remains challenged; benefit and mandatory placement unconfirmed |
| R40 | C32 | C33 | Entity found: update cache asynchronously; absent: load cached entity | In-memory proposed; async update depicted | S01,M01.4 | PROPOSED | See component qualification |
| R41 | C32 | C34 | Found entity enriches transcript | UNKNOWN | S01,M01.4,M02.3 | PROPOSED | Entity-appending approach remains challenged; benefit and mandatory placement unconfirmed |
| R42 | C33 | C34 | Cached entity enriches transcript when entity absent | UNKNOWN | S01,M01.4,M02.3 | PROPOSED | Entity-appending approach remains challenged; benefit and mandatory placement unconfirmed |
| R43 | C34 | C12 | Enrichment as shared upstream detection dependency is challenged | UNKNOWN | S01,M01.7,M02.3 | CONFLICTING | Entity-appending approach remains challenged; benefit and mandatory placement unconfirmed |
| R44 | C31 | C39 | Direct deterministic bypass shown as dotted line; relation to second ingress unresolved | UNKNOWN | S01,M01.3 | CONFLICTING | See component qualification |
| R45 | C19 | C35 | Vector retrieval produces top-K candidate signals in the current semantic-path direction; K UNKNOWN | UNKNOWN | S02,M01.6,M02.1,M02.2 | CONFIRMED | See component qualification |
| R46 | C35 | C36 | Top-K candidates supply signal descriptions for reranking against the utterance; retained count UNKNOWN | Joint utterance–candidate description scoring described in meeting; model version and API UNKNOWN | S02,M01.6,M02.1,M02.2 | CONFIRMED | See component qualification |
| R47 | C36 | C22 | Reranker results to resolution | UNKNOWN | S02,U07 | CONFIRMED | Current baseline: semantic reranker results enter shared threshold-based resolution; numeric thresholds and scoring contract not chosen |
| R48 | C36 | C37 | Async training-data storage | UNKNOWN | S02,S03 | PROPOSED | See component qualification |
| R49 | C38 | C22 | Classifier results to resolution | UNKNOWN | S02,M02.2 | PROPOSED | Earlier reference relationship retained; classifier implementation deferred per M02.2; no active POC classifier wiring newly approved |
| R50 | C39 | C22 | Combined deterministic results to resolution | UNKNOWN | S02 | CONFIRMED | See component qualification |
| R51 | C22 | C40 | Signal Detected? Yes branch | SSE / WebSocket alternatives | S03 | PROPOSED | See component qualification |
| R52 | C40 | C29 | Publish detected signal | SSE / WebSocket alternatives | S03 | PROPOSED | See component qualification |
| R53 | C41 | C13 | Reuse VANTAGE-managed signals as catalog; integration undecided | UNKNOWN | M01.1 | PROPOSED | See component qualification |
| R54 | C43 | C42 | Retrieve examples and pass to LLM | Vector search proposed; API unknown | M01.2 | PROPOSED | See component qualification |
| R55 | C12 | C36 | Utterance is paired with each candidate signal description for reranker evaluation; representation/preprocessing unresolved | Logical input dependency only; no direct network call or bypass implied | M02.1 | CONFIRMED | See component qualification |
| R56 | C23 | C45 | Remember occurrence of the pivot signal for that conversation; exact pivot trigger unresolved | Functional state requirement; persistence, API and implementation UNKNOWN | M02.4 | CONFIRMED | See component qualification |
| R57 | C45 | C46 | Earlier pivot occurrence contributes to detection with a later pattern in the same conversation | Logical dependency; near-vicinity definition and evaluation owner UNKNOWN | M02.4 | CONFIRMED | See component qualification |
| R58 | C12 | C48 | Evaluate conversation transcript for verbatim disclosure occurrence; text representation, boundaries and tolerance unspecified | Scenario-level input dependency; no regex, fuzzy or exact-string implementation selected | M03.2 | CONFIRMED | See component qualification |
| R59 | C50 | C49 | Use domain-associated signal/entity list to restrict checks; exclude remaining signals/entities in the proposed model | Configuration dependency proposed; ownership, domain assignment and filter placement UNKNOWN | M03.5 | PROPOSED | See component qualification |
| R60 | C51 | C30 | Distinguished per-call input proceeds to independent microbatch processing; batching ownership and exact normalization order not settled | Logical dependency only; API, service boundary and scheduling UNKNOWN | M04.1,M04.3 | CONFIRMED | See component qualification |
| R61 | C47 | C12 | Detection processing consults context from the same conversation for each independent microbatch; identity propagation contract UNKNOWN | Logical dependency only; API, service boundary and scheduling UNKNOWN | M04.1,M04.4 | CONFIRMED | See component qualification |
| R62 | C13 | C54 | Evaluate catalog signal applicability using call metadata before applying detection mechanisms; catalog provider and metadata source unspecified | Logical dependency only; API, service boundary and scheduling UNKNOWN | M04.2,M04.3 | CONFIRMED | See component qualification |
| R63 | C47 | C55 | Previously identified same-call signals provide earlier occurrence information for proposed composition | Logical dependency only; API, service boundary and scheduling UNKNOWN | M04.4,M05.6 | CONFIRMED | Low-priority composite requirement only; not an active deployed edge |
| R64 | C23 | C55 | A new signal can be combined with a previous same-call signal to determine a third; no recursion or publication policy specified | Logical dependency only; API, service boundary and scheduling UNKNOWN | M04.4,M05.6 | CONFIRMED | Low-priority composite requirement only; not an active deployed edge |
| R65 | C02 | C57 | Emulator supplies transcripts to WebSocket interface; concurrency extension requested | Logical data relationship; protocol unspecified unless stated | M05.1,M05.4 | CONFIRMED | See component qualification |
| R66 | C57 | C56 | Default adapter supplies input to ingestion processing; packaging unresolved | Logical data relationship; protocol unspecified unless stated | M05.4 | CONFIRMED | See component qualification |
| R67 | C56 | C59 | Utterance/event chunks to detector | Logical data relationship; protocol unspecified unless stated | M05.1,M05.2,P05 | CONFIRMED | See component qualification |
| R68 | C56 | C47 | Maintain recent same-call conversation context | Logical data relationship; protocol unspecified unless stated | M05.2,P05 | CONFIRMED | See component qualification |
| R69 | C47 | C59 | Conversation context for detection | Logical data relationship; protocol unspecified unless stated | P05,M05.2 | CONFIRMED | See component qualification |
| R70 | C52 | C59 | Detection method, criteria and parameters configure detector | Logical configuration relationship; protocol unspecified unless stated | M05.3,M05.5,P05 | CONFIRMED | See component qualification |
| R71 | C59 | C39 | Configured deterministic evaluation | Logical data relationship; protocol unspecified unless stated | M05.3,P05 | CONFIRMED | See component qualification |
| R72 | C59 | C18 | Semantic branch embeds utterance for vector retrieval | Logical data relationship; protocol unspecified unless stated | M05.3,P04,P05 | CONFIRMED | See component qualification |
| R73 | C59 | C60 | Configured LLM evaluation | Logical data relationship; protocol unspecified unless stated | M05.3,P05 | CONFIRMED | See component qualification |
| R74 | C65 | C52 | Positive/negative examples inform signal definitions | Logical configuration relationship; protocol unspecified unless stated | P05 | CONFIRMED | See component qualification |
| R75 | C64 | C52 | Entity references inform definitions | Logical configuration relationship; protocol unspecified unless stated | P05 | CONFIRMED | See component qualification |
| R76 | C66 | C52 | Requirement/regulatory mappings inform definitions | Logical configuration relationship; protocol unspecified unless stated | P05 | CONFIRMED | See component qualification |
| R77 | C67 | C52 | Taxonomy organizes signal definitions | Logical configuration relationship; protocol unspecified unless stated | P05 | CONFIRMED | See component qualification |
| R78 | C65 | C61 | Examples/embeddings populate vector database; embedding generation process not fully specified | Logical data relationship; protocol unspecified unless stated | M05.8,P05 | CONFIRMED | See component qualification |
| R79 | C19 | C61 | Top-K semantic retrieval against vector representations | Logical data relationship; protocol unspecified unless stated | P04,P05 | CONFIRMED | See component qualification |
| R80 | C56 | C63 | Persist utterances | Logical data relationship; protocol unspecified unless stated | P05,U06 | PROPOSED | See component qualification |
| R81 | C23 | C63 | Persist detected results | Logical data relationship; protocol unspecified unless stated | P05,U06 | PROPOSED | See component qualification |
| R82 | C60 | C23 | LLM strategy contributes detected-signal result; shared resolution policy unspecified | Logical data relationship; protocol unspecified unless stated | P05 | CONFIRMED | SUPERSEDED in current diagram by U07/R93: LLM results now pass through Signal Resolution. Retained only as P05 source history; not an active bypass. |
| R83 | C53 | C13 | UI manages signal catalog; no API or database chosen | Logical management relationship; protocol unspecified unless stated | M05.1,M05.5 | CONFIRMED | See component qualification |
| R84 | C56 | C68 | Ingestor owns session management responsibility | Logical containment relationship; protocol unspecified unless stated | M05.2,M05.4 | CONFIRMED | See component qualification |
| R85 | C56 | C69 | Ingestor owns segmentation/buffering responsibility | Logical containment relationship; protocol unspecified unless stated | M05.2,M05.4 | CONFIRMED | See component qualification |
| R86 | C56 | C05 | Ingestor owns normalization responsibility; exact rules unknown | Logical containment relationship; protocol unspecified unless stated | M05.2,M05.4 | CONFIRMED | See component qualification |
| R87 | C59 | C54 | Before detection, determine which catalog signals apply to the call | Logical logical responsibility relationship; protocol unspecified unless stated | M04.3,M05.3 | CONFIRMED | See component qualification |
| R88 | C52 | C13 | Unified signal definitions are maintained in the catalog | Logical definition relationship; protocol unspecified unless stated | M05.5 | CONFIRMED | See component qualification |
| R89 | C59 | C21 | Detection produces evidence for source-documented resolution; method-specific merge/wait semantics unresolved | Logical data relationship; protocol unspecified unless stated | A05,A06,P05 | CONFIRMED | See component qualification |
| R90 | C01 | C58 | Future Genesys source can use a provider adapter; not current prototype integration | Logical dependency; protocol unspecified | M05.4 | PROPOSED | See component qualification |
| R91 | C54 | C59 | Applicable catalog signals govern detector evaluation; logical ordering, not a separate service call | Logical dependency; protocol unspecified | M04.3,M05.3 | CONFIRMED | See component qualification |
| R92 | C56 | C54 | Call utterance/event and metadata context enter applicability evaluation before detection; metadata origin unspecified | Logical dependency; protocol unspecified | M04.3,M05.2 | CONFIRMED | See component qualification |
| R93 | C60 | C22 | LLM result enters common threshold-based Signal Resolution before an accepted signal is produced | Logical acceptance flow; API and scheduling unspecified | U07 | CONFIRMED | Replaces historical direct LLM-to-Detected-Signal path R82 in the current baseline |
