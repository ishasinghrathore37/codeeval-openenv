import subprocess
import uuid
import os

def run_in_docker(code):
    file_id = uuid.uuid4().hex
    file_name = f"temp_{file_id}.py"

    with open(file_name, "w") as f:
        f.write(code)

    try:
        result = subprocess.run(
            [
                "docker", "run",
                "--rm",
                "-v", f"{os.getcwd()}:/app",
                "-w", "/app",
                "python:3.10-slim",
                "python", file_name
            ],
            capture_output=True,
            text=True,
            timeout=3
        )

        return result.stdout.strip()

    except subprocess.TimeoutExpired:
        return "Timeout"

    finally:
        if os.path.exists(file_name):
            os.remove(file_name)