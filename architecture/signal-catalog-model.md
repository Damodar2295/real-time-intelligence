# Signal catalog — source-backed planning model

P01/P02 document candidate attributes; M05 requests agreement on a unified model. This is not an approved executable schema. No types, required flags, defaults, API routes, tables, enum completeness or cardinalities are invented. Example identifiers/values are examples, not live catalog records.

| Attribute | Source description | Source example |
|---|---|---|
| signal_id | Unique signal identifier | SIG-CR-001 |
| signal_name | Business-readable name | Personal Credit Impact Misrepresentation |
| description | What the signal identifies | Agent incorrectly states personal credit cannot be impacted |
| domain | Top-level classification | Credit & Credit Reporting |
| group | Signal grouping | Credit Reporting |
| detection_method | Execution strategy | SEMANTIC |
| applicable_products | Product scope | Business Card, Corporate Card (where applicable) |
| applicable_speakers | Speaker scope | AGENT |
| entity_refs | References to entity dictionary | PERSONAL_CREDIT, CREDIT_SCORE |
| detection_config | Method-specific rules or parameters | Similarity threshold, Top-K |
| requirement_refs | Approved requirements/policies (source label) | REQ-CR-001 |
| regulatory_refs | Applicable regulatory mappings (source label) | Reviewed FCRA/Reg V or other mappings |
| example_refs | Positive/negative examples | EX-001, EX-002 |
| severity | Risk priority | HIGH |
| version | Configuration version | 1.0 |
| status | Lifecycle state | DRAFT / ACTIVE / RETIRED |

M05 confirms deterministic, semantic and LLM as required method coverage. P05 associates definitions with taxonomy, dictionary, examples and regulatory/requirement mappings. `entity_refs` does not require a runtime entity-extraction stage. Similarity threshold and Top-K are method-config examples, not numeric defaults. Composite definitions are low priority; operators/window schema absent. No physical catalog store is selected.

Reference detected-result content (P05): Signal ID, Domain / Group, Evidence, Confidence, Entities, Regulatory mapping. Requiredness, score calibration and result/event lifecycle remain undefined. Mapping examples are recorded as metadata, not legal conclusions.
