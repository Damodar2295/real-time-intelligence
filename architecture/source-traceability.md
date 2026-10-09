# Source traceability — v0.1

Only the user-selected architecture and signal-pipeline images and supplied meeting were used as architecture evidence. Other images in `design&planning/` were discovered but not interpreted or incorporated in this initial scope. Image UI labels such as “Sep 29” do not establish meeting date, approval, or version precedence.

## Sources

- **A01** — `Architecture&implementationplan1.jpeg` (external input; not committed): Four primary concerns; proposed architecture; selective deeper context after a detected signal.
- **A02** — `arch2.jpeg` (external input; not committed): Genesys Cloud → Authenticate OAuth → Create Notification Channel → Subscribe to Required Topics → Genesys WebSocket → multiplexed events → demultiplex by conversation_id.
- **A03** — `arch3.jpeg` (external input; not committed): Demultiplex using conversation identifier; normalize internal transcript contract; publish to internal conversation stream.
- **A04** — `arch4.jpeg` (external input; not committed): Connector → normalization → keyed internal stream → partitions → workers → conversation context.
- **A05** — `arch5.jpeg` (external input; not committed): Bounded context; deterministic and semantic paths; embedding → vector search → classifier; signal evidence → resolution → detected signal.
- **A06** — `arch6.jpeg` (external input; not committed): Deterministic sufficient; selective semantic processing; independent evaluation when semantics inherently required; also standalone classifier path.
- **A07** — `arch7.jpeg` (external input; not committed): Initial engineering latency targets, not production SLAs.
- **A08** — `arch8.jpeg` (external input; not committed): POC scope; stage P50/P95/P99; event traceability; no final end-to-end SLA.
- **A09** — `arch9.jpeg` (external input; not committed): POC sources → connector → event mapper → context buffer; signal catalog → rule families → resolution → signal events → workbench / optional store.
- **A10** — `arch10.jpeg` (external input; not committed): Signal output and POC success criteria; eventual selective contextual reasoning → activation.
- **S01** — `signaldetectionpipeline1.jpeg` (external input; not committed): Microbuffered input → normalize → entity extraction; found: async context update; missing: cache lookup; enrich → detection. Direct normalized-to-deterministic dotted path also shown.
- **S02** — `signaldetectionpipeline2.jpeg` (external input; not committed): Semantic, classifier and deterministic branches; top-K → BGE Reranker; async training storage; combined results and classifier → resolution.
- **S03** — `signaldetectionpipeline3.jpeg` (external input; not committed): Resolution → signal detected? → yes: publish via SSE / WebSocket → downstream consumers.
- **M01** — [meeting-001-extract.md](<sources/meeting-001-extract.md>): Meeting supplied in chat; date and speakers not provided. Excerpts indexed M01.1–M01.8.

The user-supplied role brief is an external attachment and is not committed; it supplies organizational context only.

## Element assertions

