import subprocess
import yaml
from pathlib import Path

try:
    git_hash = subprocess.check_output(
        ["git", "rev-parse", "--short", "HEAD"],
        stderr=subprocess.DEVNULL
    ).decode().strip()
except Exception:
    git_hash = "unknown"

variables = {"git": git_hash}

Path("_variables.yml").write_text(yaml.dump(variables), encoding="utf-8")
