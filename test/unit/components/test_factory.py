import pytest
from dataclasses import dataclass
from lambda_scraper.components.factory import Factory


@pytest.fixture(scope="module")
def factory() -> Factory:
    return Factory("Simple Test factory")


@pytest.fixture(scope="module")
def test_class_name() -> str:
    return 'testClass'


@pytest.fixture(scope="module")
def test_class_doc() -> str:
    return "A test class factory"


@pytest.fixture(scope="module")
def testClass_factory(factory, test_class_name, test_class_doc) -> Factory:
    
    @dataclass
    @factory.register(test_class_doc)
    class testClass:
        message: str
        __name__: str = test_class_name

    return factory


def test_contains(testClass_factory, test_class_name):
    assert test_class_name in testClass_factory


def test_get_class(testClass_factory, test_class_name):
    print(testClass_factory._cls[test_class_name])
    assert testClass_factory.get_class(test_class_name)


def test_doc(testClass_factory, test_class_name, test_class_doc):
    print(testClass_factory._cls)
    assert testClass_factory.doc(test_class_name) == test_class_doc


def test_call(testClass_factory, test_class_name):
    print(testClass_factory._cls)

    test_message = "test message"
    class_instance = testClass_factory(test_class_name, message = test_message)
    assert class_instance.message == test_message

def test_unregister(testClass_factory, test_class_name):
    testClass_factory.unregister(test_class_name)
    assert test_class_name not in testClass_factory
