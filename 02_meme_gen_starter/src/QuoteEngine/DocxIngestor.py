"""This file parses docx file and returns quotes."""
from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
import docx


class DocxIngestor(IngestorInterface):
    """class for docx files inherting IngestorInterface."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse function to parse docx file and return quotes."""
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
            raise Exception("docx parsing issue occured.")
        return quotes
