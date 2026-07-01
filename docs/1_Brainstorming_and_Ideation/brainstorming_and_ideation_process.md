# Brainstorming and Ideation Process

## 1. Idea Prioritization Matrix
During initial project formulation, three distinct machine learning projects were evaluated against development complexity, data availability, and business value:

| Project Candidate | Complexity | Data Accessibility | Business Impact | Decision |
|---|---|---|---|---|
| **1. Fraud Detection Engine** | High | Low (Highly anonymized) | High | Rejected |
| **2. Budgeting Assistant** | Medium | Medium (Requires banks APIs)| Medium | Rejected |
| **3. SmartLender AI** | Medium | High (Structured tabular data)| High | **Selected** |

## 2. Selection Rationale
SmartLender AI was selected because structured lending datasets are highly standardized. The system maps clearly to the core underwriting needs of retail banks and offers immediate, measurable performance gains (reducing decision cycles from days to milliseconds).

## 3. Ideation Notes
- The team agreed on a dark navy banking theme (`#0b1329`) to establish a premium enterprise identity.
- Rule-based overrides are crucial: machine learning predictions must be backed by institutional guardrails (such as strict rejections for poor credit history) to remain compliant with banking regulations.
- Decoupled state management via local storage ensures the application remains lightweight, fast, and server-independent.
