import os
import subprocess
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from config import WATCH_FOLDER, SCRIPT_TEMPLATE, TEMP_SCRIPT, PROGRAM_MAP

class PrepressHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            _, ext = os.path.splitext(file_path)
            ext = ext.lower()

            if ext in PROGRAM_MAP:
                print(f"New file detected: {file_path}")

                try:
                    # Copy the Illustrator JSX script to the trigger location
                    os.makedirs(os.path.dirname(TEMP_SCRIPT), exist_ok=True)
                    shutil.copyfile(SCRIPT_TEMPLATE, TEMP_SCRIPT)
                    print("Script copied to Illustrator trigger folder.")

                    # Open file using system default (assumes associations are set)
                    subprocess.run(['start', '', file_path], shell=True)

                    # Clean up after delay (optional but recommended)
                    time.sleep(10)
                    os.remove(TEMP_SCRIPT)
                    print("Trigger script removed.")

                except Exception as e:
                    print("Error during automation:", e)

def start_watcher():
    event_handler = PrepressHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_FOLDER, recursive=False)
    observer.start()
    print(f"Watching folder: {WATCH_FOLDER}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
