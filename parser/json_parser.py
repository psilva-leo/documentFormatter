import json
from typing import Tuple

from parser.base_parser import BaseParser


class JSONParser(BaseParser):

    def __init__(self):

        super(JSONParser, self).__init__()
        self.__setup()

    def __setup(self):
        pass

    def parse_data(self, data: str, indent: int = 2, sort_keys: bool = False) -> Tuple[str, str or None]:
        try:
            json_string = json.loads(data)
            json_formatted = json.dumps(json_string, indent=indent, sort_keys=sort_keys)

            return json_formatted, None
        except ValueError as error:
            print(error)
            return data, error.__str__()
        except Exception as error:
            print(error)
            return data, 'Unknown error'
