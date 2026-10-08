# Architecture requirements — v0.1

- REQ01: Detect meaningful business signals during active interactions quickly enough to influence the interaction. [A01]
- REQ02: Keep simple deterministic detection separate from deeper cognitive/contextual processing; do not require unlimited call history ahead of detection. Exact orchestration remains open. [A01,A05,M01.7]
- REQ03: Route multiplexed input using conversation identity; normalize the internal event contract; use conversation-keyed stream processing. Broker, contract and lifecycle details unspecified. [A02–A04]
- REQ04: Real-time detection has bounded conversation context. Size, age and retention are unknown. [A05]
- REQ05: Add mini-based detection to POC evaluation. Model access, wiring, priority and performance remain unconfirmed. [M01.2,M01.8]
- REQ06: Validate against real compliance detection scenarios; generic cancellation examples do not define scope. Scenarios and acceptance dataset are missing from this source set. [M01.5]
- REQ07: POC scope includes interaction simulation, Genesys integration, normalization/event routing, deterministic + semantic detection, signal configuration and latency instrumentation. [A08]
- REQ08: Trace events across stages; report P50, P95 and P99, not averages alone. [A08]
- REQ09: Demonstrate live conversation → transcript received → conversation routed → deterministic detector fires → signal created → evidence displayed → latency displayed. Selective contextual reasoning → activation is eventual. [A10]

## Initial engineering targets, not measured results or production SLAs

| Stage | Target from A07 | Measurement boundaries |
|---|---|---|
| Genesys → platform ingestion | ≤50 ms | Event emitted → platform received |
| Event normalization / routing | ≤10 ms | Received → internal event |
| Context assembly | ≤10 ms | Event → detection-ready |
| Deterministic detection | ≤10 ms | Detection start → evidence complete |
| Deterministic signal resolution | ≤10 ms | Evidence → final signal |
| Internal signal publication | ≤25 ms | Signal → event published |
| Semantic embedding + retrieval | ≤150 ms | Semantic start → evidence |
| Semantic classification | ≤150 ms | Classification start → result |
| Contextual reasoning | TBD | Signal → recommendation |
| Activation / delivery | TBD | Signal → consumer |
| Deterministic signal path | Target ≤100–150 ms internal | Platform receive → signal available |
| End-to-end actionable path | TBD | Speech → agent-visible result |

The target range is preserved as written, not converted into a single SLA. No LLM or reranker latency budget is supplied. Genesys transcription and downstream experience latency need empirical measurement. Internal and end-to-end boundaries differ; do not sum these rows into an asserted SLA. [A07,A08]

## v0.2 — current POC direction and scenario requirements

Earlier requirements remain unless explicitly qualified here.

- REQ10: Current implementation emphasis is deterministic detection plus semantic retrieval/top-K/reranking; separate classifier implementation is deferred for now. Runtime parallelism versus selective execution is still unresolved. [M02.2]
- REQ11: Reranking consumes the utterance together with candidate signal descriptions. K, retained-result count, score thresholds, exact model and source of descriptions are unspecified. [M02.1]
- REQ12: The ESP scenario requires remembering a transfer-to-digital pivot within a conversation and considering a later nearby pattern in detection. Exact pivot condition, follow-on pattern, window and output definition are unknown. This does not establish an absence/timeout rule or a separate correlation service. [M02.4]
- REQ13: Select and implement three or four different real business detection cases; use the outcomes to identify missing capabilities and refine design. Selected cases, data and success criteria are not provided. [M02.5]
- REQ14: Review outreach implementation as a reference for realistic scenarios; no integration requirement follows. [M02.6]
- REQ15: Continue knowledge consolidation/brainstorming; hold diagram editing and final design until subsequent discussions permit it. [U02]

REQ05 (mini-based POC action) remains historical evidence with current priority UNKNOWN until the scope of classifier deferral is clarified. No new latency or accuracy target was supplied. Example counts (ten/fifteen candidates, three retained results) are not requirements.

