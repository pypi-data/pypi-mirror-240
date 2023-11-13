from enum import Enum


class InputSource(Enum):
    Empty = 0
    Request = 1
    Body = 2
    ParsedBody = 3
    CastedParsedBody = 4
    Parameters = 5
    CastedParsedParameters = 6
    FileName = 7