| Element ID | Name or endpoints | Source statement / visible label | Interpretation | Status |
|---|---|---|---|---|
| C01 | Genesys Cloud | A02: Genesys Cloud or described function | Live conversation source | CONFIRMED |
| C02 | Transcript Emulator | A08,A09: Transcript Emulator or described function | POC interaction simulation | CONFIRMED |
| C03 | Genesys Connector | A02,A04,A09: Genesys Connector or described function | Acquire live events; source also calls this Genesys / WebSocket Connector | CONFIRMED |
| C04 | Demultiplexer | A02,A03: Demultiplexer or described function | Separate events by conversation_id | CONFIRMED |
| C05 | Normalize Transcript Event | A03,A04: Normalize Transcript Event or described function | Map events into the internal transcript contract | CONFIRMED |
| C06 | Internal Transcript Stream | A04: Internal Transcript Stream or described function | Route using interaction_id / conversation_id | CONFIRMED |
| C07 | Partition 1 / Partition 2 / Partition 3 | A04: Partition 1 / Partition 2 / Partition 3 or described function | Illustrative stream partitions; no fixed count confirmed | CONFIRMED |
| C08 | Processing Worker A / Processing Worker B / Processing Worker C | A04: Processing Worker A / Processing Worker B / Processing Worker C or described function | Process events for conversation context; count illustrative | CONFIRMED |
| C09 | Conversation Context A / Conversation Context B / Conversation Context C | A04,A05: Conversation Context A / Conversation Context B / Conversation Context C or described function | Provide bounded context; limits unknown | CONFIRMED |
| C10 | Event Mapper | A09: Event Mapper or described function | POC event mapping; equivalence to Normalize Transcript Event unconfirmed | CONFIRMED |
| C11 | Context Buffer | A09: Context Buffer or described function | POC buffering; equivalence to worker context or microbuffer unconfirmed | CONFIRMED |
| C12 | Transcript Event / Detection Input | A05,A06: Transcript Event / Detection Input or described function | Logical input to detection | CONFIRMED |
| C13 | Signal Catalog | A09,A10,M01.1: Signal Catalog or described function | Signal configuration; provider and management ownership unresolved | CONFIRMED |
| C14 | Rules | A05,A06,A09: Rules or described function | Deterministic detection capability | CONFIRMED |
| C15 | Regex | A05,A06,A09: Regex or described function | Deterministic detection capability | CONFIRMED |
| C16 | Fuzzy | A05,A06,A09: Fuzzy or described function | Deterministic detection capability | CONFIRMED |
| C17 | Entity | A05,A06,A09: Entity or described function | Deterministic detection capability | CONFIRMED |
| C18 | Embedding | A05,A06: Embedding or described function | Embed transcript for semantic retrieval | CONFIRMED |
| C19 | Vector Search | A05,A06,M01.6: Vector Search or described function | Retrieve signal / intent candidates | CONFIRMED |
| C20 | Classifier | A05,A06,S02: Classifier or described function | Classify transcript/context; exact ordering relative to retrieval disputed | CONFIRMED |
| C21 | Signal Evidence | A05,A06: Signal Evidence or described function | Collect detection evidence; source also uses Evidence Aggregator / Merge Evidence | CONFIRMED |
| C22 | Signal Resolution | A05,A06,A09,S02: Signal Resolution or described function | Resolve detection evidence to a signal; policy unspecified | CONFIRMED |
| C23 | Detected Signal | A05: Detected Signal or described function | Logical detection output | CONFIRMED |
| C24 | Signal Events | A09,A10: Signal Events or described function | Publish signal output in POC | CONFIRMED |
| C25 | Real-Time Signal Workbench | A09,A10: Real-Time Signal Workbench or described function | POC signal display; evidence and latency visible in demonstration | CONFIRMED |
| C26 | Optional Signal Store | A09,A10: Optional Signal Store or described function | Optional signal persistence; no technology selected | PROPOSED |
| C27 | Contextual Generation | A01: Contextual Generation or described function | Selectively invoke deeper context assembly when a detected signal warrants it | CONFIRMED |
| C28 | Activation | A01,A10: Activation or described function | Deliver signal, recommendation or experience to consumers | CONFIRMED |
| C29 | Downstream Consumers | A01,S03: Downstream Consumers or described function | Receive signals or resulting experience | CONFIRMED |
| C30 | Upstream Utterance / Microbuffered Sentence | S01,M01.3: Upstream Utterance / Microbuffered Sentence or described function | POC detection input; microbuffer policy unknown | PROPOSED |
| C31 | Normalize Transcript | S01,M01.3: Normalize Transcript or described function | POC text cleanup; distinct from event-contract normalization until confirmed | PROPOSED |
| C32 | Entity / Target Keyword(s) Extraction | S01,M01.4,M01.7: Entity / Target Keyword(s) Extraction or described function | Identify configured entities; compulsory placement challenged | CONFLICTING |
| C33 | Conversation Context Cache | S01,M01.4,M01.7: Conversation Context Cache or described function | Proposed in-memory recent-entity cache; source operations Update Conversation Context Cache (Async) / Load Entity from Conversation Context Cache | PROPOSED |
| C34 | Enrich Transcript | S01,M01.4,M01.6: Enrich Transcript or described function | Append entity context before semantic similarity; efficacy unvalidated | CONFLICTING |
| C35 | Top-K Candidate Signals | S02,M01.6: Top-K Candidate Signals or described function | Intermediate semantic retrieval result; K not confirmed | PROPOSED |
| C36 | BGE Reranker | S02,M01.6: BGE Reranker or described function | Image names BGE; discussion considers cross-encoder or NLP reranking; selection unconfirmed | PROPOSED |
| C37 | Async: Store Detection Data for Classifier Training | S02,S03: Async: Store Detection Data for Classifier Training or described function | Persist detection data asynchronously for later training | PROPOSED |
| C38 | Classifier Detector / Load Configured Classifier / Signal Classification | S02,M01.2: Classifier Detector / Load Configured Classifier / Signal Classification or described function | Source pipeline classifier branch; trained classifier suggested as future option | PROPOSED |
| C39 | Deterministic Detector / Combine Results | S01,S02: Deterministic Detector / Combine Results or described function | POC wrapper and aggregation for Rule, Regex, Fuzzy, NER / Entity Rules | CONFIRMED |
| C40 | Publish Signal to SSE / WebSocket | S03: Publish Signal to SSE / WebSocket or described function | Source pipeline publication mechanism; final transport choice unknown | PROPOSED |
| C41 | VANTAGE signal management | M01.1: VANTAGE signal management or described function | Meeting reports editing signals, examples and Amex taxonomy; reuse is a proposal | PROPOSED |
| C42 | Mini-based detection mechanism | M01.2,M01.8: Mini-based detection mechanism or described function | Explicit POC action to add LLM classification; GPT 4.1 mini access attempted, availability unconfirmed | CONFIRMED |
| C43 | Few-shot example retrieval | M01.2: Few-shot example retrieval or described function | Proposed vector search to supply examples to an LLM; distinct from signal-candidate retrieval | PROPOSED |
| C44 | Latency instrumentation / Observability | A07,A08: Latency instrumentation / Observability or described function | Trace events and measure major stages at P50/P95/P99 | CONFIRMED |
| R01 | C01 → C03 | A02: Notification events; setup: Authenticate OAuth → Create Notification Channel → Subscribe to Required Topics | Directed source assertion; OAuth setup; Genesys WebSocket | CONFIRMED |
| R02 | C02 → C03 | A09: Simulated transcript input in POC source diagram | Directed source assertion; UNKNOWN | CONFIRMED |
| R03 | C03 → C04 | A02,A03: Multiplexed events for routing | Directed source assertion; conversation_id | CONFIRMED |
| R04 | C04 → C05 | A03: Routed events normalized by ingestion | Directed source assertion; UNKNOWN | CONFIRMED |
| R05 | C05 → C06 | A03,A04: Publish normalized internal transcript events | Directed source assertion; UNKNOWN | CONFIRMED |
| R06 | C06 → C07 | A04: Keyed events to illustrative partitions | Directed source assertion; interaction_id / conversation_id; broker UNKNOWN | CONFIRMED |
| R07 | C07 → C08 | A04: Partition events to processing workers | Directed source assertion; UNKNOWN | CONFIRMED |
| R08 | C08 → C09 | A04: Maintain conversation context | Directed source assertion; UNKNOWN | CONFIRMED |
| R09 | C09 → C12 | A05: Bounded context accessible to detection; logical dependency, not a specified transport | Directed source assertion; UNKNOWN | CONFIRMED |
| R10 | C03 → C10 | A09: POC received events | Directed source assertion; UNKNOWN | CONFIRMED |
| R11 | C10 → C11 | A09: POC mapped events | Directed source assertion; UNKNOWN | CONFIRMED |
| R12 | C11 → C13 | A09: Arrow as drawn in POC; runtime event path versus configuration boundary unclear | Directed source assertion; UNKNOWN | CONFLICTING |
| R13 | C13 → C14 | A09,A10: Catalog supplies detection configuration (logical dependency) | Directed source assertion; UNKNOWN | CONFIRMED |
| R17 | C12 → C14 | A05,A06: Deterministic evaluation of transcript input; scheduling unspecified | Directed source assertion; UNKNOWN | CONFIRMED |
| R21 | C14 → C21 | A05: Detection evidence | Directed source assertion; UNKNOWN | CONFIRMED |
| R14 | C13 → C15 | A09,A10: Catalog supplies detection configuration (logical dependency) | Directed source assertion; UNKNOWN | CONFIRMED |
| R18 | C12 → C15 | A05,A06: Deterministic evaluation of transcript input; scheduling unspecified | Directed source assertion; UNKNOWN | CONFIRMED |
| R22 | C15 → C21 | A05: Detection evidence | Directed source assertion; UNKNOWN | CONFIRMED |
| R15 | C13 → C16 | A09,A10: Catalog supplies detection configuration (logical dependency) | Directed source assertion; UNKNOWN | CONFIRMED |
| R19 | C12 → C16 | A05,A06: Deterministic evaluation of transcript input; scheduling unspecified | Directed source assertion; UNKNOWN | CONFIRMED |
| R23 | C16 → C21 | A05: Detection evidence | Directed source assertion; UNKNOWN | CONFIRMED |
| R16 | C13 → C17 | A09,A10: Catalog supplies detection configuration (logical dependency) | Directed source assertion; UNKNOWN | CONFIRMED |
| R20 | C12 → C17 | A05,A06: Deterministic evaluation of transcript input; scheduling unspecified | Directed source assertion; UNKNOWN | CONFIRMED |
| R24 | C17 → C21 | A05: Detection evidence | Directed source assertion; UNKNOWN | CONFIRMED |
| R25 | C12 → C18 | A05,A06: Transcript for semantic embedding; applicability/scheduling unresolved | Directed source assertion; UNKNOWN | CONFIRMED |
| R26 | C18 → C19 | A05,A06: Embedding for vector retrieval | Directed source assertion; UNKNOWN | CONFIRMED |
| R27 | C19 → C20 | A05,A06,S02: Vector-search output to classifier in A05; independent classifier in A06/S02 | Directed source assertion; UNKNOWN | CONFLICTING |
| R28 | C12 → C20 | A05,A06,S02: Transcript/context directly to classifier in A06; A05 shows serial retrieval | Directed source assertion; UNKNOWN | CONFLICTING |
| R29 | C20 → C21 | A05: Classification evidence | Directed source assertion; UNKNOWN | CONFIRMED |
| R30 | C21 → C22 | A05,A06: Aggregate evidence for resolution | Directed source assertion; UNKNOWN | CONFIRMED |
| R31 | C22 → C23 | A05: Resolved signal | Directed source assertion; UNKNOWN | CONFIRMED |
| R32 | C22 → C24 | A09,A10: Signal output events | Directed source assertion; UNKNOWN | CONFIRMED |
| R33 | C24 → C25 | A09,A10: POC signal display | Directed source assertion; UNKNOWN | CONFIRMED |
| R34 | C24 → C26 | A09,A10: Optional persistence | Directed source assertion; UNKNOWN | PROPOSED |
| R35 | C23 → C27 | A01: Selective deeper context assembly when signal warrants it | Directed source assertion; UNKNOWN | CONFIRMED |
| R36 | C27 → C28 | A10: Eventual contextual reasoning → activation; interface not specified | Directed source assertion; UNKNOWN | CONFIRMED |
| R37 | C28 → C29 | A01: Signal, recommendation or experience delivery | Directed source assertion; UNKNOWN | CONFIRMED |
| R38 | C30 → C31 | S01,M01.3: Microbuffered transcript for cleanup | Directed source assertion; UNKNOWN | PROPOSED |
| R39 | C31 → C32 | S01,M01.7: Pre-detection entity extraction; placement challenged | Directed source assertion; UNKNOWN | CONFLICTING |
| R40 | C32 → C33 | S01,M01.4: Entity found: update cache asynchronously; absent: load cached entity | Directed source assertion; In-memory proposed; async update depicted | PROPOSED |
| R41 | C32 → C34 | S01,M01.4: Found entity enriches transcript | Directed source assertion; UNKNOWN | PROPOSED |
| R42 | C33 → C34 | S01,M01.4: Cached entity enriches transcript when entity absent | Directed source assertion; UNKNOWN | PROPOSED |
| R43 | C34 → C12 | S01,M01.7: Enrichment as shared upstream detection dependency is challenged | Directed source assertion; UNKNOWN | CONFLICTING |
| R44 | C31 → C39 | S01,M01.3: Direct deterministic bypass shown as dotted line; relation to second ingress unresolved | Directed source assertion; UNKNOWN | CONFLICTING |
| R45 | C19 → C35 | S02,M01.6: Top-K semantic candidates; 500 and ten in meeting are examples | Directed source assertion; UNKNOWN | PROPOSED |
| R46 | C35 → C36 | S02,M01.6: Candidate reranking | Directed source assertion; UNKNOWN | PROPOSED |
| R47 | C36 → C22 | S02: Reranker results to resolution | Directed source assertion; UNKNOWN | PROPOSED |
| R48 | C36 → C37 | S02,S03: Async training-data storage | Directed source assertion; UNKNOWN | PROPOSED |
| R49 | C38 → C22 | S02: Classifier results to resolution | Directed source assertion; UNKNOWN | PROPOSED |
| R50 | C39 → C22 | S02: Combined deterministic results to resolution | Directed source assertion; UNKNOWN | CONFIRMED |
| R51 | C22 → C40 | S03: Signal Detected? Yes branch | Directed source assertion; SSE / WebSocket alternatives | PROPOSED |
| R52 | C40 → C29 | S03: Publish detected signal | Directed source assertion; SSE / WebSocket alternatives | PROPOSED |
| R53 | C41 → C13 | M01.1: Reuse VANTAGE-managed signals as catalog; integration undecided | Directed source assertion; UNKNOWN | PROPOSED |
| R54 | C43 → C42 | M01.2: Retrieve examples and pass to LLM | Directed source assertion; Vector search proposed; API unknown | PROPOSED |

