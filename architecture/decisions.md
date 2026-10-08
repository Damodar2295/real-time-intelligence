# Decision and conflict register — v0.1

No production deployment or final architecture approval is evidenced.

| ID | Record | Status | Evidence / consequence |
|---|---|---|---|
| D01 | Four primary concerns are documented in the proposed architecture | CONFIRMED source assertion | A01; retain exact names |
| D02 | Simple deterministic checking and deeper cognitive processing should remain separate | CONFIRMED meeting constraint | M01.7; precise runtime isolation unresolved |
| D03 | Include mini-based detection in POC methodology | CONFIRMED meeting action | M01.8; not model access, deployment or API approval |
| D04 | Reuse VANTAGE-managed signal catalog and examples | PROPOSED | M01.1; do not draw as established integration |
| D05 | Require entity extraction/cache/enrichment before detection | CONFLICTING | S01,M01.4 versus M01.7; direct bypass also depicted |
| D06 | Always parallel versus selectively invoked detection | CONFLICTING | A06 supports multiple modes; M01.8 recommends parallel threads; whether runtime or comparative POCs is unclear |
| D07 | Vector retrieval followed by classifier versus independent classifier | CONFLICTING | A05 versus A06/S02; no precedence assigned |
| D08 | BGE/cross-encoder/NLP reranking | PROPOSED | S02,M01.6; model and hot-path inclusion not settled |
| D09 | Training-data persistence and trained classifier at scale | PROPOSED | S02,M01.2; retention and training process not approved |
| D10 | Optional signal persistence | PROPOSED | A09,A10 explicitly optional |
| D11 | Latency numbers are initial POC engineering targets | CONFIRMED qualification | A07,A08; measured results and final SLA unknown |
| D12 | Use real compliance scenarios to drive validation/design | CONFIRMED meeting request | M01.5; scenario definitions missing |

## Modeling choices for this draft (not architecture decisions)

One consolidated editable page preserves the source-supported logical concerns. Supported component/data dependencies use solid arrows; catalog configuration uses dotted arrows. The disputed classifier input is omitted and annotated. The mini-based detector is shown as an explicitly requested POC addition with no invented input/output wiring. Proposed entity enrichment, reranking, catalog reuse and publication alternatives are retained in an isolated review panel and registers. No ordering/wait policy is implied by the logical layout. No approval has been requested for file creation or reversible editing.

## v0.2 — continuation (M02); records only

Earlier D01–D12 remain as history. Current qualifications below take precedence only where explicitly stated. No final architecture approval is recorded.

| ID | Record | Status | Evidence / effect on earlier records |
|---|---|---|---|
| D13 | Prioritize deterministic and semantic implementation; semantic path includes top-K plus reranker | CONFIRMED stated meeting direction | M02.1–2; advances the reranker role in D08 from proposed to source-supported POC direction. Exact BGE artifact and measured performance remain UNKNOWN; R47 resolution wiring stays PROPOSED |
| D14 | Defer separate classifier implementation during current experimentation | CONFIRMED stated meeting priority | M02.2; retain C20/C38 and their historical relationships, marked deferred. Does not permanently delete them or settle D07 sequencing |
| D15 | Scope of classifier deferral versus earlier mini-based detection action | UNKNOWN | M01.8 versus M02.2; D03 retained, not silently revoked; needs clarification |
| D16 | Entity-appending benefit/placement remains challenged | CONFLICTING | M02.3 continues D05; neither mandatory enrichment nor permanent removal confirmed |
| D17 | Remember a prior pivot signal and use a subsequent nearby pattern within the conversation | CONFIRMED scenario-level requirement | M02.4; C45/C46 describe behavior only; trigger, window and follow-on pattern unknown |
| D18 | Select and implement three or four real business detection cases to expose gaps | CONFIRMED meeting request | M02.5; selected cases and acceptance criteria UNKNOWN; D12 still applies |
| D19 | Review outreach implementation as business-case reference | CONFIRMED meeting request | M02.6; material not supplied; no new architectural integration |
| D20 | Hold all diagram/design edits while discussions continue | CONFIRMED user direction | U02; model and registers v0.2, draw.io/previews remain v0.1; final design deferred |

“Working as a classifier” describes the reranker's scoring role in discussion and does not reinstate the deferred classifier branch. Cost, key-value/single-pass explanations and classifier algorithm claims remain unverified source commentary (M02.7).

## v0.3 — M03 continuation; diagram hold retained

| ID | Record | Status | Evidence / effect |
|---|---|---|---|
| D21 | Evaluate business cases spanning linguistic/semantic, verbatim/pattern, and conditional/sequence behavior | CONFIRMED meeting direction | M03.1–3; no new architecture layers or distinct detector services implied |
| D22 | Onboard the case called “preset limit” and seek two other types | CONFIRMED meeting request | M03.1; exact label and selected case set UNKNOWN; does not establish onboarding completion or supersede D18's three/four-case target |
| D23 | Disclosure occurrence itself generates a trigger in the verbatim scenario | CONFIRMED scenario behavior | M03.2; missing-disclosure alerts and tolerance not specified |
| D24 | Use domain-associated signal/entity lists and exclude remaining checks for a call | PROPOSED | M03.5 asks whether this model fits real time; no scope assignment, provider or routing decision |
| D25 | Entity identification must be justified against actual cases | CONFIRMED question/validation direction | M03.4; D05/D16 conflict remains; no new mandatory entity stage approved |

