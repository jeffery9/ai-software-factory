# [Domain] Expert System: The Muscle (Template)

The Expert System is the **Production Engine**. It performs the physical implementation for a specific domain.

## 1. Interaction Patterns
- **Input**: Atomic technical spec (`specs.md`).
- **Action**: Generates and injects code using the Surgical Modification Protocol (SMP).
- **Self-Audit**: Runs internal linters and syntax checks before handing off.

## 2. Directory Structure
- `skills/`: Pluggable expert modules (e.g., `{language}_models`, `{framework}_views`).
- `assets/`: Code templates and boilerplates.
- `scripts/`: Deterministic implementation tools.

## 3. Core Genes [MANDATORY]
- **Surgical Modification Protocol (SMP)**: Strictly use JSON `modify` actions with `old_string`/`new_string`. Never overwrite full files unless creating new ones.
- **Test-First Mandate**: Code injection is INVALID without a corresponding, passing unit test. Tests must be generated *before* logic implementation.

## 4. Operational Standard [MANDATORY]
- **Primary Tool**: All instance operations MUST use the platform's standard CLI (e.g., `bin/dev`, `manage.py`, `cargo run`) via `{TARGET_CLI}`. Direct language imports are prohibited for runtime.
