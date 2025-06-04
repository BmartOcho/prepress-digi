import os
import subprocess

def run_illustrator_script_with_file(ai_file_path):
    jsx_template_path = os.path.join("Scripts", "run_this.jsx")
    temp_script_path = os.path.join("Scripts", "temp_run.jsx")

    # Load and inject AI file path
    with open(jsx_template_path, "r") as file:
        jsx_code = file.read()

    jsx_code = jsx_code.replace("[[FILE_PATH]]", ai_file_path.replace("\\", "\\\\"))

    # Save to temp_run.jsx
    with open(temp_script_path, "w") as file:
        file.write(jsx_code)

    # Use ExtendScript Toolkit or Visual Studio Code ExtendScript Runner
    # This path is for the legacy ExtendScript Toolkit
    # Update this if you're using VSCode + ExtendScript Debugger
    # estk_path = r'"C:\Program Files (x86)\Adobe\ExtendScript Toolkit CC\ExtendScript Toolkit.exe"'

    try:
        subprocess.run([
            "C:\\Program Files (x86)\\Adobe\\ExtendScript Toolkit CC\\ExtendScript Toolkit.exe",
            temp_script_path
        ], check=True)

        print("Script sent to Illustrator successfully.")
    except Exception as e:
        print("Failed to send script to Illustrator:", e)
