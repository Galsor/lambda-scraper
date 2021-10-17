import pytest

from lambda_scraper.utils.types import *


def test_ExecutorMode():
    assert ExecutorMode.PRODUCER
    assert ExecutorMode.SCRAPER


def test_TaskType():
    assert len(list(TaskType)) > 0
