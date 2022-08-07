from abc import ABC, abstractmethod
from typing import List


class AbstractTrie(ABC):
    """An abstract Trie (Suffix Tree)"""

    @abstractmethod
    def insert(self, word: str) -> bool:
        """
        Adds a suffix to this Trie
        Returns True if the word was added, False otherwise
        """
        raise NotImplementedError
    

    @abstractmethod
    def delete(self, word: str) -> bool:
        """
        Deletes a suffic from this Trie
        Returns True if the suffix was deleted, False otherwise
        """
        raise NotImplementedError

    
    @abstractmethod
    def contains(self, word: str) -> bool:
        """Returns True if this Trie contains the suffix, False otherwise"""
        raise NotImplementedError


    @abstractmethod
    def get_all(self) -> List[str]:
        """Returns a list of all suffixes in this Trie"""
        raise NotImplementedError


    @abstractmethod
    def get_suggestions(self, prefix: str) -> List[str]:
        """
        Returns a list of all suffixes for the given prefix
        Returns an empty list if the prefix is not in this trie or if
            the prefix has no suffixes.
        """
        raise NotImplementedError
