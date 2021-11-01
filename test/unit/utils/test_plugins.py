import pytest
from pathlib import Path

from lambda_scraper.utils.types import BaseTask
from lambda_scraper.utils.plugins import load_plugins
from lambda_scraper.recipe.interface import scrap, produce, context

@pytest.fixture(scope="module")
def plugin_dir() -> Path:
    return (Path() / "test" / "unit"/ "utils"/ "mock_plugins").resolve()

@pytest.fixture(scope="module")
def plugin(plugin_dir) -> Path:
    return plugin_dir / "mock_plugin.py"

@pytest.fixture(scope="module")
def mock_task(plugin):
    return type(plugin.stem, BaseTask, {})

def test_load_plugins(plugin_dir):
    print(plugin_dir)
    #Given
    init_scrap_reg_len = len(scrap.registry)
    init_produce_reg_len = len(produce.registry)
    init_context_reg_len = len(context.registry)

    # With
    plugins = load_plugins([plugin_dir])

    # Expect
    assert plugins
    assert len(plugins) > 0
    assert len(scrap.registry) > init_scrap_reg_len
    assert len(produce.registry) > init_produce_reg_len
    assert len(context.registry) > init_context_reg_len
