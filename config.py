import os
import json


CONFIG_FILE = os.getenv(
    "PDP_CONFIG_FILE",
    os.path.join(os.path.dirname(__file__), "config.json"),
)


def _load_config(path: str) -> dict:
    if os.path.exists(path):
        with open(path, "r") as fh:
            return json.load(fh)
    return {}


_CONFIG_DATA = _load_config(CONFIG_FILE)


def _get_config(key: str, default: str) -> str:
    value = os.getenv(key.upper(), _CONFIG_DATA.get(key, default))
    if isinstance(value, str):
        value = os.path.expandvars(value)
    return value


# Folder to watch
WATCH_FOLDER = _get_config(
    "watch_folder", os.path.join(os.getcwd(), "watch_folder")
)

# Path to your Illustrator script template
SCRIPT_TEMPLATE = _get_config(
    "script_template", os.path.join(os.getcwd(), "Scripts", "check_and_export.jsx")
)

# Location to copy script that Illustrator auto-loads
TEMP_SCRIPT = _get_config(
    "temp_script",
    os.path.expandvars(
        r"%APPDATA%\Roaming\Adobe\Illustrator Script Runner\run_this.jsx"
    ),
)

# Adobe app you want to trigger
ILLUSTRATOR_EXE = _get_config(
    "illustrator_exe",
    r'"C:\Program Files\Adobe\Adobe Illustrator 2025\Support Files\Contents\Windows\Illustrator.exe"',
)

# File types and apps
PROGRAM_MAP = {
    ".ai": "Illustrator",
    ".png": "Photoshop",
    ".indd": "InDesign",
    ".psd": "Photoshop",
    ".pdf": "Acrobat"
}

