"""Export the same notebooks for browser execution on GitHub Pages."""
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "chapters/w02"
OUTPUT = ROOT / "dist/w02"
for name, notebook, mode, data_path in [
    ("slides", SOURCE / "week02_slides.py", "run", "practice/data"),
    ("lab", SOURCE / "practice/regression_lab.py", "edit", "data"),
]:
    folder = OUTPUT / name
    subprocess.run([
        sys.executable, "-m", "marimo", "export", "html-wasm", str(notebook),
        "--output", str(folder), "--mode", mode, "--force",
    ], check=True, cwd=notebook.parent)
    shutil.copytree(SOURCE / "practice/data", folder / data_path, dirs_exist_ok=True)
    assert (folder / "index.html").is_file()
    html_file = folder / "index.html"
    html = html_file.read_text()
    # shortcut: marimo 0.25.1 exports runtime defaults; remove when its CLI preserves autorun config.
    autorun = '"auto_instantiate": false'
    assert html.count(autorun) == 1, "WASM configuration changed; review the autorun setting"
    html = html.replace(autorun, '"auto_instantiate": true', 1)
    html_file.write_text(html)
    assert '"auto_instantiate": true' in html, "Browser calculations must start automatically"
    assert str(ROOT) not in html, "A local machine path leaked into the export"
    if name == "slides":
        assert ".reveal-viewport" in html, "Slide CSS was not included"
print(f"Exported browser slides and editable regression lab: {OUTPUT}")
