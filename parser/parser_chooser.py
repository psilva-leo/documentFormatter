from parser.json_parser import JSONParser


class ParserChooser(object):

    def __init__(self):

        self.__parsers = dict(
            json=JSONParser()
        )

    def get_parser(self, parser: str):

        try:
            return self.__parsers[parser]
        except KeyError:
            raise KeyError('Parser {parser} not implemented.'.format(parser=parser))
        except Exception:
            raise Exception