## v0.2 — M02 / U02 delta

[M02 architecture extract](sources/meeting-002-extract.md) distinguishes meeting evidence from the user’s diagram hold instruction U02. Earlier rows above are the v0.1 record; the following rows describe changes.

| Element | Evidence / source statement | Interpretation and current status |
|---|---|---|
| C18 — Embedding | A05,A06,M02.2 | CONFIRMED: Embed transcript for semantic retrieval; Current POC focus stated in M02.2; execution schedule and implementation completion UNKNOWN |
| C19 — Vector Search | A05,A06,M01.6,M02.2,M02.1 | CONFIRMED: Retrieve top-K signal candidates using separate embeddings/cosine similarity as described in the meeting; model and reference corpus details unconfirmed; Current POC focus stated in M02.2; execution schedule and implementation completion UNKNOWN |
| C20 — Classifier | A05,A06,S02,M02.2 | CONFIRMED: Classify transcript/context; exact ordering relative to retrieval disputed; Deferred for current experimentation per M02.2; not permanently removed |
| C32 — Entity / Target Keyword(s) Extraction | S01,M01.4,M01.7,M02.3 | CONFLICTING: Identify configured entities; compulsory placement challenged; Entity-appending proposal remains challenged; no approved required preprocessing |
| C33 — Conversation Context Cache | S01,M01.4,M01.7,M02.3 | PROPOSED: Proposed in-memory recent-entity cache; source operations Update Conversation Context Cache (Async) / Load Entity from Conversation Context Cache; Entity-appending proposal remains challenged; no approved required preprocessing |
| C34 — Enrich Transcript | S01,M01.4,M01.6,M02.3 | CONFLICTING: Append entity context before semantic similarity; efficacy unvalidated; Entity-appending proposal remains challenged; no approved required preprocessing |
| C35 — Top-K Candidate Signals | S02,M01.6,M02.1,M02.2 | CONFIRMED: Top-K candidate stage explicitly included in current semantic-path direction; K remains UNKNOWN; ten/fifteen candidates and top three reranked results are examples;  |
| C36 — BGE Reranker | S02,M01.6,M02.1,M02.2 | CONFIRMED: Reranker role explicitly included after top-K in semantic path; meeting describes joint utterance–signal-description scoring. Existing BGE label retained from S02; exact BGE variant/version and validated performance UNKNOWN; Current semantic-path focus; CONFIRMED applies to reranking role, not a selected model artifact or measured quality |
| C37 — Async: Store Detection Data for Classifier Training | S02,S03 | PROPOSED: Persist detection data asynchronously for later training; UNKNOWN: classifier deferral does not explicitly decide training-data storage |
| C38 — Classifier Detector / Load Configured Classifier / Signal Classification | S02,M01.2,M02.2 | PROPOSED: Source pipeline classifier branch; trained classifier suggested as future option; Deferred for current experimentation per M02.2; not permanently removed |
| C39 — Deterministic Detector / Combine Results | S01,S02,M02.2 | CONFIRMED: POC wrapper and aggregation for Rule, Regex, Fuzzy, NER / Entity Rules; Current POC focus stated in M02.2; execution schedule and implementation completion UNKNOWN |
| C42 — Mini-based detection mechanism | M01.2,M01.8,M02.2 | CONFIRMED: Explicit POC action to add LLM classification; GPT 4.1 mini access attempted, availability unconfirmed; UNKNOWN: earlier explicit mini-based POC action retained; whether M02.2 classifier deferral includes it is unresolved |
| C45 — Conversation signal history (descriptive capability) | M02.4 | CONFIRMED: Remember that a pivot signal has already occurred in the same call for subsequent detection; required behavior in the ESP example, not a new approved store/service; Business-scenario requirement; realization UNKNOWN |
| C46 — Sequence-dependent detection (descriptive capability) | M02.4 | CONFIRMED: Detect from a prior transfer-to-digital pivot plus another pattern in its near vicinity; precise second event and timing semantics not supplied; Business-scenario requirement; realization UNKNOWN |
| C47 — memory caching (meeting wording) | M02.3,M02.4 | PROPOSED: Proposed caching of utterances and/or detection outcomes; wording does not settle stored content; not equated with C33 entity cache or C45 signal history; Option discussed; no cache product, service, retention or wiring selected |
| R27 — C19 → C20 | A05,A06,S02,M02.2: Vector-search output to classifier in A05; independent classifier in A06/S02 | CONFLICTING; Earlier reference relationship retained; classifier implementation deferred per M02.2; no active POC classifier wiring newly approved |
| R28 — C12 → C20 | A05,A06,S02,M02.2: Transcript/context directly to classifier in A06; A05 shows serial retrieval | CONFLICTING; Earlier reference relationship retained; classifier implementation deferred per M02.2; no active POC classifier wiring newly approved |
| R29 — C20 → C21 | A05,M02.2: Classification evidence | CONFIRMED; Earlier reference relationship retained; classifier implementation deferred per M02.2; no active POC classifier wiring newly approved |
| R39 — C31 → C32 | S01,M01.7,M02.3: Pre-detection entity extraction; placement challenged | CONFLICTING; Entity-appending approach remains challenged; benefit and mandatory placement unconfirmed |
| R41 — C32 → C34 | S01,M01.4,M02.3: Found entity enriches transcript | PROPOSED; Entity-appending approach remains challenged; benefit and mandatory placement unconfirmed |
| R42 — C33 → C34 | S01,M01.4,M02.3: Cached entity enriches transcript when entity absent | PROPOSED; Entity-appending approach remains challenged; benefit and mandatory placement unconfirmed |
| R43 — C34 → C12 | S01,M01.7,M02.3: Enrichment as shared upstream detection dependency is challenged | CONFLICTING; Entity-appending approach remains challenged; benefit and mandatory placement unconfirmed |
| R45 — C19 → C35 | S02,M01.6,M02.1,M02.2: Vector retrieval produces top-K candidate signals in the current semantic-path direction; K UNKNOWN | CONFIRMED; UNKNOWN |
| R46 — C35 → C36 | S02,M01.6,M02.1,M02.2: Top-K candidates supply signal descriptions for reranking against the utterance; retained count UNKNOWN | CONFIRMED; Joint utterance–candidate description scoring described in meeting; model version and API UNKNOWN |
| R49 — C38 → C22 | S02,M02.2: Classifier results to resolution | PROPOSED; Earlier reference relationship retained; classifier implementation deferred per M02.2; no active POC classifier wiring newly approved |
| R55 — C12 → C36 | M02.1: Utterance is paired with each candidate signal description for reranker evaluation; representation/preprocessing unresolved | CONFIRMED; Logical input dependency only; no direct network call or bypass implied |
| R56 — C23 → C45 | M02.4: Remember occurrence of the pivot signal for that conversation; exact pivot trigger unresolved | CONFIRMED; Functional state requirement; persistence, API and implementation UNKNOWN |
| R57 — C45 → C46 | M02.4: Earlier pivot occurrence contributes to detection with a later pattern in the same conversation | CONFIRMED; Logical dependency; near-vicinity definition and evaluation owner UNKNOWN |
| U02 | User says not to modify/design the architecture diagram now | Draw.io and previews frozen at v0.1; records only updated |

