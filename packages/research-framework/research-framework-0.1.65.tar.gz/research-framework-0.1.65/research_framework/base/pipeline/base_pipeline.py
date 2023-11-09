from abc import ABC, abstractmethod

class BasePipeline(ABC):
    @abstractmethod
    def start(self) -> None: ...
    @abstractmethod
    def log_metrics(self) -> None: ...