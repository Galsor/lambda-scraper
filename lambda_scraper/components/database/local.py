import json
import logging
from functools import cached_property
from pathlib import Path
from typing import Dict

from lambda_scraper.components.database.ls_database import LambdaScraperDocumentDatabase

from .factory import DatabaseFactory

logger = logging.getLogger(__name__)


@DatabaseFactory.register("Simple document database enabling local use of the scraper")
class LocalDocumentDatabase(LambdaScraperDocumentDatabase):
    """Minimal Database for testing"""

    def __init__(self, config):
        self.filepath = config.environment.db.filepath

        if not Path(self.filepath).exists():
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump({}, f)

    @cached_property
    def _data(self) -> dict:
        with open(self.filepath) as f:
            data = json.load(f)
        return data

    def _save_state(self):
        with open(self.filepath, "w") as f:
            json.dump(self._data, f)

    def add(self, id: str, data: Dict) -> None:
        try:
            logger.info(f"Updating document {id} with: {data} ")
            self._data[id] = data
        except KeyError:
            logger.info(f"Creating new document {id} with: {data}")
            self._data.update({id: data})

    def get(self, id: str) -> dict:
        return self._data[id]

    def delete(self, id: str, save: bool = False) -> None:
        del self._data[id]
        if save:
            self._save_state()

    def save(self, id: str, data: Dict) -> None:
        self.add(id, data)
        self._save_state()

    @property
    def is_empty(self) -> bool:
        return not bool(self._data)

    def __len__(self) -> int:
        return len(self._data)
