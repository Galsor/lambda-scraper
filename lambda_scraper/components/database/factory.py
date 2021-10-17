from lambda_scraper.components.factory import Factory


class DatabaseFactoryClass(Factory):

    def register(self, doc=None):
        def fn(cls):
            return super(DatabaseFactoryClass, self).register(cls.__name__, doc)(cls)

        return fn


DatabaseFactory = DatabaseFactoryClass('Database')
