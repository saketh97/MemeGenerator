from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
import docx


class DocxIngestor(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Ingest error file extension issue.')
        quotes = []
        try:
            doc = docx.Document(path)
            for para in doc.paragraphs:
                if para.text != "":
                    parse = para.text.split('-')
                    new_quote = QuoteModel(parse[0].strip(),
                                           parse[1].strip())
                    quotes.append(new_quote)

        except Exception as e:
            return Exception(e)
        return quotes
