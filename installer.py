import os
import shutil
import winreg


def get_illustrator_scripts_path():
    """Attempt to locate the Illustrator Scripts folder via
    registry or fallback guess."""
    try:
        # Look for installed Illustrator version in registry
        key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Adobe\Adobe Illustrator"
        )
        version = winreg.EnumKey(key, 0)  # e.g., "25.0"
        install_path_key = winreg.OpenKey(key, version)
        install_path, _ = winreg.QueryValueEx(install_path_key, "InstallPath")
        scripts_path = os.path.join(
            install_path,
            "Presets",
            "en_US",
            "Scripts",
        )
        return scripts_path
    except Exception:
        # Fallback (update version folder if needed)
        print("Could not find Illustrator in registry, using fallback.")
        fallback = os.path.join(
            r"C:\Program Files\Adobe\Adobe Illustrator 2025\Presets\en_US",
            "Scripts",
        )
        return fallback


def install_jsx_script():
    source = os.path.join("Scripts", "run_this.jsx")
    dest_folder = get_illustrator_scripts_path()
    dest = os.path.join(dest_folder, "run_this.jsx")

    try:
        os.makedirs(dest_folder, exist_ok=True)
        shutil.copyfile(source, dest)
        print(f"Installed script to: {dest}")
    except Exception as e:
        print(f"Failed to install Illustrator script: {e}")
