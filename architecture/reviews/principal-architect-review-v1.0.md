# Principal Enterprise Architect review — v1.0 baseline

Reviewed 2026-10-08 against the current draw.io XML, preview, structured model, integration matrix, coverage record and supplied meeting/reference evidence. This is a separate review artifact. No baseline, renderer, inventory, decision register or diagram changes are authorized or made by this review. Recommendations below are proposals, not new decisions.

## Assessment

The architecture is a useful logical discussion baseline. It captures the main responsibilities and avoids selecting unsupported runtime products. It is not yet an implementation contract: event acceptance/publication, state ownership, method orchestration and configuration consistency remain unresolved.

The previous structural validation established editable XML and reference IDs. It did not establish that combining arrows from different reference views yields a coherent execution model. The most significant review findings are these composition gaps, not fabricated technology choices.

## Findings, ordered by architectural impact

### F01 — Different strategies have different apparent acceptance and publication paths

**Type:** cross-source composition ambiguity; high impact. **Elements:** C21–C25, C36, C60; R30–R32, R47, R82. **Evidence:** A05/A09, S02, P05, M05.3.

Deterministic → Evidence → Resolution → Detected Signal is shown. Semantic reranking → Resolution is proposed/dashed. LLM → Detected Signal is solid and bypasses the resolver. Meanwhile, Signal Events → Workbench starts at Resolution, not Detected Signal. Thus the picture supplies no directed LLM-to-Workbench publication route.

R82 is individually source-backed by P05; calling it fabricated would be incorrect. What is unsupported is treating its presence alongside the older resolver flow as a confirmed decision that LLM results bypass shared acceptance while using the same event lifecycle. The sources do not settle that.

**Manager decision:** Do all strategy results become evidence evaluated under one acceptance/publication contract, or can each strategy finalize and publish independently? Where do deduplication, conflicting evidence and late results get resolved? A common contract would simplify consistency but needs an explicit policy that does not unnecessarily delay fast deterministic results. Do not implement either option merely from this review.

### F02 — Context contains detected signals, but no component owns their write-back

**Type:** missing dependency / ownership; high impact. **Elements:** C47, C56, C59, C23, C55; R56, R63/R64, R68/R69. **Evidence:** M02.4, M04.4, M05.2, M05.6.

The cache lists recent utterances and identified signals. Only Ingestor → Cache and Cache → Detector are drawn. Ingestion can supply transcript context, but the shown flow does not explain how newly detected/accepted signals enter history. The model records prior-signal retention as a logical requirement without assigning a concrete writer.

This matters to subsequent sequence checks and composites: candidate evidence, accepted signals and published signals are not automatically interchangeable history entries.

**Manager decision:** Which component records a signal in history, at what acceptance point, and before which subsequent batch can it be observed? What call-level ordering, expiry, duplicate handling and restart behavior are required? Do not introduce a shared cache product or transaction mechanism without that decision.

### F03 — Reranker input is incomplete in the picture

**Type:** omitted source-supported dependency; high impact for implementation. **Elements:** C35/C36, R46/R55. **Evidence:** M02.1, S02.

Only Top-K candidates feed the reranker visually. The meeting and R55 explicitly require the utterance paired with candidate signal descriptions. No input contract says the candidate payload carries the utterance, so that must not be assumed.

**Proposed correction:** After approval, show a logical utterance/context input or label the reranker input explicitly as paired utterance and candidate descriptions. This does not require inventing another service. Original versus normalized/enriched utterance remains open.

### F04 — Activation appears to depend on generation despite generation being selective

**Type:** incomplete alternative flow / potentially misleading dependency. **Elements:** C23, C27–C29; R35–R37. **Evidence:** A01/A10.

Only Detected Signal → Contextual Generation → Activation → Consumers is shown. A01 makes deeper context selective and permits activation to deliver signals as well as recommendations/experiences. The POC Workbench route exists separately, but does not explain the future activation path for a signal that needs no generation.

**Manager decision:** Can an accepted signal be delivered directly, and who selects generation versus direct delivery? Clarify the intended contract before adding an alternate edge. The current path is source-backed; its implied exclusivity is not.

### F05 — Catalog and definition flows lack a consistent configuration boundary

**Type:** overlapping representations / unclear ownership. **Elements:** C13, C52–C54, C59; R62, R70, R83, R88, R91. **Evidence:** M04.2–3, M05.5, P01/P02/P05.

The UI manages the Catalog, applicability reads the Catalog, and Definitions separately configure the Detector. These can be reasonable logical representations, but the picture does not establish that they share an activated version. Definitions/schema are data contracts, not evidence of a second configuration service.

**Manager decision:** Is there one managed catalog containing versioned definitions? When do edits activate, and can an active call change versions? What is the source for runtime applicability and strategy configuration? Clarify ownership rather than assuming another datastore or publication mechanism.

### F06 — Applicability and adapter placement may be mistaken for extra services

**Type:** unclear responsibility boundary. **Elements:** C54, C56–C59; R87/R91/R92. **Evidence:** M04.3, M05.2–4.

Pre-detection metadata applicability is confirmed. Its placement as a standalone box before the Detector does not confirm a separate service. The model also records it as a Detector responsibility. Likewise, a separate Default WebSocket Adapter box establishes a logical adaptation boundary, not a separate deployment.

**Manager decision:** What is the implementation owner of applicability, and what belongs in the adapter versus Ingestor? Define responsibilities for provider DTO mapping, event normalization, session identity and batch assembly. Emulator separation is already confirmed; do not reopen it.

