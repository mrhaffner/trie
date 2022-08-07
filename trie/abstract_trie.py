from abc import ABC, abstractmethod
from typing import List


class AbstractTrie(ABC):

    @abstractmethod
    def insert(self, word: str) -> bool:
        raise NotImplementedError
    

    @abstractmethod
    def delete(self, word: str) -> bool:
        raise NotImplementedError

    
    @abstractmethod
    def contains(self, word: str) -> bool:
        raise NotImplementedError


    @abstractmethod
    def get_all(self) -> List[str]:
        raise NotImplementedError

    @abstractmethod
    def get_suggestions(self, prefix: str) -> List[str]:
        raise NotImplementedError