## v0.3 — M03 delta

Source: [Meeting 003 extract](sources/meeting-003-extract.md). [Scenario register](scenario-register.md) retains unclear business terms without normalization. Earlier traceability rows remain historical evidence.

| Element | Source statement / evidence | Interpretation / status |
|---|---|---|
| C13 | M03.5: domains and related entities discussed for signals | Catalog ownership of this metadata UNKNOWN; existing catalog confirmation unchanged |
| C17 / C32 | M03.4: why entity identification is needed should be established through cases | Existing Entity rules remain documented; mandatory extraction still CONFLICTING |
| C46 | M03.3: because an occurrence happened, something else must be said | CONFIRMED scenario-level requirement; generic conditional example not equated with ESP events |
| C48 / R58 | M03.2: disclosure said verbatim, occurrence generates trigger | CONFIRMED behavior and transcript-input dependency; implementation/output destination UNKNOWN |
| C49 / C50 / R59 | M03.5: domain-associated signals/entities checked, remaining excluded; asks if fit for real time | PROPOSED metadata and scoped-evaluation dependency; not approved filtering/integration |
| SC01 / D22 / REQ19 | M03.1: onboard preset-limit case and find two others | CONFIRMED request; exact terminology/selection UNKNOWN |
| SC02 / D23 / REQ17 | M03.2: positive disclosure occurrence trigger | CONFIRMED scenario behavior, not absence detection |
| SC03 / REQ18 | M03.3: gold context, X/Y/Z afterward | CONFIRMED category; actual trigger/text UNKNOWN |
| SC04 | M02.4: ESP pivot plus nearby pattern | Earlier scenario preserved; no new identification with SC03 |
| D21 / REQ16 | M03.1–3: semantic, verbatim/pattern, conditional behavior | CONFIRMED scenario coverage direction, no architectural layer inference |
| D24 / PROP01 | M03.5: asks if scoped-domain model fits real time | PROPOSED |
| D25 | M03.4: justify entity identification with cases | CONFIRMED question, not component approval |
| Q23–Q30 | Gaps in M03.1–5 | OPEN; no answers inferred |

