"""This file parses txt file and returns quotes."""
from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class TextIngestor(IngestorInterface):
    """class for txt files inherting IngestorInterface."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse function to parse txt file and return quotes."""
        if not cls.can_ingest(path):
            raise Exception('Ingest error file extension issue.')
        quotes = []
        try:
            txt_file = open(path, 'r')
            for lines in txt_file.readlines():
                line = lines.strip('\n\r').strip()
                if(len(line) > 0):
                    parse = line.split('-')
                    new_quote = QuoteModel(str(parse[0].strip()),
                                           str(parse[1].strip()))
                    quotes.append(new_quote)
            txt_file.close()
        except Exception as e:
            raise Exception("txt parsing issue occured.")
        return quotes
