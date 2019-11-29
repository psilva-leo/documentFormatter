class BaseParser(object):

    def parse_data(self, data: str) -> str:
        raise NotImplementedError('Child class must implement parse_data method')


if __name__ == '__main__':

    parser = BaseParser()
