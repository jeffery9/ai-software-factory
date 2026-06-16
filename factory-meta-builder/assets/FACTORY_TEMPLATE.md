# [Domain] AI Software Factory System Blueprint

## 1. Vision
**"Zero-Latency Atomic Delivery Flow for [Domain]."**
This factory is designed to deliver truth-verified functional atoms at AI-speed, independent of specific technology implementations.

## 2. Core Principles
- **🚀 Twin-Engine Decoupling**: Separation of Production (Build) and Audit (QA).
- **⚡️ Zero-Sprint Continuous Flow**: Requirements to Delivery reaction chain.
- **🏛️ Hierarchy of Truth [UX First]**: 
    1. **Visual/UX State** (The Final Authority): If the UX/UI breaks, the feature is broken.
    2. **Logic/Application State**: Business methods and API contracts.
    3. **Physical Persistence State**: Database state and data integrity (Lowest Validation Priority).
- **🛠️ Swappable Expert Modules**: The factory chassis supports hot-swapping tech-specific experts via the `AGENTS.md` registry.

## 3. Component Architecture & Responsibilities

### 🏗️ The Builder (The Constructor) — [name]-factory-builder
- **Responsibility**: The only component with "God-mode". It physically instantiates the environment, audits dependencies, and manages the expert registry (`AGENTS.md`).
- **Evolution**: Drives Cycle B to refactor its own structure and improve the chassis.

### 🧠 The Orchestrator (The Brain) — [name]-orchestrator
- **Responsibility**: Manages the "Factory-in-a-box" logic. Enforces WIP limits, manages the backlog queue, and triggers external webhooks.
- **Managed by**: `factory-builder` (initialized via `deploy_factory.py`).

### 💪 The Expert System (The Muscle) — [name]-expert-system
- **Responsibility**: Performs physical code injection using SMP and TDD. Contains the granular domain experts.
- **Powered by**: Loaded into the AI Agent's context via the Builder's synchronization process.

### 👁️ The Audit Sentry (The Eyes) — [name]-qa-agent
- **Responsibility**: Enforces "Layered Parallel Validation" (UX > Logic > DB). Stores forensic evidence in `qa_results/`.

## 4. Lifecycle & Evolution
- **Phase 1: Instantiation**: Run `python3 deploy_factory.py` to link all modules and validate the environment.
- **Phase 2: Production**: The Orchestrator drives daily atomic delivery flows.
- **Phase 3: Evolution**: 
    - **Cycle A**: Captures domain knowledge from production tasks.
    - **Cycle B**: The Builder evolves the factory's infrastructure to fix structural bottlenecks.
