from pathlib import Path
from importlib import import_module

plugin_dir = Path("./plugins/")
assert plugin_dir.is_dir()

PLUGINS = []

for file in plugin_dir.glob("*.py"):
    PLUGINS.append(file.name)
    import_module(file.name)