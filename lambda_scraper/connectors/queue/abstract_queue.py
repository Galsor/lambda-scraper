from abc import ABC, abstractmethod


class LambdaScraperQueue(ABC):
    @abstractmethod
    def put(self, message):
        ...

    @abstractmethod
    def get(self):
        ...

    @property
    @abstractmethod
    def is_empty(self) -> bool:
        ...

    @abstractmethod
    def __len__(self) -> int:
        ...