## v0.3 — scenario coverage and proposed scoping

- REQ16: Use cases should exercise linguistic/semantic, verbatim/pattern and conditional/sequence detection behavior; these are not three new services or layers. [M03.1–3]
- REQ17: In the verbatim disclosure scenario, occurrence of the required wording produces a trigger. Exact wording, speaker, boundary and tolerance remain undefined. [M03.2]
- REQ18: A prior condition may require subsequent speech; define that condition and obligation from the business case before designing its evaluation. Missing-speech/timeout detection is not yet specified. [M03.3]
- REQ19: The “preset limit” case is requested for onboarding with two other types to be identified. Preserve its unclear name and do not assert a final selection or revised overall case count. [M03.1]
- PROP01: Restrict checks to signals/entities associated with a defined call domain and exclude the rest. This is an option posed for real-time applicability, not an accepted requirement. [M03.5]

See [scenario register](scenario-register.md). Entity necessity remains unresolved; defining related entities in configuration does not confirm an entity-extraction step. No new performance requirements or model selections were supplied.

## v0.4 — demo and execution requirements

- REQ20: Current interface demo uses WebSocket and handles two or three calls concurrently while distinguishing their inputs and outcomes. This is a demo requirement, not a production cap or measured result. [M04.1]
- REQ21: Interface responsibility includes normalization; exact kind and transformation/order are UNKNOWN. [M04.1]
- REQ22: Process independent microbatches with access to the same call's context. Batch boundaries, flush policy and identity contract are UNKNOWN. [M04.1,M04.3]
- REQ23: Define a signal schema and management console capability. Actual schema, workflows and build/reuse boundary are UNKNOWN. [M04.2]
- REQ24: Select the catalog signals applicable to the call using call metadata before applying detection. Metadata source, keys, predicates and reevaluation rules are UNKNOWN. Domain/entity-specific scoping PROP01 is not fully approved by this statement. [M04.2–3]
- REQ25: Keep in-memory context for earlier utterance windows and identified signals in the same conversation; window size, expiry and physical cache arrangement UNKNOWN. [M04.4]
- PROP02: Prior signal plus new signal may derive a third signal in that conversation. Combination rules, timing and lifecycle require definition. [M04.4]
- REQ26: Prioritize a scoped real-time detection demo, with expansion toward very large scale later. No numeric scale target or generation SLA is supplied. [M04.5]

## v1.0 — consolidated additions

- REQ27: Support deterministic, semantic and LLM detection selected by signal definition. LLM detection is distinct from downstream Contextual Generation; exact model remains open. [M05.3]
- REQ28: Ingestor normalizes, manages independent sessions, buffers/segments/windows input, maintains recent context and retains conversation material. Call ID is the prototype session/correlation key. Atomic mini-batch scope is not defined. [M05.2–4]
- REQ29: Provide default WebSocket adapter construct now; accommodate future provider adapters. Packaging and provider contracts open. [M05.4]
- REQ30: Signal Management UI and unified basic signal definitions across all three methods; composites low priority. [M05.5–6]
- REQ31: Configure reported PostgreSQL vector instance and populate initial embeddings; GKE environment provisioning is reported in progress; deploy modules when ready. No topology inferred. [M05.8]
- REQ32: Shared monorepo contains modules and architecture; end-to-end logging/tracing required. [M05.7,M05.9]
- PROP03: Persist utterances and detected results to BigQuery as shown in the new reference diagram; prototype adoption not confirmed. [P05]

Preserve previous latency targets as engineering targets, not SLAs. Larger conversation storage does not expand the bounded detection window to unlimited history. No authentication requirement has been removed.

## v1.1 — shared signal acceptance

- REQ33: Results from configured deterministic, semantic and LLM methods pass through common threshold-based Signal Resolution before acceptance/publication. [U07]
- Threshold values, scope, score representation and multi-result acceptance/wait behavior remain undefined. This does not require every signal to invoke all three methods.
