# Manager walkthrough and decisions

Based on the v1.1 logical baseline and subsequent publishing context. This is a presentation and decision agenda, not an amendment to the architecture. Timing below is approximately three minutes at a measured speaking pace, including short pauses to point at the diagram.

## Three-minute walkthrough

**0:00–0:25 — Purpose and boundaries**

“This platform identifies business signals during a live customer interaction so they can influence that interaction. Read the diagram from top to bottom, with Signal Management on the left and supporting context, storage and operations on the right. This is a logical design baseline. A named capability or arrow does not mean that its implementation or deployment is complete.”

**0:25–0:55 — Conversation input and isolation**

“The prototype starts with a separate transcript emulator producing concurrent streams. A default WebSocket adapter feeds ingestion. Ingestion manages sessions, normalizes events and buffers utterances into small batches. Call ID is the prototype session and correlation identifier. Each call needs its own context so concurrent conversations remain isolated. The context cache supplies a bounded recent window; its detailed ownership and lifecycle still need agreement.”

**0:55–1:20 — Signal configuration**

“Signal Management supplies the catalog and definitions, supported by taxonomy, examples and reference metadata. Call metadata selects applicable signals before detection. The definitions specify the detection method and relevant configuration. We have a planning model, but still need an executable schema and a consistent way to activate catalog changes and example embeddings.”

**1:20–2:00 — Detection and acceptance**

“There are three configured methods: deterministic checks, semantic retrieval with top-K candidates and reranking, and LLM-based detection. The branches describe capabilities; they do not require every method to execute for every batch. Their results go through shared threshold-based Signal Resolution. That common acceptance point is confirmed. What remains open is how thresholds relate to each method's output, how multiple results combine, and whether fast results can publish before slower methods finish.”

**2:00–2:30 — Outputs and later capabilities**

“The output area includes detected signals and the prototype event route to a workbench showing evidence and latency. Later contextual generation and activation remain distinct from LLM detection. Composite signals are also recognized, but their rules are not defined. BigQuery is a reference option, not selected storage. Observability spans the flow; the documented latency figures are engineering targets rather than measured service commitments.”

**2:30–3:00 — Decisions requested**

“The next step is to agree five things: the acceptance contract, method scheduling and timing, conversation-state ownership, configuration activation, and the business cases and success criteria for the prototype. Those decisions turn this logical view into implementation contracts. Today's layout changes do not add integrations, choose infrastructure, or settle those questions. We should leave the meeting with a named owner and next action for each.”

## Five most important unresolved decisions

Ranking is a review recommendation. No answer, owner or deadline is presumed.

| Priority | Decision to make with the manager | Why it matters | Concrete meeting outcome | Existing evidence/questions |
|---|---|---|---|---|
| 1 | **What precisely makes a signal accepted and publishable?** Is the threshold shared, per signal or per method? What does it mean for a deterministic match? If multiple methods run, is any qualifying result enough, or must a combination rule hold? How are conflicts, duplicates and revisions represented? | A common resolver is confirmed, but it does not define score comparability or acceptance. Teams otherwise implement inconsistent outcomes. | Acceptance/evidence contract, threshold scope, combination and publication-finality rules. Do not assume a weighted score or universal probability. | Q09, Q47–Q48; review F01, partially resolved by U07 |
| 2 | **When is each method invoked, and how long may it take?** One configured method, several methods, selective fallback or parallel execution? What happens on a timeout or late result? Which utterance representation reaches retrieval/reranking and LLM detection? | Controls latency, compute cost and whether slower inference delays deterministic signals. Branching alone does not settle execution. | Per-signal invocation policy, time budgets and timeout/late-result behavior; retrieval/reranker and LLM input contracts. | Q01, Q06, Q10, Q14, Q22, Q43; review F03 |
| 3 | **Who owns conversation state and its lifecycle?** Who writes accepted signals back into history, and when can the next batch see them? What closes a batch, what window expires, and what survives reconnect, replay or restart? What requires durable full-call storage? | Correct sequencing and composite detection depend on call-isolated, consistently updated history. BigQuery remains reference-only; no persistence choice is settled. | State responsibility matrix covering batching, recent context, accepted-signal history and full logs; ordering, expiry, recovery and persistence boundaries. | Q07, Q19–Q20, Q33, Q36–Q37, Q40, Q45; review F02/F08 |
| 4 | **What is an activated signal configuration?** Which schema fields are required? Who owns catalog definitions and example/index updates? Do in-flight calls retain a version? How do unknown/changing metadata and entity information affect eligibility? | The catalog, definitions and vector examples must not silently diverge. Entity dictionary metadata does not establish mandatory entity-first processing. | Versioned schema and activation contract; ownership of example embedding updates; applicability rules and live-call update behavior. | Q03, Q26–Q30, Q34–Q35, Q42, Q44; review F05/F07 |
| 5 | **What must the prototype prove before expansion?** Which three or four business cases are selected? What are the exact disclosure, sequence and omission conditions? What labeled examples, false-positive/false-negative tolerances, concurrent-call tests and latency measurements constitute success? Is a composite case in this increment? | Architecture choices need evidence from representative cases. Two or three concurrent demo calls do not establish production-scale capability. Removing the Composite Signals priority label did not change delivery priority. | Agreed scenario set and measurable acceptance scorecard, with explicit current versus later scope. | Q02, Q17–Q18, Q21, Q23–Q25, Q38; scenario register and review F08 |

## Presenter cautions

- All three methods now feed common threshold-based resolution. Do not repeat the v1.0 review's LLM-bypass finding as an outstanding defect.
- The diagram preserves existing logical connections. It still does not assign accepted-signal history write-back, explicitly show the utterance input to reranking, or establish a direct activation route that bypasses optional generation. These are contract/diagram follow-ups, not changes made in this presentation edition.
- Catalog and Definitions are not confirmed separate services. Similarly, applicability and adapter boxes do not establish separate deployment units.
- Emulator separation and BigQuery's reference-only status are answered questions, not items to reopen. GKE/PostgreSQL readiness, physical deployment and future provider integration remain unverified.
- The GitHub repository has now been created and populated with architecture artifacts. The unchanged baseline's older repository label records its earlier knowledge, not the current publishing state.
