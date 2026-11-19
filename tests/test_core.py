import tempfile
from pathlib import Path

from malletscolds6j_kit.core import Malletscolds6jTool


def test_summarize_numeric_column():
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp, "a.csv")
        path.write_text("x,y\n1,2\n3,4\n", encoding="utf-8")
        stats = Malletscolds6jTool().summarize(path)
        assert stats["x"]["n"] == 2 and stats["x"]["mean"] == 2.0


def test_missing_file_returns_empty():
    assert Malletscolds6jTool().summarize("/no/such.csv") == {}


def test_skips_non_numeric_rows():
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp, "b.csv")
        path.write_text("x\n1\nnot-a-number\n", encoding="utf-8")
        assert Malletscolds6jTool().summarize(path)["x"]["n"] == 1
