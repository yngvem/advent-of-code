from pathlib import Path


def load_data(filename):
    with open(Path(__file__).parent / "data" / filename) as f:
        return f.read()
