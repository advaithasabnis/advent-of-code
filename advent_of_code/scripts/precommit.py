import os
import subprocess


def run_linters():
    commands = ["poetry run isort .", "poetry run black .", "poetry run mypy ."]
    for command in commands:
        print(f"Running command: {command}")
        result = subprocess.run(command, shell=True)
        if result.returncode != 0:
            raise SystemExit(f"Command failed: {command}")
