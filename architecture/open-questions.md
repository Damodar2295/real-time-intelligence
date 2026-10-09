# Open questions — v0.1

All are OPEN. No owners or deadlines were supplied. The first two questions were raised in chat; no answer is presumed.

| ID | Priority | Question | Why it affects architecture | Evidence |
|---|---|---|---|---|
| Q01 | Blocking flow approval | Are deterministic, semantic and cognitive paths runtime-parallel, selectively invoked, or only parallel POC experiments? Which signals use which mode? | Scheduling, waits and resolution cannot be fixed | A06,M01.8 |
| Q02 | Blocking validation | What are the real compliance detection scenarios, signal definitions, labeled examples and acceptance criteria? | Determines detector needs and valid POC comparison | M01.5 |
| Q03 | Blocking flow approval | Is entity extraction/enrichment optional, semantic-only, or shared? Must deterministic detection bypass it? What overhead is accepted? | Protects simple millisecond path; resolves challenged POC flow | S01,M01.7 |
| Q04 | Blocking interface definition | Is Classifier an independent detector, a stage after retrieval, the mini-based LLM, or multiple alternatives? What does cognitive mean here? | Avoids conflating classifier, LLM detection and Contextual Generation | A05,A06,S02,M01.2,M01.8 |
| Q05 | Catalog boundary | Will VANTAGE own definitions, examples and Amex taxonomy? Which API exports them, with what update/version behavior? | No confirmed catalog integration | M01.1 |
| Q06 | LLM POC | Is GPT 4.1 mini access available? What endpoint, prompt inputs, few-shot corpus and output/evidence contract are approved? | Explicit action has no confirmed wiring | M01.2,M01.8 |
| Q07 | Context/input | How do Context Buffer, microbuffering, Conversation Context and entity cache relate? What windows, expiry, reset, speaker separation and missing-context behavior apply? | Their equivalence and lifecycle are unknown | A04,A05,A09,S01 |
| Q08 | Normalization | Is transcript cleanup separate from event mapping? Which words may be removed without changing compliance meaning? | Event contract normalization is not text cleanup | A03,S01,M01.3 |
| Q09 | Resolution | How are thresholds, conflicting evidence, duplicates, late results and partial results resolved? Can a fast result publish before semantic/LLM completion? | A shared resolver does not specify wait policy | A05,A06,S02 |
| Q10 | Retrieval/reranking | Which retrieval corpus, embedding, K, thresholds and reranker are selected? Is entity filtering part of the POC comparison only? | Image BGE label is not model-selection approval | S02,M01.6 |
| Q11 | Streaming | Which Genesys topics, event contract, partial/final semantics, reconnect/replay handling and stream technology are confirmed? | Documented integration is conceptual, not verified vendor implementation | A02–A04 |
| Q12 | Output boundary | How do Detected Signal, Signal Events and SSE/WebSocket publication relate to Activation? Is Workbench a POC consumer only? | Transport, deployment boundary and event schema missing | A01,A09,S03 |
| Q13 | Storage | Are optional signal storage and classifier-training storage needed? What data, retention and ownership are approved? | Two distinct optional/proposed storage purposes | A09,S02 |
| Q14 | Latency | What are measured stage distributions and the LLM/reranker budgets? How will end-to-end latency be measured? | Initial targets cannot establish feasibility or SLA | A07,A08 |
| Q15 | Baseline authority | Which source/version is approved by the architecture owner? Which POC changes are accepted? | Image dates and meeting chronology do not settle conflicting designs | All |

Until resolved, preserve source assertions and conflicting alternatives; do not silently select a design.

## v0.2 — question updates and new gaps

No final answers presumed. Q01 remains OPEN: prioritizing both paths does not settle runtime scheduling. Q02 is PARTIALLY INFORMED by the ESP sequence example; selected cases and acceptance criteria are still missing. Q03 remains OPEN: entity-appending is still challenged. Q04/Q06 are linked to Q16 below. Q07 now also covers the distinction between latest entity, utterance history and prior-signal occurrence. Q10 is PARTIALLY INFORMED: top-K plus reranking is now explicit POC direction, while model/K/thresholds remain open. Q13 remains OPEN: classifier deferral does not explicitly decide training-data storage.