D13/D14 (semantic + deterministic focus; separate classifier deferral), D15 (mini-based scope unknown) and D20/U02 (diagram hold) remain unchanged. The statement corrected from cognitive to semantic is captured as scenario terminology, not a change to the Contextual Generation concern.

## v0.4 — M04 continuation

| ID | Record | Status | Evidence / consequence |
|---|---|---|---|
| D26 | Organize demo work into interfacing, signal build, execution flow | CONFIRMED meeting direction | M04.1–3; workstreams/responsibilities, not replacement architecture layers |
| D27 | Limit current interface demo to WebSocket; support two or three concurrent, distinguishable calls with call-specific outcomes | CONFIRMED requirement | M04.1; completion and production capacity not established |
| D28 | Put normalization within interface responsibility | CONFIRMED responsibility assignment | M04.1; event mapping versus text cleanup and batching order unresolved |
| D29 | Define signal schema and build management-console capability | CONFIRMED request | M04.2; design/implementation absent; build versus extend/reuse VANTAGE unresolved |
| D30 | Select applicable catalog signals using call metadata before detection | CONFIRMED requirement | M04.2–3; advances applicability behavior, not all of D24's domain/entity model |
| D31 | Maintain in-memory context of earlier utterance windows and identified signals within the same conversation | CONFIRMED requirement | M04.4; C47 promoted from PROPOSED; not cross-call history or mandatory entity enrichment |
| D32 | Combine prior same-call signal and new signal to derive a third | PROPOSED | M04.4; rules and detector identity not decided |
| D33 | Meaning of the third path labeled only “signal detection” | UNKNOWN | M04.3; no classifier/LLM/sequence mapping inferred; D14/D15 unchanged |

No diagram changes. Very large scale remains an unquantified objective; generation remains later focus, not removed. Outreach remains a reference, not an integration.

## v1.0 — M05 and newly supplied planning references

| ID | Current decision/assertion | Status | Effect / source |
|---|---|---|---|
| D34 | Resume diagram work and consolidate current layered architecture | CONFIRMED user direction | U05 supersedes D20/U02 hold; not production approval |
| D35 | Current methods are deterministic, semantic and LLM-based | CONFIRMED meeting direction | M05.3; resolves unnamed third method D33/Q31; separate trained/configured classifier remains deferred; mini variant unselected |
| D36 | Ingestor owns normalization, session management and buffering/segmentation | CONFIRMED | M05.2–4/P05; specific sequencing/batching contracts open |
| D37 | Call ID serves as session/correlation ID in prototype | CONFIRMED prototype convention | M05.4; socket grouping and production uniqueness not established |
| D38 | Default WebSocket adapter now; provider adapters later | CONFIRMED direction | M05.4; future adapters PROPOSED; logical order known, packaging not fixed |
| D39 | Use Signal Management terminology; unified method-aware signal definition | CONFIRMED | M05.5; remove Policy Manager naming; regulatory/policy reference metadata still valid |
| D40 | Composite signals acknowledged but low priority | CONFIRMED scope/priority | M05.6; no executable composite rules approved |
| D41 | PostgreSQL vector instance and GKE setup are reported/planned | CONFIRMED report | M05.8; exact instance/extension and readiness unverified |
| D42 | BigQuery stores utterances/results in reference design | PROPOSED prototype choice | P05 only; no current runtime dependency silently introduced |
| D43 | One monorepo for modules and architecture; end-to-end logging/tracing | CONFIRMED requirement | M05.7,M05.9; no Git setup, CI/CD or telemetry product inferred |
| D44 | Emulator separate module versus bundled Ingestor | CONFLICTING | M05.4; shown as logical source without asserting separate deployment |
| D45 | Mandatory entity-first candidate narrowing | CONFLICTING | P03 vs M01/M02/M03 objections; dictionary metadata accepted as reference, mandatory runtime extraction not adopted |

P01/P02 planning fields and P06/P07 regulatory labels are documented source material, not approved schema or verified compliance mappings. New references omit the M02 reranker but do not explicitly withdraw it; preserve semantic top-K + reranking with unresolved LLM sequencing. Initial auth deferral is a suggestion, not a decision for live integration.

### U06 clarification

D44 emulator separation is RESOLVED: separate module/service. Adapter packaging still open. D42 remains reference-only for BigQuery, explicitly confirmed by user; R80/R81 remain PROPOSED. These clarifications supersede earlier ambiguity, not evidence of deployment.

## v1.1 — U07 approved changes

| ID | Decision | Status | Effect |
|---|---|---|---|
| D46 | All configured detection methods use common threshold-based Signal Resolution | CONFIRMED user decision | C22 accepts deterministic, semantic and LLM results; R47 confirmed and R93 replaces historical R82 bypass |
| D47 | Remove three presentation items | CONFIRMED user direction | Remove “Not Policy Manager”; remove unresolved-design panel; remove LOW PRIORITY from Composite Signals heading only |
| D48 | Threshold scope and multi-method acceptance rule | UNKNOWN | Per-method/per-signal recommendation not explicitly selected; no values, aggregation formula, any-path rule or mandatory all-method execution inferred |

M05 composite implementation priority and unaddressed review questions remain unchanged. BigQuery remains reference-only. D46 supersedes v1.0's unresolved resolver-bypass layout, not every remaining orchestration question.
