class BaseParser(object):

    def __init__(self):

        self.var = 1
        self._setup()

    def _setup(self):
        pass

    def parse_data(self, data: str) -> str:
        raise NotImplementedError('Child class must implement parse_data method')


if __name__ == '__main__':

    parser = BaseParser()
