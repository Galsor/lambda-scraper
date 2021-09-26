from queue import SimpleQueue

from .queue import Queue


class MinimalQueue(Queue, SimpleQueue):
    def __init__(self):
        super().init()

    @property
    def empty(self) -> bool:
        return super().empty()

    def __len__(self) -> int:
        return super().qsize()
