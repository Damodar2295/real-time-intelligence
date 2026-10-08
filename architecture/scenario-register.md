# Business detection scenarios — v0.3 working register

Scenario definitions, not architecture design or test results. No examples below are complete enough to finalize detection logic. Source names with unclear transcription are preserved. Categories may overlap.

| ID | Source wording / scenario | Supported detection behavior | Status and missing definition | Source |
|---|---|---|---|---|
| SC01 | “preset limit”; later “not spending limit” | Linguistic/semantic detection; speaker requests onboarding | CONFIRMED direction; exact case name, trigger, expected signal, examples and acceptance criteria UNKNOWN; not onboarded evidence | M03.1 |
| SC02 | Disclosure “said verbatim” | Positive occurrence of required wording generates a trigger | CONFIRMED scenario behavior; exact script, speaker, matching tolerance, transcript boundaries and output UNKNOWN | M03.2 |
| SC03 | “because this happened” → must “say something else”; “gold” context → “X, y, and z” afterward | Prior condition establishes required follow-on speech | CONFIRMED category; gold meaning, condition, required wording/order/window and satisfaction-versus-violation output UNKNOWN | M03.3 |
| SC04 | ESP transfer to digital → another nearby pattern | Remember earlier pivot in the conversation and consider subsequent pattern | Earlier partial example retained; relationship to SC03 is conceptual only; not assumed to be the same selected case | M02.4 |

M03 requests onboarding one case and finding two others of distinct nature. M02 requested three or four cases. These can be compatible, but no final selected set or revised case count is confirmed. The register does not count SC03 and SC04 as distinct approved POC implementations.

## Proposed scope model (not a selected scenario)

Domain-associated signal/entity lists could restrict call evaluation to compliance or service checks and exclude others. The real-time applicability is explicitly a question. Domain source, assignment timing, multiple domains, switching, default behavior and filtering stage are unknown. [M03.5]

## Interpretation for the next discussion

The notes distinguish what is detected (meaning, exact wording, or a conditional sequence) from which configured signals are eligible for evaluation (the proposed domain scope). They also distinguish configured entities associated with a signal from extracting entities at runtime. Neither distinction selects an implementation or resolves whether entity extraction is necessary.

## M04 additions

- **Demo condition:** two or three simultaneous calls, distinct outcomes per call, independent microbatches and access to each call's own history. Not an additional business-signal type or production benchmark. [M04.1]
- **Applicability condition:** choose applicable catalog signals using call metadata before detection. The domain-specific schema remains unconfirmed. [M04.2–3]
- **Proposed generic composition:** earlier same-call signal plus new signal may produce a third. Signal identities, time/order and acceptance criteria are absent; not presumed to be the third detector path, SC03 disclosure obligation, or SC04 ESP event pair. [M04.4]

Prior-signal occurrence is a required type of cached context. This does not validate mandatory entity-appending or a particular stateful detection implementation.

## Newly supplied P03–P07 reference scenarios

| Source family | Supported reference focus | Qualification |
|---|---|---|
| Credit Reporting & Credit Impact | Statements about inquiries, business/personal credit, bureau reporting, credit-score impact | Proposed family; includes Personal Credit Impact Misrepresentation example, not accepted legal ground truth |
| Fees, APR & Card Pricing | Misstated APR/fees/charges; compare extracted values with approved product values | Product-value source unspecified; $695 and 18.49% are example utterances, not asserted current terms |
| Rewards, Benefits & Statement Credits | Reward rates, eligibility, benefits, redemption, statement credits, conditions | Proposed family; named spreadsheets not supplied as datasets |
| Spending, Payment & Employee Card Features | Spending capacity, Pay Over Time, Expanded Buying Power, employee-card and digital-transfer features | `All_NoPresetSpending Limit` and transfer-to-digital labels provide reference names, not completed rule definitions |

P03/P04 also explicitly mention omission-based detection but provide no trigger/window/completion rules. Taxonomy example: Product Terms & Pricing → Fees & Pricing → Annual Fee Misrepresentation. Regulatory domains remain source-provided associations requiring their own approval; no financial/legal claims are adopted. Reference families do not finalize the selected three/four-case POC set.
