from lambda_scraper.components.factory import Factory


class QueueFactoryClass(Factory):

    def register(self, doc=None):
        def fn(cls):
            return super(QueueFactoryClass, self).register(cls.__name__, doc)(cls)

        return fn


QueueFactory = QueueFactoryClass('Queue')
