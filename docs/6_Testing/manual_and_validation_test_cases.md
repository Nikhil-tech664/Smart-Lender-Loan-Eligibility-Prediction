# Manual and Validation Test Cases

Manual validations ensure that edge cases, interface elements, and client-side interactions perform cleanly:

## 1. Manual Testing Matrix

| Test ID | Area | Action | Expected Output | Status |
|---|---|---|---|---|
| **MT-001** | Reset Button | Clicks "Reset Form" after viewing results. | Form resets to default values; the verdict card collapses instantly. | Pass |
| **MT-002** | Theme Toggle | Toggles the theme button. | Swaps theme layout smoothly; updates the local storage indicator. | Pass |
| **MT-003** | History Search | Types an income value into the history search field. | Filters the history list dynamically to show matching records. | Pass |
| **MT-004** | Input Limits | Submits negative numbers or zero for monthly income. | Form validation flags block the submission and display warning tooltips. | Pass |
| **MT-005** | Reuse Inputs | Clicks "Reuse Form Inputs" on a past history item. | Form fields are automatically repopulated with the selected values. | Pass |
| **MT-006** | DTI Overrides | Inputs $1,500 income with a $450k requested loan amount. | Automatic rejection triggers, displaying DTI overages. | Pass |
| **MT-007** | Export JSON | Clicks "Export JSON" on the verdict panel. | Initiates a local JSON download of the raw API response. | Pass |