| ID | Priority | Open question | Architectural significance | Source |
|---|---|---|---|---|
| Q16 | Current scope | Does “defer classifier” include the earlier mini-based LLM detector, or only the separate configured/trained classifier implementation? | Preserve earlier action without assuming cancellation | M01.8,M02.2 |
| Q17 | Scenario semantics | Is the transfer-to-digital pivot triggered by customer agreement, transfer initiation, actual transfer, or completion? What establishes it? | Defines the state that is remembered | M02.4 |
| Q18 | Scenario semantics | What exactly is the subsequent event/pattern, and what detection results? Must it occur, must its absence be detected, or is something else intended? | Absence/timeout behavior has not been stated | M02.4 |
| Q19 | Temporal scope | What does “near vicinity” mean: elapsed time, utterance distance or conversation stage? What order, expiry and repeat-occurrence rules apply? | Bounds required conversation state without choosing a mechanism | M02.4 |
| Q20 | Cache contents | Does proposed memory caching hold utterances, detector outcomes, prior signals, entity context or some subset? Is any existing context component intended to own it? | Do not conflate C33, C45 and C47 or invent a store | M02.3–4 |
| Q21 | Business validation | Which three or four cases will be selected, and which outreach materials define their triggers, examples and acceptance criteria? | Only one incomplete scenario is supplied; outreach is not an integration | M02.5–6 |
| Q22 | Reranker contract | Which utterance representation and candidate descriptions are paired? What results, thresholds and evidence reach final resolution? | Input pairing is clearer; final signal acceptance and model selection remain open | M02.1–2,S02 |

Useful next discussion topics are Q16 (POC scope) and Q17–Q19 (complete one concrete business sequence). These are recorded gaps, not a request to stop the ongoing meeting-note collection. No new design alternative is adopted here.

## v0.3 — scenario and domain-scope questions

Q02/Q21 are further informed by three scenario types and a requested initial case, but no complete selected-case definitions or acceptance criteria are supplied. Q03 stays OPEN: entity identification is still questioned. Q18 is not answered by the generic conditional-disclosure example; the ESP follow-on event remains unnamed. Q16 (mini-based scope) is unchanged.

| ID | Priority | Open question | Architectural significance | Source |
|---|---|---|---|---|
| Q23 | Case definition | What is the exact name and detection condition of the “preset limit” / “not spending limit” case? Which two other cases are selected? | Avoid substituting a known product term or inventing the case set | M03.1 |
| Q24 | Verbatim behavior | What disclosure text and speaker count as a match? Must it be in one utterance, and what normalization/transcription variation is allowed? | Defines “verbatim” without assuming exact-string, regex or fuzzy implementation; relates to transcript cleanup | M03.2 |
| Q25 | Conditional disclosure | What does “gold” mean here, what event creates the obligation, and what must be said afterward, in what order/window? Is the output satisfaction, violation, or both? | Requirement cannot yet define sequence, absence or timeout logic | M03.3 |
| Q26 | Domain scope | Is the domain model accepted for real time? Who/what assigns the domain, when, and from which data? Can one call cover multiple domains or change domain? | The described scoping is a proposal, not confirmed routing | M03.5 |
| Q27 | Eligibility behavior | What happens with an unknown or changing domain, and are any signals evaluated regardless of domain? | Specifies inclusion/exclusion behavior before applying a filter | M03.5 |
| Q28 | Metadata ownership | Where are domain–signal–entity associations defined, who owns them, and is this actually the existing Signal Catalog/VANTAGE model? | The referenced implementation and “they” are unidentified; no integration established | M03.5 |
| Q29 | Entity role | Are related entities configuration metadata, runtime conditions, semantic features, or extracted context? Which selected case needs each role? | Domain-scoped configuration does not prove the need for mandatory entity extraction | M03.4–5 |
| Q30 | Evaluation boundary | If scoping is adopted, does it select applicable detectors/signals before evaluation, constrain semantic candidates, or filter results? | Filter location and relationship to top-K/reranking/deterministic rules are unspecified | M03.5 |

Questions are retained for the continuing discussion, not treated as permission to choose a design. No urgency, owners or deadlines are inferred.

## v0.4 — updates and new questions

