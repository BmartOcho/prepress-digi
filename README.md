# PrePress Digi

This project automates the launching of Adobe applications when new files are dropped into a watch directory.  
Paths were previously hard coded in `config.py`.  Configuration is now handled through a small JSON file or environment variables.

## Configuration

1. Copy `config.json` and edit the values to match your environment.  
   You can also set environment variables with the same names if you prefer.
   * `watch_folder` – folder that will be monitored for new files.
   * `script_template` – path to the JSX template used by Illustrator.
   * `temp_script` – location where Illustrator will read the generated JSX file.
   * `illustrator_exe` – full path to the Illustrator executable.
2. Optionally set `PDP_CONFIG_FILE` to point to a different JSON file.
3. Each individual value may be overridden with environment variables named in upper case. For example `WATCH_FOLDER` overrides `watch_folder` from the JSON file.

Environment variables inside values (e.g. `%APPDATA%`) are expanded automatically.

## Running

After configuring, run `main.py` to install the script and start watching for new files:

```bash
python main.py
```
