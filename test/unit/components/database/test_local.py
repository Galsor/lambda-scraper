import pytest
import logging
from lambda_scraper.components.database.local import LocalDocumentDatabase

logger = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def database(mock_config):
    return LocalDocumentDatabase()


@pytest.fixture(scope="module")
def item():
    return {"0": {"name": "test item"}}


def populated_database(database):
    database.save(item)
    return database


def test_empty(database):
    assert database.is_empty


def test_length(database):
    assert len(database) == 0


def test_save(database, item):
    database.save(item)
    assert len(database) == 1


def test_get(populated_database, item):
    item_id = item.keys()[0]
    retrieved_item = populated_database.get(item_id)
    assert retrieved_item == item
