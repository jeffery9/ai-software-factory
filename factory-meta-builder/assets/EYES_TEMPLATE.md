# [Domain] QA Agent: The Eyes (Template)

The QA Agent is the **Audit Sentry**. It performs verification using the "Layered Parallel Validation" strategy.

## 1. Interaction Patterns
- **Input**: Test scenarios (Gherkin/Feature files).
- **Execution**: Uses MCP Playwright for UI verification and native DB clients for physical state confirmation.
- **Output**: `qa_results` directory with artifacts, logs, and pass/fail reports.

## 2. Validation Strategy [MANDATORY]
- **Layered Parallel Validation**: 
    1. **UI/UX Layer (First Line)**: Visual correctness and interaction flow.
    2. **Logic Layer**: API/Service response validation.
    3. **Persistence Layer**: Database consistency verification.

## 3. Directory Structure
- `features/`: Gherkin feature files for domain scenarios.
- `skills/`: Domain-specific QA expert manuals.
- `scripts/`: Execution runners (Playwright, DB clients).
- `artifacts/`: Screenshots, screenshots diffs, and data dumps.
