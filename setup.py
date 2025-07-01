import subprocess
from pathlib import Path
import argparse

# basic setup for argument throug command line for local testing and development
_parser=argparse.ArgumentParser()
_parser.add_argument("--rewrite")
_parser.add_argument("--path")
_args=_parser.parse_args()

def get_requirements_path(path) -> Path:
    if path:
        requirements_path = Path(path.lower(), 'requirements.txt')
        requirements_lock_path = Path(path.lower(), 'requirements.lock')
    else: 
        requirements_path = Path('./requirements.txt')
        requirements_lock_path = Path('./requirements.lock')
    return requirements_path, requirements_lock_path

if __name__ == "__main__":

    requirements, requirements_lock = get_requirements_path(path = _args.path)

    if not (Path.exists(requirements_lock) or (lambda x: _args.rewrite.lower() if _args.rewrite.lower() else _args.rewrite) == "true"):
        if not Path.exists(requirements):
            raise FileNotFoundError(f"File {requirements} not found. Please create it first.")
        else:
            print(f"Installing from file: {requirements}", flush=True)
            subprocess.run(f"pip install -r {requirements}", shell=True, check=True)
        print("Generating requirements.lock...", flush=True)
        subprocess.run(f"pip freeze > {requirements_lock}", shell=True, check=True)
    else:
        print(f"Installing from file: {requirements_lock}", flush=True)
        subprocess.run(f"pip install -r {requirements_lock}", shell=True, check=True)
