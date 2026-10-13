# VANTAGE Intelligence — Architecture Guide

Status: proposed target architecture, not production approval. Package date: 13 October 2026. Platform: Lumi, the internal Google Cloud platform; GKE is the target application runtime. Accountable owners and service approvals remain to be confirmed.

## Purpose

Identify meaningful business signals during active conversations and expose accepted results with evidence and latency information. Keep live detection distinct from later contextual generation and activation.

## Processing responsibilities

1. **Sources and acquisition:** provider transcripts or the proposed live audio → speech recognition route produce transcript updates. Exact Genesys contract and coexistence policy remain open. The separate transcript emulator is a test source.
2. **Transcript ingress:** source adaptation, event framing and call/session identity. Required timestamp, speaker, partial/final and revision fields require an agreed contract.
3. **Handoff:** V4 proposes Pub/Sub before workers. The options diagram compares a shared Redis Streams alternative and a distinct colocated in-process queue prototype. Choose one implementation per test configuration; no source-specific broker, automatic fallback or dual publishing is implied.
4. **Conversation processing:** normalize updates, handle revisions/order, maintain bounded same-call context and assemble detection windows. V4 retains worker-side windowing. Ingress-side assembly is a separate option requiring a decision.
5. **Detector coordination:** choose applicable signals from call metadata and configured evaluation methods. Deterministic, semantic and LLM strategies are selective. Concurrency does not imply every method runs for every event.
6. **Semantic detection:** embedding → top-K retrieval → reranking. Models, thresholds, index lifecycle and hosting require validation.
7. **Shared resolution:** accepts evidence from invoked methods. V4's threshold-based acceptance remains the baseline; necessity/interpretation of numeric thresholds is under evaluation. Raw rule, semantic and LLM outputs are not automatically interchangeable probabilities.
8. **Output:** publish accepted signals to the workbench with evidence and freshness/latency. Persistence and consumer delivery consistency remain open. Later activation is selective.

## Multiple simultaneous calls

The worker-pool direction allows concurrency across calls. Every event, context access and output must retain the correct conversation identity. Per-call ownership, safe state mutation, ordering, duplicates and restart recovery need an executable contract and tests. The design does not require a queue or thread per call. A local queue alone does not distribute work across service instances.

## State and storage

Choose storage by responsibility: transient call context, versioned signal catalog, semantic representations and accepted decisions/evidence. Memorystore and Cloud SQL hosting remain proposed. Existing approved PostgreSQL is an alternative. Key-value storage is not an automatic replacement for vector retrieval or evidence-query needs. BigQuery is reference-only; no response-cache tier is added.

The accepted-signal history writer and visibility point are unresolved. Context is working state, not an automatically approved system of record. Freshness of an alert, context recovery and audit retention are separate policies.

## Lumi, security and operation

Confirm product availability, versions, model access, projects/regions, identity/network paths, operating owners, capacity and costs with Lumi. Runtime borders do not establish security trust zones. Approve sensitive-data handling for audio, transcripts, model requests, state and logs. No service or control is proven deployed by its diagram icon.

Measure stage and end-to-end latency, queue age, quality, errors, resource utilization and cost. No arbitrary SLO, exactly-once business guarantee, zero-latency claim or permissible input-loss policy is approved.

## Evaluation scope

Compare viable handoff options on the same source contract, workload and detector configuration. Include concurrent calls, transcript revisions, overload, restart, lost context, model/storage failures and consumer reconnect. Record differing recovery guarantees. Agree quality, freshness, capacity, recovery and cost criteria before judging results.

The [options diagram](gcp-gke-level-1/options-review/vantage-technical-level-1-options-review.drawio) provides a Level 1 comparison. It is not a detailed implementation specification or production selection.
