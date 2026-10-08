# U07 — resolution and presentation approval

Recorded 2026-10-08. Source: direct user chat after the v1.0 architecture review.

The user proposes a threshold value for signal resolution across all three detection paths, then says “now go ahead and apply above discussed changes.” This authorizes a common threshold-based acceptance stage for deterministic, semantic and LLM results and the three requested presentation changes: remove “Not Policy Manager,” remove the “Unresolved design choices” panel, and remove “LOW PRIORITY” from the Composite Signals title.

The assistant recommended thresholds per signal/method and asked whether multiple results should be accepted independently or combined. No explicit choice was received. Therefore neither one universal numeric threshold nor per-method thresholds, any-path acceptance, combined-score formula, score scale, deterministic confidence scheme, mandatory execution of all three methods or a wait policy is established.

All invoked method results pass through Signal Resolution. Removing a priority word from the diagram does not change the M05 implementation priority. The review's other proposed changes (history writer, direct activation route, etc.) remain open; this approval does not supply their missing architectural decisions.
