import subprocess

def get_response(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "tinyllama"],
            input=prompt,
            capture_output=True,
            text=True
        )
        return result.stdout.strip() if result.returncode == 0 else f"Error: {result.stderr}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"
