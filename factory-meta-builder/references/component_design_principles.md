# Factory Component Construction Protocol (v2.0)

Every operational engine (Orchestrator, Expert System, QA Agent) produced by the Meta-Builder MUST adhere to these architectural genes.

## 1. Naming & Identity
- **Kebab-Case Standard**: All directories and skill names MUST use `kebab-case`. (e.g., `web-expert-system`, NOT `Web_Expert_System`).
- **Manifest Rigor**: Every component directory MUST contain:
    - `gemini-extension.json`: The identity manifest.
    - `SKILL.md`: The execution logic (Keep < 500 lines).
    - `commands/`: Even if empty, to signal Extension status.
    - `README.md`: High-level description for human architects.

## 2. Statelessness (The Golden Rule)
- **Zero Local State**: Components MUST NOT write logs, state files, or caches into their own directory.
- **Project Redirection**: All transient data, generated code, and forensic artifacts MUST be redirected to the project workspace (`state/`, `qa_results/`).

## 3. Atomic Discovery & Dependency Injection
- **Flat Expert Structure**: Expert Systems should be designed as a collection of granular experts in a `skills/` sub-directory.
- **Registry Discovery**: Components discover their sub-skills via a local `AGENTS.md` manifest, rather than hardcoded relative paths.
- **Meta-Factory Indexing**: Every factory MUST include a `registry.json` to map available domain skills, allowing other factories to invoke its capabilities remotely or locally.

## 4. Portability & Pathing
- **Relative-First**: All internal references (links, imports, includes) MUST use relative paths.
- **Workspace Anchoring**: Components MUST use the `--workspace <relative_path>` argument to resolve the project root.

## 5. Flow-Centric Design [CRITICAL]
All components MUST be designed to support the **Pull-based Flow**:
- **Atomic Work Units**: Tasks should be granular enough to be completed in one SDLC cycle (Lead Time < 4 hours).
- **JIT Specs**: Requirement specifications (`specs.md`) must be generated ONLY when the task is pulled from the backlog.
- **Double-Loop Quality**:
    - **Outer Loop**: Expert Systems must provide Gherkin-compatible stubs.
    - **Inner Loop**: Expert Systems must support TDD (Test-First) injection.
- **UX-First Truth**: QA Agents must prioritize visual/user-interaction verification over raw data persistence.

## 6. Flow Metrics & Visibility
- **Lead Time Tracking**: The Orchestrator must timestamp the start of Requirement Ingest and the completion of Delivery.
- **Cycle Time Tracking**: The Orchestrator must timestamp the start of Implementation and the completion of Audit.
- **CFD Ready**: Metrics should be stored in a standardized `state/metrics.log` (CSV format: `timestamp,task_id,phase,duration`).
