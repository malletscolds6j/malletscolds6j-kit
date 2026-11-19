# malletscolds6j-kit

Summarize numeric CSV columns (n / min / max / mean).

Small, dependency-free Python utility package generated for day-to-day file chores.
Standard library only — no third-party imports.

## Install

```bash
pip install -e .
```

## Usage

```bash
python -m malletscolds6j_kit.cli --help
```

```python
from malletscolds6j_kit.core import Malletscolds6jTool

tool = Malletscolds6jTool()
print(tool)
```

## Layout

```
malletscolds6j_kit/
  __init__.py
  core.py
  cli.py
tests/
  test_core.py
```

## License

MIT © 2026 malletscolds6j
