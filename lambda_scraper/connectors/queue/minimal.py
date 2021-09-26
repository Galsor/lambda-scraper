from queue import SimpleQueue

from .queue import LambdaScraperQueue


class MinimalQueue(SimpleQueue, LambdaScraperQueue):
    """Minimal Queue for testing"""

    @property
    def is_empty(self) -> bool:
        return self.empty()

    def __len__(self) -> int:
        return self.qsize()
