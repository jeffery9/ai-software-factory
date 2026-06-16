# [Domain] Orchestrator: The Brain (Template)

The Orchestrator is the **Flow Controller**. It manages the state machine of the Atomic Delivery Chain and enforces continuous movement.

## 1. Interaction Patterns
- **Input**: Natural language requirement OR atomic technical spec (`specs.md`).
- **Control**: Spawns and delegates tasks to the Muscle, Eyes, and Asset Engine.
- **Decision**: Analyzes audit reports from the Eyes to decide between 'Deliver' or 'Heal Loop'.

## 2. Flow Governance [MANDATORY]
- **WIP Limit (Pull System)**: MUST enforce a Work-In-Progress limit (default = 3). Use `backlog_queue.py` for state management.
- **Event-Driven Trigger**: MUST support external triggers via `webhook_server.py` (port 8765) to integrate with CI/CD or Issue Trackers.
- **Metrics Tracking**: MUST record `Lead Time` (Start to Finish) and `Cycle Time` (Implementation Start to Audit Finish).

## 3. Double-Loop Quality Drive
- **Inner Loop (TDD)**: Direct the Muscle to write unit tests before code.
- **Outer Loop (BDD)**: Direct the Eyes to verify functional atoms against Gherkin scenarios.

## 4. Directory Structure
- `commands/`: Custom CLI commands for task management.
- `state/`: Persistent state machines and `metrics.log`.
- `references/`: SDLC loop logic, risk classification rules, and delegation protocols.
- `scripts/`: 
    - `dev_loop.sh` (The SDLC Physical Engine).
    - `webhook_server.py` (External Trigger Receiver).
    - `backlog_queue.py` (Priority Queue Manager).