### F07 — Embedding population is supported as an outcome, not a fully specified workflow

**Type:** abbreviated logical connection; not inherently unsupported. **Elements:** C65 → C61, R78; C18/C19. **Evidence:** M05.8, P04/P05.

Examples/embeddings → Vector DB is supported. It does not identify the process that embeds examples, keeps corpus and query representations compatible, applies versions or handles retirement. The runtime Embedding node only states utterance embedding.

**Manager decision:** Who owns example embedding and index updates? How do catalog activation and indexed examples remain aligned? This is a missing responsibility; do not manufacture an indexing service or job technology.

### F08 — Sequence/composite behavior and current prototype scope are not executable yet

**Type:** incomplete capability contract. **Elements:** C45/C46/C55; source scenario register. **Evidence:** M02–M05.

Composite Signals is an isolated capability note, not a connected execution step. Remembering an earlier signal, detecting a required later utterance and combining two signals into a third may have different rules. They should not be silently merged into a single implemented detector. General omission examples do not establish timers or when absence becomes a violation.

**Manager decision:** Which concrete sequence/composite case, if any, is part of the first prototype? Specify antecedent, follow-on condition, observation window, output and repeat behavior. Removing a priority label from the diagram does not change the recorded delivery priority.

## Responsibilities and overlaps to clarify

| Area | Review conclusion |
|---|---|
| Signal Catalog / Signal Definitions / Signal Management UI | Likely repository-of-definitions, data contract and management interface respectively; these are proposed clarifications, not three proven services. |
| Context Cache / Context Buffer / session state / conversation history | Distinguish batch assembly, recent detection context, earlier signal history and persistent full-call log. Physical consolidation is not decided. |
| Signal Detector / deterministic-semantic-LLM strategies / Signal Resolution | Clarify orchestration, evidence production and acceptance ownership. Do not equate detector methods with separately deployed services. |
| LLM detection / Contextual Generation | Responsibilities can remain distinct: decide whether a signal exists versus produce later contextual output. No need to remove either merely because both might use an LLM. Shared runtime is unconfirmed. |
| Signal Evidence / Detected Signal / Signal Events | Distinguish candidate evidence, accepted result and publication envelope. These are logical artifacts unless service ownership is explicitly assigned. |
| Workbench / Signal Management UI | One displays real-time evidence/latency, the other manages definitions and is also described as viewing signals. Whether they are one frontend is unresolved. |
| Entity Dictionary / entity rules / entity-first extraction | Configured vocabulary, deterministic conditions and disputed mandatory preprocessing are different roles. Dictionary presence does not settle the extraction dispute. |
| GKE / monorepo / observability | Runtime environment, development organization and cross-cutting capability are different abstractions. Current supporting placement is preferable to calling them processing layers. |

## Connections that should retain their qualifications

- BigQuery write arrows are correctly reference-only per U06. Do not promote them to the prototype storage decision.
- Reranker → Resolution is visibly proposed. A dash does not make it confirmed; acceptance routing is still F01.
- Future provider adapters are appropriately marked future. Their missing ingestion attachment is not evidence that a provider integration is established.
- Call ID as session/correlation ID is a prototype convention, not proof of global uniqueness, single-socket ownership or replay semantics.
- PostgreSQL vector/GKE statements are reported plans, not verified readiness or a pod/database hosting map.
- A04 stream/partitions/workers remain an earlier scale reference. Their absence from the active path does not prove current large-scale capability.

## Manager discussion priorities

1. **What is the first prototype's acceptance/publication contract?** Settle F01 before implementing outputs independently by method.
2. **Who owns call state and accepted-signal history?** Settle writer, ordering and lifecycle before sequence/composite behavior.
3. **How are methods invoked?** One per signal, multiple configured methods, selective fallback or parallel evidence? Define latency/late-result policy without assuming it from fan-out lines.
4. **What exactly will demonstrate business value?** Select cases, required disclosure text, labels, false-positive/false-negative acceptance and stage latency measurements. Two/three simultaneous calls are a demo condition, not a production throughput target.
5. **What constitutes an activated signal configuration?** Agree basic schema, catalog/index versioning and how updates affect live calls.
6. **What is the actual prototype storage/deployment boundary?** BigQuery remains optional; full conversation persistence still requires a choice. Identify GKE/module ownership and future provider authentication requirements without adding infrastructure by default.

## Proposed presentation-only changes requested by the user

These are concrete pending changes, not applied to the baseline:

| Location | Proposed edit | What remains in the records |
|---|---|---|
| C53 Signal Management UI | Remove the line `Not “Policy Manager” [M05.5]`; retain Signal Management UI and its responsibilities | M05's terminology decision remains traceable. |
| `open-note` panel | Remove the entire “Unresolved design choices” panel and tidy the vacated space | Keep all decisions/questions in the supporting records. Update diagram-coverage references that currently point to this panel if approved. |
| C55 Composite Signals | Change title to `Composite Signals [M05.6]`, removing `LOW PRIORITY` | Existing low-priority implementation decision is unchanged unless explicitly revised. |

Keep the BigQuery reference-only label, future-adapter styling and proposed-edge legend. Removing a meeting discussion panel should not make unconfirmed integrations look approved. The request to remove the panel is not interpreted as removing every OPEN/TBD qualification elsewhere.

## Review limits and preservation

Read-only examination of existing architecture artifacts and source evidence. No vendor verification, implementation testing, production readiness assessment or native diagrams.net import was performed. Existing baseline files are checked for byte-for-byte preservation; only this review document is added.
