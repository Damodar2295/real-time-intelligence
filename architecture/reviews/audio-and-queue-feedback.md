# Proposed amendment — live audio and multi-call queuing

Recorded 2026-10-09. Source: meeting-006-extract.md and U08. This is a review addendum; the current diagram, inventory/model and GitHub baseline are unchanged pending the remaining queue discussion. Items below are proposed logical responsibilities, not new approved services.

## Supported diagram changes

| Area | Proposed change | Boundary to preserve |
|---|---|---|
| Transcript Emulator | Give it distinct test-source styling and identify it as a test/simulation source | Keep the confirmed separate module/service role; do not imply removal of testing support |
| Conversation acquisition | Add live audio hook/connector receiving streaming audio from Genesys Cloud | Exact provider API, availability, protocol and deployment remain unverified |
| Transcription | Add streaming speech-to-text responsibility between audio acquisition and Interaction Streaming | No selected STT engine or promise of lower latency; physical packaging remains open |
| Interaction Streaming | Show transcripts produced by the new STT path entering existing ingestion responsibilities | Provider/source mapping into the canonical event contract is still required; do not invent a second normalization owner |
| Multiple-call handling | Make queue-based processing visible after its role is clarified | Audio queue, transcript queue and detector-work queue are different choices; do not silently choose one |

The supported target extension is: **Genesys Cloud → live audio acquisition → streaming speech-to-text → Interaction Streaming**. These are proposed logical dependencies. Whether the existing default WebSocket adapter carries STT output is not decided.

The feedback does not explicitly remove provider-produced transcripts. Preserve that earlier source direction until replacement versus coexistence is decided. Existing deterministic, semantic, LLM and shared threshold-resolution responsibilities are not changed by this feedback.

## Decisions needed before queue wiring

1. Where is the queue: before STT, after transcript normalization, after microbatch assembly, or at more than one boundary? What does a queued item contain?
2. How is call identity preserved from audio through transcript, batch, context and detected signal? What source metadata supplies speaker/channel and timestamps?
3. Is ordering required per call, and what concurrency is permitted inside one call? Queue concurrency across calls does not automatically establish safe concurrent state updates within a call.
4. What consumes the queue, who owns conversation context, and what happens on retries, duplicates, late/partial transcript revisions, worker movement or restart?
5. What buffering/backpressure and maximum queue age are acceptable for real-time relevance? No broker or delivery guarantee is selected.

A conversation-keyed transcript queue with multiple consumers is a possible design discussion, informed by A04. It is not an approved insertion into the current Ingestor-to-Detector flow.

## Live audio and demo questions

- Is access to the needed live audio stream available in the target Genesys environment? Which interface and constraints apply?
- Who owns STT, which engine is evaluated, and what streaming partial/final transcript contract is required?
- Will provider transcripts coexist as an alternate input, comparison baseline or fallback? None of these roles is selected yet.
- What do measurements show for audio acquisition, first usable transcript, finalized transcript, queue wait, detection and display latency? Include transcription quality; a faster transcript may change detection accuracy.
- What live demonstration proves the business benefit beyond emulator processing, and what acceptance criteria compare it with the current provider-transcript path?

Direct audio understanding remains an exploratory idea outside the confirmed transcript-based detection contract. Do not add it as a fourth detector or replace STT without another decision.

## Superseded placement question — M07 / v1.2

The subsequent conversation settles queue-before-ingestion-workers at a logical level. The canonical v1.2 diagram/model now incorporate this direction, proposed audio/STT, and distinct emulator styling. The earlier statement that the baseline remains unchanged describes the M06-only review stage. Payload, broker, dispatch, ordering and delivery guarantees remain open.
