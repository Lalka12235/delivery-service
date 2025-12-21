import uuid
from abc import ABC,abstractmethod


class UUIDGenerator(ABC):

    @abstractmethod
    def generate(self) -> uuid.UUID:
        raise NotImplementedError