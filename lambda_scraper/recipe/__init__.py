from importlib import import_module
from pathlib import Path

plugin_dir = (Path(__file__).parent / "plugins").resolve()
assert plugin_dir.is_dir()

PLUGINS = []

for file in plugin_dir.glob("*.py"):
    if file.name != "__init__.py":
        PLUGINS.append(file.name)

# FIXME Check if modules are really imported.
import_module("lambda_scraper.recipe.plugins")
