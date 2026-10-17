"""Check paths, argument forwarding, bootstrap isolation, and download failure."""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

SOURCE = Path(__file__).resolve().parents[2] / "scripts/week02.sh"
with tempfile.TemporaryDirectory(prefix="week02 launcher ") as directory:
    root = Path(directory)
    (root / "scripts").mkdir()
    (root / "chapters/w02").mkdir(parents=True)
    shutil.copy2(SOURCE, root / "scripts/week02.sh")
    binary = root / "bin"
    binary.mkdir()
    fake_uv = binary / "uv"
    fake_uv.write_text('#!/bin/sh\nprintf "%s\\n" "$@"\n')
    fake_uv.chmod(0o755)
    env = dict(os.environ, PATH=f"{binary}:/usr/bin:/bin")

    def run(*args):
        return subprocess.run(["/bin/bash", str(root / "scripts/week02.sh"), *args],
                              cwd="/tmp", env=env, capture_output=True, text=True, timeout=10)

    for choice, mode, file in [("slides", "run", "week02_slides.py"),
                               ("lab", "edit", "practice/regression_lab.py")]:
        result = run(choice, "--headless")
        assert result.returncode == 0, result.stderr
        assert result.stdout.splitlines() == [
            "run", "--frozen", "--project", str(root / "chapters/w02"),
            "marimo", mode, str(root / "chapters/w02" / file), "--headless",
        ], result.stdout
    assert run("unknown").returncode == 2

    # Keep a stub outside PATH to simulate uv's project-local installation.
    fake_uv.rename(root / "fake-uv")
    env["BOOTSTRAP_FAKE_UV"] = str(root / "fake-uv")
    curl = binary / "curl"
    curl.write_text('''#!/bin/sh
while [ "$1" != "--output" ]; do shift; done
cat > "$2" <<'INSTALLER'
mkdir -p "$UV_UNMANAGED_INSTALL"
cp "$BOOTSTRAP_FAKE_UV" "$UV_UNMANAGED_INSTALL/uv"
INSTALLER
''')
    curl.chmod(0o755)
    assert run("lab").returncode == 0
    assert (root / ".tools/uv/uv").is_file()
    (root / ".tools/uv/uv").unlink()
    curl.write_text("#!/bin/sh\nexit 22\n")
    assert run("slides").returncode == 22
    assert not (root / ".tools/uv/uv").exists()
print("PASS: launcher modes, paths with spaces, isolated uv bootstrap, download failure")
