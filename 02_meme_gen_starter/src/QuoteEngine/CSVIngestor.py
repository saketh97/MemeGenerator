from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
import pandas


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Ingest error file extension issue.')
        quotes = []
        try:
            csv = pandas.read_csv(path, header=0)
            for index, rows in csv.iterrows():
                new_quote = QuoteModel(rows['body'], rows['author'])
        except Exception as e:
            print('Not able to oepn the file specified')

        return quotes