Q20 is PARTIALLY ANSWERED: cache purpose is now same-conversation in-memory context from earlier utterance windows and identified signals. Exact representation, ownership and lifecycle remain open; the entity cache is not declared equivalent. Q30 is PARTIALLY ANSWERED: applicable catalog signals are selected using call metadata before detection; detailed filter placement remains open. Q26/Q28 remain open for the particular domain/entity model. Q08 gains interface-level responsibility assignment, but normalization kind remains open. Q01 detector scheduling is not answered by concurrent calls. Q16 mini-based scope remains open.

| ID | Priority | Open question | Architectural significance | Source |
|---|---|---|---|---|
| Q31 | Detector identity | What exactly is the third path called only “signal detection”? | Do not infer sequence/cognitive/LLM/classifier identity or reverse classifier deferral | M04.3 |
| Q32 | Interface contract | What call identifier accompanies packets, batches, cache access and results? How does the interface map to the existing Genesys Connector/Demultiplexer? | Independent processing still needs call-correct context/outcomes; service mapping not supplied | M04.1 |
| Q33 | Microbatch behavior | What closes a microbatch, can it overlap earlier batches, and who creates it? How are late/repeated/partial utterances handled? | Batch policy/ownership is not determined by interface wording | M04.1,M04.3 |
| Q34 | Applicability metadata | Which call metadata fields and predicates determine eligible signals, where do they originate, and what happens when missing or changed? | Before-detection selection is known; selection contract and timing are not | M04.2–3 |
| Q35 | Schema/console scope | What signal fields and console operations are required? Is this new software, an extension, or reuse of VANTAGE? | New build request does not settle earlier reuse proposal or catalog publishing contract | M04.2,M01.1 |
| Q36 | Memory lifecycle | How large are utterance/signal windows, when are they updated/expired/reset, and which existing component owns them? What must survive worker movement/restart? | In-memory is confirmed; local/shared topology and durability are not | M04.4 |
| Q37 | Signal composition | Which two signals qualify, within what ordering/window, and what third signal results? How are repeats/expiry handled; can derived signals participate again? | Proposed composition has no executable rules or lifecycle | M04.4 |
| Q38 | Demo/scale validation | Which concrete simultaneous-call cases and pass criteria demonstrate correct isolated outcomes? What quantified workload defines later “very large scale”? | Avoid treating two/three demo calls as throughput evidence | M04.1,M04.5 |

These remain topics for continuing discussion; no implementation alternatives or missing answers have been selected.

## v1.0 — current resolution status and remaining blockers

**Resolved/advanced:** Q31: third method is LLM-based (M05.3). Q16: LLM detection is in current scope; the specific mini model remains unconfirmed. Q32: call ID = session/correlation ID is the prototype convention; production identity/socket contract remains open. Q35: name is Signal Management; candidate fields supplied, but build/reuse and exact schema remain open. Q08: ingestion owns normalization; precise text transformations remain open. Q23: P07 includes `All_NoPresetSpending Limit`, supporting a candidate name, but its explicit equivalence to earlier speech and selected test definition still need confirmation. Q18/Q25: P03/P04 mention omission-based checking generally; no timer or disclosure-violation rule is established.

| ID | Priority | Open question | Why unresolved | Source |
|---|---|---|---|---|
| Q39 | Module boundary | Is emulator a separately deployed/module source or bundled with ingestion? Where is adapter code packaged? | Debate lacks an unambiguous final boundary; logical role is clear | M05.4 |
| Q40 | Store selection | Is BigQuery selected for prototype utterance/result persistence, or reference only? How is full conversation stored? | Reference diagram specifies it; meeting gives no explicit approval/contract | P05,M05.2 |
| Q41 | Environment | What are the exact “sales profit” GKE/PostgreSQL instance identities and intended pgvector extension/version? What is provisioned and where do modules run? | Spoken names/readiness unverified; no deployment map | M05.8 |
| Q42 | Catalog contract | Which P01/P02 fields are required, their types/cardinalities, method config schema, supported methods per signal, version/lifecycle semantics, and persistence owner? | Planning table is not an agreed executable schema | P01,P02,M05.5 |
| Q43 | Runtime scheduling | Is LLM independent, selective after candidate retrieval, or fallback after reranking? How do resolution, thresholds, evidence and late results combine? | References show method alternatives; no orchestration contract | P04,P05,M05.3,A06 |
| Q44 | Entity-flow conflict | Does P03's entity-first candidate narrowing supersede earlier objections, apply selectively, or remain experimental? | Latest meeting does not settle mandatory extraction/enrichment | P03,M01–M03 |
| Q45 | Persistence and state | Which data is stored in recent cache versus full log, with what ordering/retention/write-failure behavior? What does atomic mini-batch execution cover? | Source gives responsibilities, not consistency boundaries | M05.2–4,P05 |
| Q46 | Authentication | Is auth deferred for emulator-only prototype, and what is required for future provider/session integration? Is the isolated “Webhook” wording intentional? | Suggestion does not define live-system security or a second transport | M05.10,A02 |