## v0.4 — M04 delta

Source: [Meeting 004 extract](sources/meeting-004-extract.md). Prior rows remain historical.

| Element | Evidence | Interpretation/status |
|---|---|---|
| C04: Demultiplexer | A02,A03,M04.1,M04.2,M04.3 | CONFIRMED: Separate events by conversation_id; Call distinction reinforced by M04; exact identity fields and mapping of the interface workstream to existing Demultiplexer remain unconfirmed |
| C09: Conversation Context A / Conversation Context B / Conversation Context C | A04,A05,M04.1,M04.4 | CONFIRMED: Provide bounded context; limits unknown; M04 requires same-conversation in-memory context; physical equivalence with existing context/cache records is unresolved |
| C13: Signal Catalog | A09,A10,M01.1,M03.5,M04.1,M04.2,M04.3 | CONFIRMED: Signal configuration; provider and management ownership unresolved; Current requirement: select applicable catalog signals for each call using call metadata before detection. Domain/entity associations and provider remain unresolved |
| C30: Upstream Utterance / Microbuffered Sentence | S01,M01.3,M04.1,M04.2,M04.3 | CONFIRMED: Independent microbatches are explicitly required for the demo execution flow; existing source label retained; batch creation ownership, flush policy and boundaries UNKNOWN; Current demo requirement; not evidence that microbatching is implemented |
| C41: VANTAGE signal management | M01.1,M04.2 | PROPOSED: Meeting reports editing signals, examples and Amex taxonomy; reuse is a proposal; Earlier VANTAGE reuse proposal retained; new console build request does not establish replacement versus extension/reuse |
| C45: Conversation signal history (descriptive capability) | M02.4,M04.1,M04.4 | CONFIRMED: Remember signals identified earlier in the same conversation for later detection; no separate history store/service established; Business-scenario requirement; realization UNKNOWN |
| C47: memory caching (meeting wording) | M02.3,M02.4,M04.1,M04.4 | CONFIRMED: Maintain in-memory context from previous utterance windows of the same conversation, including signals already identified; not history across different calls; Explicit current requirement; ownership, memory topology, retention and equivalence to C09/C11/C33/C45 UNKNOWN |
| C49: Domain-scoped signal/entity evaluation (descriptive capability) | M03.5,M04.2,M04.3 | PROPOSED: Proposed restriction of call evaluation to signals/entities associated with the defined domain, excluding remaining ones; applicability to real time explicitly posed as a question; Domain/entity-specific model remains PROPOSED; M04 separately confirms call-metadata-based signal applicability (C54), not the domain ontology or entity extraction |
| C51: interfacing layer (meeting wording) | M04.1 | CONFIRMED: WebSocket-only current demo scope; handle two or three calls concurrently, distinguish calls and attribute outcomes; normalization assigned here at responsibility level, exact transformation unknown; Current meeting requirement; implementation not verified |
| C52: signal schema (meeting wording) | M04.2 | CONFIRMED: Define signal structure; schema content requested but not supplied; Current meeting requirement; implementation not verified |
| C53: management console (meeting wording) | M04.2 | CONFIRMED: Build signal-management capability as requested; relationship to VANTAGE reuse proposal not settled; Current meeting requirement; implementation not verified |
| C54: Call-metadata signal applicability selection (descriptive capability) | M04.2,M04.3 | CONFIRMED: Determine which catalog signals apply to a call based on its metadata before applying detection mechanisms; exact filter algorithm/placement unspecified; Current meeting requirement; implementation not verified |
| C55: Prior-signal plus new-signal composition (descriptive capability) | M04.4 | PROPOSED: Proposed construct combining a previous signal and a new signal in the same conversation to determine a third signal; not confirmed as the unnamed third detector path; Proposed construct; implementation and rule semantics unresolved |
| R60: C51 → C30 | M04.1,M04.3 | CONFIRMED: Distinguished per-call input proceeds to independent microbatch processing; batching ownership and exact normalization order not settled |
| R61: C47 → C12 | M04.1,M04.4 | CONFIRMED: Detection processing consults context from the same conversation for each independent microbatch; identity propagation contract UNKNOWN |
| R62: C13 → C54 | M04.2,M04.3 | CONFIRMED: Evaluate catalog signal applicability using call metadata before applying detection mechanisms; catalog provider and metadata source unspecified |
| R63: C47 → C55 | M04.4 | PROPOSED: Previously identified same-call signals provide earlier occurrence information for proposed composition |
| R64: C23 → C55 | M04.4 | PROPOSED: A new signal can be combined with a previous same-call signal to determine a third; no recursion or publication policy specified |
| D26–D33 / REQ20–REQ26 / PROP02 / Q31–Q38 | M04.1–5 as indexed in each register row | Requirements, proposals and gaps kept distinct; no runtime topology inferred |

