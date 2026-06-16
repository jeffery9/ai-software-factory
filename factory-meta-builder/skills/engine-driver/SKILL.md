---
name: engine-driver
description: Engine driving skill for system operations with proper YAML frontmatter
version: 1.0.0
---
# Engine Driver

This skill handles the core operational engine driving for manufacturing systems.

# Blueprint Authoring Guide (L0 Generator) 📝

## 🎯 Description
This skill acts as the **Drafting Tool** for the Meta Builder. It does not build factories itself; instead, it generates high-quality FDL (Factory Definition Language) blueprints and code templates to teach L1 Builders how to construct specific types of factories.

## 🛠️ Operations
### 1. Generate Blueprint Standards
- Produces standardized `fdl-manifest.json` structures for different domains (e.g., Go, Odoo, Python).
- Ensures all generated blueprints adhere to the rules in `references/component_design_principles.md`.

### 2. Create Teaching Examples (Textbooks)
- Generates `examples/` directory content to serve as reference solutions for Builders.
- Provides "Before vs After" scenarios to demonstrate evolutionary improvements (e.g., migrating a monolith structure to micro-services).

### 3. Template Provisioning
- Supplies boilerplate code for new Builder components, ensuring they start with the correct architectural genes (SOLID, Stateless, Flow-Centric).

## ⚠️ Constraints
- **Textbook Only**: Outputs are strictly documentation and structural templates. No execution or file system modification of existing factories is allowed.
- **Consistency**: All generated blueprints must validate against `references/fdl_schema.json`.
