from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
import subprocess
import os
import random


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Ingest error file extension issue.')
        quotes = []

        try:
            tmp = f'./_data/DogQuotes/{random.randint(0, 1000)}.txt'
            print(tmp)
            call = subprocess.call(['pdftotext', path, tmp])

            file_ref = open(tmp, "r")
            for line in file_ref.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split('-')
                    new_quote = QuoteModel(parse[0].strip(),
                                           parse[1].strip())
                    quotes.append(new_quote)
            file_ref.close()
            os.remove(tmp)
        except Exception as e:
            return Exception(e)
        return quotes
