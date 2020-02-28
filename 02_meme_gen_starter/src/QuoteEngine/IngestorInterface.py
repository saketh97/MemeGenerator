"""Interface for file ingestors."""
from abc import ABC
from abc import abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Abstract class to inherit parsing files."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """can_ingest Method checks the extension."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract method to implement in further classes."""
        pass
