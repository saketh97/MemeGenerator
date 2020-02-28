from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
import pandas


class CSVIngestor(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Ingest error file extension issue.')
        try:
            quotes = []
            csv = pandas.read_csv(path, header=0)
            for index, rows in csv.iterrows():
                new_quote = QuoteModel(rows['body'], rows['author'])
        except Exception as e:
            return Exception(e)
        return quotes
