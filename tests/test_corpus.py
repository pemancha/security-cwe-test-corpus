import subprocess
import sys
from pathlib import Path


def test_corpus_contract() -> None:
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run([sys.executable, str(root / "tools" / "validate_corpus.py")], check=True, capture_output=True, text=True)
    assert "CORPUS_VALIDATION_OK cwes=30 pairs=60 cases=120" in result.stdout
