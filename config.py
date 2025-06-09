import os

# Folder to watch
WATCH_FOLDER = r"C:\Users\Benjamin\Desktop\PrePressDigi\watch_folder"

# Path to your Illustrator script template
SCRIPT_TEMPLATE = os.path.join(os.getcwd(), "Scripts", "check_and_export.jsx")

# Location to copy script that Illustrator auto-loads
TEMP_SCRIPT = os.path.expandvars(r"%APPDATA%\Roaming\Adobe\Illustrator Script Runner\run_this.jsx")

# Adobe app you want to trigger
# Provide the raw path without surrounding quotes so ``subprocess`` can
# receive it directly.
ILLUSTRATOR_EXE = r"C:\Program Files\Adobe\Adobe Illustrator 2025\Support Files\Contents\Windows\Illustrator.exe"

# File types and apps
PROGRAM_MAP = {
    ".ai": "Illustrator",
    ".png": "Photoshop",
    ".indd": "InDesign",
    ".psd": "Photoshop",
    ".pdf": "Acrobat"
}