## v1.0 — source additions and assertion delta

The earlier statement that design&planning images were not incorporated applies only to v0.1. All seven newly attached planning images are now reviewed and included.

- **M05**: [meeting-005-extract.md](<sources/meeting-005-extract.md>) — Latest implementation discussion, M05.1–M05.10; date of meeting not independently established.
- **U05**: [meeting-005-extract.md#user-direction](<sources/meeting-005-extract.md#user-direction>) — User explicitly requests consolidated/finalized layered diagram now; earlier hold lifted.
- **P01**: `signal_catalog_datamodel_planning.jpeg` (external input; not committed) — Signal Catalog Data Model Planning; Domain → Group → Signal and candidate fields.
- **P02**: `signal_ctalog_datamodelling2.jpeg` (external input; not committed) — Remaining candidate signal attributes, example refs, version and lifecycle status.
- **P03**: `design1.jpeg` (external input; not committed) — Example entity/context extraction, candidate narrowing, deterministic value checks and omission behavior.
- **P04**: `design2.jpeg` (external input; not committed) — Semantic examples/threshold retrieval and LLM review of candidate against requirement/context.
- **P05**: `design3.jpeg` (external input; not committed) — Signal Manager config, Call Ingestor, Context Cache, Signal Detector, three strategies, Vector DB, detected signal and BigQuery persistence.
- **P06**: `proposed_detection_scenario1.jpeg` (external input; not committed) — Proposed credit impact, fees/pricing, rewards/benefits scenario families and source spreadsheet names.
- **P07**: `proposed_detectionscenario2.jpeg` (external input; not committed) — Proposed spending/payment/employee features; All_NoPresetSpending Limit and transfer-to-digital source labels; taxonomy example.

| Element | Evidence | Current interpretation/status |
|---|---|---|
| C02 — Transcript Emulator | A08,A09,M05.1,M05.4 | CONFIRMED: Transcript Emulator supplies simulated call streams; extend to concurrent streams. Logical upstream role confirmed; separate deployment/module versus bundled ingestion packaging remains disputed; Current prototype source; single-stream behavior reported, concurrent extension requested; packaging CONFLICTING |
| C03 — Genesys Connector | A02,A04,A09,M05.3,M05.4 | CONFIRMED: Acquire live events; source also calls this Genesys / WebSocket Connector; Future Genesys provider integration; default WebSocket adapter first; OAuth remains source-specific reference requirement |
| C05 — Normalize Transcript Event | A03,A04,M05.2 | CONFIRMED: Map events into the internal transcript contract; Normalization responsibility explicitly in Ingestor; event mapping versus text-cleanup rules still unspecified |
| C13 — Signal Catalog | A09,A10,M01.1,M03.5,M04.1,M04.2,M04.3,M05.1,M05.5,P01,P02,P05 | CONFIRMED: Catalog of signal definitions with predefined detection method; metadata applicability retained; unified definition across deterministic, semantic and LLM methods requested; Current prototype requirement; planned attributes documented; exact schema/ownership and persistence not approved |
| C23 — Detected Signal | A05,P05 | CONFIRMED: Logical detection output;  |
| C32 — Entity / Target Keyword(s) Extraction | S01,M01.4,M01.7,M02.3,M03.4,P03,P05 | CONFLICTING: Identify configured entities; compulsory placement challenged; CONFLICTING: new reference places entity/context extraction before candidate retrieval; earlier meetings challenge mandatory entity preprocessing; no forced stage added |
| C36 — BGE Reranker | S02,M01.6,M02.1,M02.2,P04,P05,M05.3 | CONFIRMED: Reranker role explicitly included after top-K in semantic path; meeting describes joint utterance–signal-description scoring. Existing BGE label retained from S02; exact BGE variant/version and validated performance UNKNOWN; Top-K + reranker retained from M02; latest references do not show reranker or explicitly remove it. Exact model and placement relative to LLM unresolved |
| C42 — Mini-based detection mechanism | M01.2,M01.8,M02.2,M05.3 | CONFIRMED: Explicit POC action to add LLM classification; GPT 4.1 mini access attempted, availability unconfirmed; LLM detection method now explicitly in scope (C60); specific GPT 4.1 mini endpoint/access remains UNKNOWN |
| C44 — Latency instrumentation / Observability | A07,A08,M05.7 | CONFIRMED: End-to-end logging and tracing of event history and per-stage latency; preserve P50/P95/P99 requirement; Required across prototype modules; telemetry backend and instrumentation contract unspecified |
| C47 — Context Cache (earlier label: memory caching) | M02.3,M02.4,M04.1,M04.4,M05.2,P05 | CONFIRMED: Maintain recent conversation window/state and earlier identified signals in memory; Ingestor maintains context, Signal Detector consumes it. Larger conversation storage is distinct; no unlimited hot-path history requirement; Explicit current requirement; ownership, memory topology, retention and equivalence to C09/C11/C33/C45 UNKNOWN |
| C50 — Signal-domain and related-entity associations (descriptive metadata) | M03.5,P01,P02,P05 | PROPOSED: Represent the domain of a signal and its related entities in the discussed model; metadata requirement proposed for reuse, not a new store or catalog schema; Domain/group and entity_refs explicitly documented as planned catalog metadata; schema acceptance and dynamic scope policy remain unresolved |
| C51 — interfacing layer (meeting wording) | M04.1,M05.2,M05.4 | CONFIRMED: WebSocket-only current demo scope; handle two or three calls concurrently, distinguish calls and attribute outcomes; normalization assigned here at responsibility level, exact transformation unknown; Logical interface responsibility refined by named Ingestor service C56/default adapter C57; not an additional service |
| C52 — Signal Definitions / signal schema | M04.2,M05.5,P01,P02,P05 | CONFIRMED: One definition covering deterministic, semantic and LLM detection, criteria and method-specific parameters; planned catalog attributes in P01/P02; Basic unit definitions first; precise types/constraints/enums and version semantics UNKNOWN |
| C53 — Signal Management UI (earlier: management console) | M04.2,M05.1,M05.5,P05 | CONFIRMED: Manage catalog and view signals; use Signal Management terminology, not Policy Manager. P05 calls the grouping Signal Manager; Build capability requested, similar to VANTAGE; reuse/integration boundary not settled |
| C54 — Call-metadata signal applicability selection (descriptive capability) | M04.2,M04.3,M05.3,M05.5,P01,P02 | CONFIRMED: Determine which catalog signals apply to a call based on its metadata before applying detection mechanisms; exact filter algorithm/placement unspecified; Applicability before detection retained; candidate scope fields applicable_products/applicable_speakers shown in planning, exact predicate semantics UNKNOWN |
| C55 — Prior-signal plus new-signal composition (descriptive capability) | M04.4,M05.6 | CONFIRMED: Composite signal capability: two signals can lead to a third; acknowledged as a low-priority task, not a current implemented mechanism; LOW PRIORITY; basic signal definitions first. Operators/windows/recursion/output handling UNKNOWN |
| C56 — Ingestor service / Call Ingestor | M05.2,M05.4,P05 | CONFIRMED: Consume WebSocket inputs; normalize, manage independent sessions, segment/buffer/window utterances; maintain recent context and preserve larger conversation; Current logical prototype scope; implementation not verified |
| C57 — Default WebSocket adapter | M05.4 | CONFIRMED: Initial adapter construct for WebSocket input; DTO/provider abstraction requested. Logical entry ahead of ingestion processing; package may be inside Ingestor; Current logical prototype scope; implementation not verified |
| C58 — Genesys / outreach adapters | M05.4 | PROPOSED: Future provider-specific adapters to replace/connect alongside default source construct; strategy pattern suggested, not mandated; Future adapters; provider contracts/deployments not established |
| C59 — Detector service / Signal Detector | M05.1,M05.3,P05 | CONFIRMED: Use utterance/event, conversation context and signal configuration; apply configured deterministic, semantic or LLM detection; Current logical prototype scope; implementation not verified |
| C60 — LLM-based detection | M05.3,P04,P05 | CONFIRMED: Evaluate candidate against requirement and conversation context; third method explicitly in scope, separate from later Contextual Generation; Current logical prototype scope; implementation not verified |
| C61 — Vector DB — PostgreSQL / “p vector” (meeting wording) | M05.8,P04,P05 | CONFIRMED: Configure reported PostgreSQL vector instance and insert initial embeddings; reference stores signal examples/semantic representations; Technology reported; intended pgvector extension/name/version and exact “sales profit” instance require confirmation; no provisioning verified |
| C62 — “sales profit” GKE instance | M05.8 | CONFIRMED: Shared target environment discussed for module deployment; provisioning reportedly started; Reported provisioning in progress; module mapping, readiness, cluster identity and namespace unknown |
| C63 — BigQuery — Utterance & Call Log | P05 | PROPOSED: Persist utterances and detected results in reference design; Reference diagram placement only; current prototype selection, datasets and write guarantees not confirmed |
| C64 — Entity Dictionary | P02,P05 | CONFIRMED: Products, fees, benefits, credit concepts and features referenced by signal definitions; Current logical prototype scope; implementation not verified |
| C65 — Curated Examples — Positive / Negative | P02,P04,P05 | CONFIRMED: Provide signal examples for definitions and vector representations; Current logical prototype scope; implementation not verified |
| C66 — Regulatory / Policy Mappings | P01,P02,P05 | CONFIRMED: Map signal definitions to requirements/regulatory references; mapping governance unspecified; Source metadata labels only; not legal validation or a Policy Manager service |
| C67 — Signal Taxonomy — Domain → Group → Signal | P01,P05,P07 | CONFIRMED: Organize catalog definitions; Current logical prototype scope; implementation not verified |
| C68 — Session management | M05.2,M05.4 | CONFIRMED: Keep multiple interaction streams independent; use call ID as session/correlation ID for prototype; Current logical prototype scope; implementation not verified |
| C69 — Segmentation / buffering / windowing | M05.2,M05.4,P05 | CONFIRMED: Build and track utterance chunks/microbatches per call; sequencing raised as needed; Current logical prototype scope; implementation not verified |
| C70 — Common Git repository / monorepo | M05.9 | CONFIRMED: Keep modules and architecture together in one development ecosystem; Requested organization; repository provisioning/path/module directory names not supplied |
| R63 — C47 → C55 | M04.4,M05.6 | CONFIRMED: Previously identified same-call signals provide earlier occurrence information for proposed composition |
| R64 — C23 → C55 | M04.4,M05.6 | CONFIRMED: A new signal can be combined with a previous same-call signal to determine a third; no recursion or publication policy specified |
| R65 — C02 → C57 | M05.1,M05.4 | CONFIRMED: Emulator supplies transcripts to WebSocket interface; concurrency extension requested |
| R66 — C57 → C56 | M05.4 | CONFIRMED: Default adapter supplies input to ingestion processing; packaging unresolved |
| R67 — C56 → C59 | M05.1,M05.2,P05 | CONFIRMED: Utterance/event chunks to detector |
| R68 — C56 → C47 | M05.2,P05 | CONFIRMED: Maintain recent same-call conversation context |
| R69 — C47 → C59 | P05,M05.2 | CONFIRMED: Conversation context for detection |
| R70 — C52 → C59 | M05.3,M05.5,P05 | CONFIRMED: Detection method, criteria and parameters configure detector |
| R71 — C59 → C39 | M05.3,P05 | CONFIRMED: Configured deterministic evaluation |
| R72 — C59 → C18 | M05.3,P04,P05 | CONFIRMED: Semantic branch embeds utterance for vector retrieval |
| R73 — C59 → C60 | M05.3,P05 | CONFIRMED: Configured LLM evaluation |
| R74 — C65 → C52 | P05 | CONFIRMED: Positive/negative examples inform signal definitions |
| R75 — C64 → C52 | P05 | CONFIRMED: Entity references inform definitions |
| R76 — C66 → C52 | P05 | CONFIRMED: Requirement/regulatory mappings inform definitions |
| R77 — C67 → C52 | P05 | CONFIRMED: Taxonomy organizes signal definitions |
| R78 — C65 → C61 | M05.8,P05 | CONFIRMED: Examples/embeddings populate vector database; embedding generation process not fully specified |
| R79 — C19 → C61 | P04,P05 | CONFIRMED: Top-K semantic retrieval against vector representations |
| R80 — C56 → C63 | P05 | PROPOSED: Persist utterances |
| R81 — C23 → C63 | P05 | PROPOSED: Persist detected results |
| R82 — C60 → C23 | P05 | CONFIRMED: LLM strategy contributes detected-signal result; shared resolution policy unspecified |
| R83 — C53 → C13 | M05.1,M05.5 | CONFIRMED: UI manages signal catalog; no API or database chosen |
| R84 — C56 → C68 | M05.2,M05.4 | CONFIRMED: Ingestor owns session management responsibility |
| R85 — C56 → C69 | M05.2,M05.4 | CONFIRMED: Ingestor owns segmentation/buffering responsibility |
| R86 — C56 → C05 | M05.2,M05.4 | CONFIRMED: Ingestor owns normalization responsibility; exact rules unknown |
| R87 — C59 → C54 | M04.3,M05.3 | CONFIRMED: Before detection, determine which catalog signals apply to the call |
| R88 — C52 → C13 | M05.5 | CONFIRMED: Unified signal definitions are maintained in the catalog |
| R89 — C59 → C21 | A05,A06,P05 | CONFIRMED: Detection produces evidence for source-documented resolution; method-specific merge/wait semantics unresolved |

U06 explicitly confirms C02 as a separate module/service and C63/R80/R81 as reference-only BigQuery. R90 is the proposed future Genesys adapter relationship from M05.4. R91/R92 make source-stated pre-detection applicability ordering explicit (M04.3/M05.2–3), without adding a service or metadata provider.

## v1.1 — U07

[Direct user approval](sources/resolution-and-presentation-approval.md) supports C22 shared threshold acceptance, C23 accepted-result input, current R47/R31/R32, and new R93 LLM-to-resolution. R82 remains historical only. C53 label cleanup, removal of open-note and C55 heading cleanup are presentation-only. No threshold values, per-method policy or aggregation rule inferred.

## v1.2 — M06/M07

- [M06 manager audio feedback](sources/meeting-006-extract.md): C02 test role, proposed C71 live audio acquisition and C72 streaming transcription. R94–R96 express target logical data flow, not verified vendor integration.
- [M07 queue continuation](sources/meeting-007-extract.md): C73 concurrent ingress listener, C74 buffering queue, reused C08 ingestion worker pool and C56 worker responsibilities. R97–R100 replace the direct R66 adapter-to-Ingestor route. R100 is shown by containment.
- Worker A/B/N are illustrative instances of C08, not three new services or a selected replica count. Kafka and direct audio understanding are mentioned but not selected.
- R05–R08 retain earlier A04 provenance; they do not mandate another post-normalization queue.
