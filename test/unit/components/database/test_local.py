import pytest
import logging
from lambda_scraper.components.database.local import LocalDocumentDatabase

logger = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def database(mock_config_producer):
    assert mock_config_producer.environment
    return LocalDocumentDatabase(mock_config_producer)


@pytest.fixture(scope="module")
def item():
    return (-1, {"name": "test item"})

def test_empty(database):
    assert database.is_empty


def test_length(database):
    assert len(database) == 0

def test_add(database, item):
    id, item_values = item
    database.add(id, item_values)
    assert len(database) == 1

def test_save_and_delete(database, item):
    id, item_values = item
    database.save(id, item_values)
    assert len(database) == 1
    database.delete(id, save = True)
    assert len(database) == 0


def test_get(database, item):
    item_id, item_values = item
    database.add(item_id, item_values)
    retrieved_item = database.get(item_id)
    assert retrieved_item == item_values
