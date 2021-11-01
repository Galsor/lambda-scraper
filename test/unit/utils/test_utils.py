import pytest

from lambda_scraper.utils.types import *


def test_ExecutorMode():
    assert "PRODUCER" in ExecutorMode.keys()
    assert "SCRAPER" in ExecutorMode.keys()


def test_TaskType():
    assert len(list(TaskType)) > 0
