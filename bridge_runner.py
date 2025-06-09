import os
import subprocess
# Import the Illustrator executable path as a raw string
from config import ILLUSTRATOR_EXE

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
        # Open the file in Illustrator (so user can manually run the script via File > Scripts)
        # Pass the executable path directly without extra quoting
        subprocess.run([ILLUSTRATOR_EXE, ai_file_path], check=True)

        print("Illustrator opened the file. Run 'File > Scripts > run_this' inside Illustrator to complete automation.")
    except Exception as e:
        print("Failed to open file in Illustrator:", e)
