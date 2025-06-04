import os
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
import time

ILLUSTRATOR_EXE = r'"C:\Program Files\Adobe\Adobe Illustrator 2025\Support Files\Contents\Windows\Illustrator.exe"'
SCRIPT_TEMPLATE = r"C:\Users\Benjamin\Desktop\PrePressDigi\Scripts\check_and_export.jsx"
TEMP_SCRIPT = r"C:\Users\Benjamin\AppData\Roaming\Adobe\Illustrator Script Runner\run_this.jsx"

def launch_illustrator_with_script(file_path):
    # Copy script to Illustrator’s known script folder
    os.makedirs(os.path.dirname(TEMP_SCRIPT), exist_ok=True)
    shutil.copyfile(SCRIPT_TEMPLATE, TEMP_SCRIPT)

    # Open file (which triggers the startup script)
    subprocess.run(['start', '', file_path], shell=True)

    # (Optional) Wait and delete the script to avoid running it again
    time.sleep(10)
    os.remove(TEMP_SCRIPT)

# Folder to watch
WATCH_FOLDER = r"C:\Users\Benjamin\Desktop\PrePressDigi\watch_folder"

# File type → Program map (Windows example)
PROGRAM_MAP = {
    ".ai": "Illustrator.exe",
    ".indd": "InDesign.exe",
    ".psd": "Photoshop.exe",
    ".pdf": "Acrobat.exe",
    ".png": "Photoshop.exe",  # Or use "Illustrator.exe" if needed
}

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            _, ext = os.path.splitext(file_path)
            ext = ext.lower()
            print(f"New file detected: {file_path}")

            app = PROGRAM_MAP.get(ext)
            if app:
                try:
                    print(f"Opening {file_path} with {app}")
                    subprocess.run(["start", "", file_path], shell=True)
                except Exception as e:
                    print(f"Error opening file: {e}")
            else:
                print(f"No program associated with {ext}")

if __name__ == "__main__":
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_FOLDER, recursive=False)
    observer.start()

    print(f"Watching folder: {WATCH_FOLDER}")
    try:
        while True:
            pass  # Keeps the script running
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
