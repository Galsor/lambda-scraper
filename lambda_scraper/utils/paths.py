from pathlib import Path

ROOT_DIR = Path(__file__).parents[2].resolve()
SRC_DIR = Path(__file__).parents[1].resolve()
DATA_DIR = ROOT_DIR / "data"
CONFIG_DIR = ROOT_DIR / "config"
PLUGINS_DIRS = [
    (SRC_DIR / "recipe" / "plugins"),
]
