import json
import logging
from typing import Dict
from pathlib import Path
from functools import cached_property

from .factory import DatabaseFactory
from lambda_scraper.components.database.ls_database import LambdaScraperDocumentDatabase

logger = logging.getLogger(__name__)


@DatabaseFactory.register('Simple document database enabling local use of the scraper')
class LocalDocumentDatabase(LambdaScraperDocumentDatabase):
    """Minimal Database for testing"""

    def __init__(self, config):
        self.filepath = config.environement.db.filepath

        if not Path(self.filepath).exists():
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump({}, f)

    @cached_property
    def _data(self) -> dict:
        with open(self.filepath) as f:
            data = json.load(f)
        return data

    def save(self, id: str, data: Dict) -> None:
        try:
            logger.info(f"Updating document {id} with: {data} ")
            self._data[id] = data
        except KeyError:
            logger.info(f"Creating new document {id} with: {data}")
            self._data.update({id: data})

        with open(self.filepath, "w") as f:
            json.dump(self._data, f)

    def get(self, id: str) -> dict:
        return self._data[id]

    @property
    def is_empty(self) -> bool:
        return not bool(self._data)

    def __len__(self) -> int:
        return len(self._data)
