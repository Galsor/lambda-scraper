import pytest
import logging
from lambda_scraper.components.queue.local import LocalQueue

logger = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def queue():
    return LocalQueue()


@pytest.fixture
def message():
    return {"priority": 0, "value": "Testing"}


def test_empty(queue):
    assert queue.is_empty == True


def test_put(queue, message, caplog):
    queue.put(message)
    assert queue.is_empty == False


def test_len(queue):
    assert len(queue) == queue.qsize()


def test_get(queue, message):
    if len(queue) > 0:
        q_message = queue.get()
        assert q_message == message
    else:
        raise ValueError("Fixture queue does not have any message.")
