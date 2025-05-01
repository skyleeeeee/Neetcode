from abc import ABC, abstractmethod

class Logger(ABC):
    """Abstract logger interface: all implementations must provide a log method."""
    @abstractmethod
    def log(self, level: str, message: str) -> None:
        pass