No open question is silently answered by the consolidated diagram. Earlier Q01/Q03/Q06/Q09/Q10/Q14/Q17–Q19/Q24/Q26–Q30/Q33–Q38 remain open to the extent not explicitly resolved above. Emulator packaging and BigQuery status were asked in chat while independent diagram work continued.

### U06 answers

Q39 emulator portion RESOLVED: separate module/service. Adapter packaging remains open. Q40 BigQuery choice RESOLVED for this baseline: reference-design option for now; actual prototype full-conversation persistence remains unknown. Do not treat BigQuery as chosen merely because the diagram includes it.

## v1.1 — U07 update

The resolution ownership portion of Q09/Q43 is answered: all invoked methods use common threshold-based resolution. Invocation/fallback, result timing and acceptance details remain open. The review's LLM acceptance bypass is removed.

| ID | Question | Significance |
|---|---|---|
| Q47 | Is the threshold shared, per signal, per method, or both? What values and score semantics apply, especially to deterministic matching? | No score normalization or threshold schema was chosen |
| Q48 | When multiple methods evaluate a signal, can any qualifying result establish it or must results satisfy a combination rule? When is resolution final? | No any-path, consensus, weighted aggregation or wait policy was approved |

Existing history-update ownership, reranker input representation, activation route, schema and cache-lifecycle questions remain. Removing the diagram panel does not resolve them.

## v1.2 — audio and distributed ingestion

The queue placement question raised after M06 is answered by M07: incoming event stream → buffering queue → ingestion processing workers. The logical multi-conversation producer/listener precedes the queue. Exact packaging, protocol and message contract remain open. Separate emulator and reference-only BigQuery decisions remain settled.

| ID | Open question | Why it matters |
|---|---|---|
| Q49 | Which Genesys live audio interface/access is available, with what channels, timestamps, format and connection lifecycle? | Requested audio hook is not a verified integration |
| Q50 | Which streaming STT engine/hosting and partial/final revision, speaker, timestamp and confidence contract will be used? | Determines quality, latency and canonical event mapping |
| Q51 | Do provider transcripts coexist with new STT, replace it, or serve a fallback/comparison role? | Feedback does not retire the existing source path |
| Q52 | What producer validation and event envelope precede enqueueing; what exact payload, broker, queue/topic/partition model and dispatch mechanism are chosen? | Placement is known; protocol and physical topology are not |
| Q53 | What acknowledgments, durability, producer retry, duplicate handling, replay and backpressure rules meet the input-preservation requirement? | A buffer alone does not prove no loss or exactly-once outcomes |
| Q54 | How are per-call order and context ownership maintained across workers, retries, thread concurrency, failover and scale changes? | Call ID alone does not serialize updates or provide state recovery |
| Q55 | What workload and queue-age/throughput objectives drive worker scaling; what limits or actions apply when input exceeds processing capacity? | Elasticity must not be mistaken for unlimited capacity or acceptable latency |
| Q56 | What live-audio demo and quality/latency comparison will establish business value beyond transcript emulation? | Reported upstream delay is unmeasured; faster/more accurate STT has not been established |

Existing Q33/Q36/Q38/Q45 remain relevant and now apply to distributed ingestion workers. Q47/Q48 threshold and acceptance questions are unchanged. Observe queue wait and audio/transcription time separately when evaluating the existing latency targets; those targets have not been extended into new audio-to-output SLAs.
