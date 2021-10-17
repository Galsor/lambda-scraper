from pathlib import Path
from importlib import import_module

plugin_dir = (Path(__file__).parent / "plugins").resolve()
assert plugin_dir.is_dir()

PLUGINS = []

for file in plugin_dir.glob("*.py"):
    if file.name != "__init__.py":
        PLUGINS.append(file.name)
        import_module(file.name)
