import json

from parser.base_parser import BaseParser


class JSONParser(BaseParser):

    def __init__(self):

        super(JSONParser, self).__init__()
        self.__setup()

    def __setup(self):
        pass

    def parse_data(self, data: str, indent: int = None, sort_keys: bool = False) -> str:
        try:
            json_string = json.loads(data)
            json_formatted = json.dumps(json_string, indent=indent, sort_keys=sort_keys)

            return json_formatted
        except ValueError as error:
            print(error)
            return data
        except Exception as error:
            print('another error')
            print(error)
            return 'another error'


if __name__ == '__main__':

    parser = JSONParser()
