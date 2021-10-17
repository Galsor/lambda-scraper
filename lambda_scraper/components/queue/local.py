from queue import SimpleQueue

from .factory import QueueFactory
from lambda_scraper.components.queue.ls_queue import LambdaScraperQueue

@QueueFactory.register('Simple Queue enabling local use of the scraper')
class LocalQueue(SimpleQueue, LambdaScraperQueue):
    """Minimal Queue for testing"""

    @property
    def is_empty(self) -> bool:
        return self.empty()

    def __len__(self) -> int:
        return self.qsize()
