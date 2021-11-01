from abc import ABC, abstractmethod
from typing import Dict


class LambdaScraperDocumentDatabase(ABC):
    @abstractmethod
    def save(self, id: str, data: Dict):
        ...

    @abstractmethod
    def get(self, id: str):
        ...

    @property
    @abstractmethod
    def is_empty(self) -> bool:
        ...
