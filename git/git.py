import os
import subprocess

def git(command):
    result = subprocess.run(f"git {command}", shell=True, capture_output=True, text=True)
    return result.stdout.strip()