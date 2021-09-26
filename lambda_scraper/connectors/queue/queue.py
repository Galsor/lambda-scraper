from abc import ABC, abstractmethod


class Queue(ABC):
    @abstractmethod
    def put(self, message):
        ...

    @abstractmethod
    def get(self):
        ...

    @property
    @abstractmethod
    def empty(self) -> bool:
        ...

    @abstractmethod
    def __len__(self) -> int:
        ...
