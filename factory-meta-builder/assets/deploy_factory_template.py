
import os
import sys
import json
import shutil
import subprocess
import argparse

import os
import sys
import json
import shutil
import subprocess
import argparse


def detect_agent_env():
    """Auto-detect the AI Agent environment: gemini | claude | generic."""
    env_override = os.environ.get("FACTORY_AGENT_ENV", "").lower()
    if env_override in ("gemini", "claude"):
        return env_override

    try:
        result = subprocess.run(["which", "gemini"], capture_output=True, text=True, timeout=2)
        if result.returncode == 0: return "gemini"
    except Exception: pass

    try:
        result = subprocess.run(["which", "claude"], capture_output=True, text=True, timeout=2)
        if result.returncode == 0: return "claude"
    except Exception: pass

    return "generic"


def get_target_paths(agent_env, repo_root, custom_skills=None, custom_agents=None):
    """Define where the Builder will inject skills and extensions."""
    if custom_skills and custom_agents:
        return (os.path.abspath(custom_skills), os.path.abspath(custom_agents))

    if agent_env == "gemini":
        return (os.path.expanduser("~/.gemini/skills"), os.path.expanduser("~/.gemini/extensions"))
    elif agent_env == "claude":
        return (os.path.expanduser("~/.claude/SKILLS"), os.path.join(repo_root, ".agents"))
    else:
        # Universal fallback for any environment
        return (os.path.join(repo_root, ".factory", "skills"), os.path.join(repo_root, ".factory", "agents"))


def link_item(source_path, target_path, label):
    """Safe linking mechanism for the Builder to manage dependencies."""
    if os.path.lexists(target_path):
        if os.path.islink(target_path) or os.path.isfile(target_path): os.remove(target_path)
        else: shutil.rmtree(target_path)
    
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    os.symlink(source_path, target_path, target_is_directory=True)
    print(f"   [Link] {label}: {os.path.basename(source_path)} -> {target_path}")


def setup_gemini_metadata(full_path, entry, extensions_path):
    """Ensure each component has the correct identity manifest for discovery."""
    proto_name = f"{entry}.md"
    proto_source = os.path.join(full_path, "GEMINI.md")
    proto_target = os.path.join(full_path, proto_name)
    if os.path.exists(proto_source) and not os.path.exists(proto_target):
        shutil.copy(proto_source, proto_target)

    context_file = proto_name if os.path.exists(proto_target) else "AGENTS.md"
    manifest = {"name": entry, "version": "1.0.0", "contextFileName": context_file}
    with open(os.path.join(full_path, "gemini-extension.json"), "w") as f: json.dump(manifest, f, indent=2)


def deploy():
    parser = argparse.ArgumentParser(description="Factory Builder - Instantiation & Evolution Engine")
    parser.add_argument("--env", help="Force agent environment (gemini|claude|generic)")
    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(script_dir, ".."))
    agent_env = args.env or detect_agent_env()
    skills_path, extensions_path = get_target_paths(agent_env, repo_root)

    print(f"🏭 Factory Builder (Phase 1: Instantiation)\n")
    print(f"   [Builder] Detected Environment: {agent_env.upper()}")
    print(f"   [Target] Skills -> {skills_path}")
    print(f"   [Target] Extensions -> {extensions_path}\n")

    # Standard Factory Components
    CORE_COMPONENTS = {"-factory-builder", "-orchestrator", "-expert-system", "-qa-agent", "-asset-engine"}

    for entry in sorted(os.listdir(repo_root)):
        full_path = os.path.join(repo_root, entry)
        if not os.path.isdir(full_path) or entry.startswith("."): continue

        has_skill = os.path.exists(os.path.join(full_path, "SKILL.md"))
        has_agents = os.path.exists(os.path.join(full_path, "AGENTS.md"))
        is_core = any(entry.endswith(suffix) for suffix in CORE_COMPONENTS)

        if has_agents or is_core:
            # Builder links core agents to extensions
            link_item(full_path, os.path.join(extensions_path, entry), "Agent/Ext")
            if agent_env == "gemini": setup_gemini_metadata(full_path, entry, extensions_path)
        elif has_skill:
            # Builder links expert skills to the knowledge base
            link_item(full_path, os.path.join(skills_path, entry), "Skill")

    print(f"\n🔄 Phase 1 Complete. Environment audited and synchronized.")
    print(f"✅ Next Step: Activate the Orchestrator to begin Atomic Delivery Flows.")

if __name__ == "__main__":
    deploy()
