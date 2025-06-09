# PrePress Digi

PrePress Digi automates Adobe Illustrator tasks by watching a folder for new files. When a new file is detected it opens Illustrator and runs a JSX script.

## Setup

1. **Clone the repository**

```bash
git clone <repository>
cd prepress-digi
```

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure paths**

Edit `config.py` to set:

- `WATCH_FOLDER` – folder the watcher monitors for new files.
- `SCRIPT_TEMPLATE` – path to the JSX template in the `Scripts` folder.
- `TEMP_SCRIPT` – location where the JSX file is copied for Illustrator to load.
- `ILLUSTRATOR_EXE` – full path to `Illustrator.exe`.
- `PROGRAM_MAP` – extensions the watcher should react to.

## Usage

Run the watcher from the repository root:

```bash
python main.py
```

The script copies `Scripts/run_this.jsx` to your Illustrator scripts folder (determined in `installer.py`) and starts monitoring `WATCH_FOLDER`. When a supported file appears, it is opened in Illustrator and processed.

## Building the executable

The repository contains a `PrePressDigi02.spec` file used by PyInstaller. To build the standalone executable:

```bash
pyinstaller PrePressDigi02.spec
```

The resulting binary will be placed in the `dist` directory.

