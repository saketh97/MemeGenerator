from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class TextIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Ingest error file extension issue.')
        quotes = []

        try:
            txt_file = open(path, 'r')
            for lines in txt_file.readlines():
                line = line.strp('\n\r').strip()
                if(len(line) > 0):
                    parse = line.split('-')
                    new_quote = QuoteModel(parse[0].strip(),
                                           parse[1].strip())
                    quotes.append(new_quote)
                txt_file.close()
        except Exception as e:
            print('Not able to oepn the file specified')

        return quotes
