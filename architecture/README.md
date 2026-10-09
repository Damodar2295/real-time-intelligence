# VANTAGE Intelligence — consolidated architecture v1.2

Updated 2026-10-09. M06/M07 add proposed live audio acquisition/STT and confirmed queue-before-ingestion-worker direction.  U05 explicitly lifts the earlier diagram hold. This is the completed logical design review baseline from M01–M05 and all supplied reference images; unresolved decisions remain marked. It is not production approval or verified deployment.

- [Editable layered architecture](diagrams/VANTAGE_Intelligence_Layered_Architecture.drawio)
- [Architecture preview](diagrams/VANTAGE_Intelligence_Layered_Architecture.preview.png)
- [Component inventory](component-inventory.md)
- [Relationships](integration-matrix.md)
- [Layer definitions](layer-definitions.md)
- [Requirements](requirements.md)
- [Signal catalog planning model](signal-catalog-model.md)
- [Business scenarios](scenario-register.md)
- [Decisions and conflicts](decisions.md)
- [Current open questions](open-questions.md#v12--audio-and-distributed-ingestion)
- [Source traceability](source-traceability.md)
- [Latest meeting extract](sources/meeting-007-extract.md)
- [Change history](architecture-changelog.md)
- [Current validation](validation-current.md)
- [Diagram coverage](diagram-coverage.md)
- [Validation history](validation-report.md)
- [Structured model](architecture-model.json)

CONFIRMED means source-supported, not implemented. The four A01 concerns remain; Signal Management, stores, deployment/development support and observability are shown as supporting groups. Current detection methods are deterministic, semantic and LLM. U07 requires their results to pass through shared threshold-based Signal Resolution before acceptance; threshold scope and multi-method combination remain open. The separately configured/trained classifier remains deferred. Composite signals are low priority. Schema details, entity-first processing and detector scheduling remain unresolved.

Historical extracts and model snapshots preserve earlier positions; appended current sections qualify earlier records. The old diagram is archived. Continue updating evidence and stable IDs without silently resolving disagreements.

The current diagram distinguishes the emulator as a test source. Live audio/STT are proposed capabilities. A concurrent transcript listener publishes to a buffering queue, consumed by ingestion workers. Kafka, partition counts, state ownership, retry/durability guarantees and thread model remain open. Earlier manager-review copies are historical; use the canonical diagram linked above.
