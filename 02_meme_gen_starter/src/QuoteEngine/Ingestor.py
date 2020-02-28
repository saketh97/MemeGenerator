"""Main ingestor file to import in both main.py and app.py."""
from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor


class Ingestor(IngestorInterface):
    """Common ingestor class to impelement."""

    importers = [DocxIngestor, CSVIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse method to parse file and return quotes."""
        for imp in cls.importers:
            if imp.can_ingest(path):
                return imp.parse(path)
