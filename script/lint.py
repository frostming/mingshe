import subprocess

source_dirs = "mingshe tests"
subprocess.check_call(f"isort {source_dirs}", shell=True)
subprocess.check_call(f"black {source_dirs}", shell=True)
