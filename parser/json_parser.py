from parser.base_parser import BaseParser


class JSONParser(BaseParser):

    def __init__(self):

        super(JSONParser, self).__init__()
        self.__setup()

    def __setup(self):
        pass

    def parse_data(self, data: str) -> str:
        return data


if __name__ == '__main__':

    parser = JSONParser()
