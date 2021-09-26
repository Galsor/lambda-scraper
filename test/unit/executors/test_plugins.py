import pytest
from lambda_scraper.executors.plugins import Plugins, Plugin
from ..mock_config import mock_config_url_parser


@pytest.fixture(scope="module")
def plugins_config():
    return mock_config_url_parser()

@pytest.fixture
def plugins(plugins_config) -> Plugins:
    plugins = Plugins(cfg=plugins_config, initialized=False)
    plugins.reset(reinitialize=False)
    return plugins

@pytest.fixture
def discovered_plugins():
    return [
        Plugin(name="test_plugin_1", activated=True), 
        Plugin(name="test_plugin_2", activated=False)
        ]

def test_singleton(plugins_config):
    first_plugins = Plugins(plugins_config, initialized=False)
    second_plugins = Plugins(plugins_config, initialized=False)
    assert id(first_plugins) == id(second_plugins)

def test_discover(plugins):
    discovered_plugins = plugins._discover()
    assert discovered_plugins

def test_load_active_plugins(plugins, discovered_plugins):
    plugins.load_active_plugins(discovered_plugins)
    assert len(plugins.name_to_plugin) == 1

def test_load_all_plugins(plugins, discovered_plugins):
    plugins.load_all_plugins(discovered_plugins)
    assert len(plugins.name_to_plugin) == 2

def test_initialize_all_plugins(plugins):
    plugins._initialize(only_active=False)
    assert len(plugins.name_to_plugin) == 2

def test_initialize_active_plugins(plugins):
    plugins._initialize(only_active=True)
    assert len(plugins.name_to_plugin) == 1

def test_getitem_returns_plugin(plugins, discovered_plugins):
    plugins.load_all_plugins(discovered_plugins)
    ret = plugins[discovered_plugins[0].name]
    assert isinstance(ret, Plugin)

