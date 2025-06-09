import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from config import WATCH_FOLDER, PROGRAM_MAP
from bridge_runner import run_illustrator_script_with_file


class PrepressHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            _, ext = os.path.splitext(file_path)
            ext = ext.lower()

            if ext in PROGRAM_MAP:
                print(f"New file detected: {file_path}")
                try:
                    run_illustrator_script_with_file(file_path)
                except Exception as e:
                    print(f"Error processing file {file_path}: {e}")


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
