from queue import SimpleQueue

from lambda_scraper.components.queue.ls_queue import LambdaScraperQueue

from .factory import QueueFactory


@QueueFactory.register(doc="Simple Queue enabling local use of the scraper")
class LocalQueue(SimpleQueue, LambdaScraperQueue):
    """Minimal Queue for testing"""

    @property
    def is_empty(self) -> bool:
        return self.empty()

    def __len__(self) -> int:
        return self.qsize()
