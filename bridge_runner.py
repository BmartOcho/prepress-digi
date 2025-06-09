import os
import subprocess
from config import ILLUSTRATOR_EXE  # ✅ You need to import this or define it here

def run_illustrator_script_with_file(ai_file_path):
    jsx_template_path = os.path.join("Scripts", "run_this.jsx")
    temp_script_path = os.path.join("Scripts", "temp_run.jsx")

    # Load and inject AI file path
    with open(jsx_template_path, "r") as file:
        jsx_code = file.read()

    # Replace [[FILE_PATH]] with escaped path (e.g., C:\\Users\\...)
    jsx_code = jsx_code.replace("[[FILE_PATH]]", ai_file_path.replace("\\", "\\\\"))

    # Save the injected script as temp_run.jsx
    with open(temp_script_path, "w") as file:
        file.write(jsx_code)

    try:
        # Launch Illustrator and execute the generated script directly
        subprocess.run([ILLUSTRATOR_EXE, "-cmd", temp_script_path], check=True)
        print("Illustrator executed the script automatically.")
    except Exception as e:
        print("Failed to run Illustrator script:", e)
