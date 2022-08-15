from abc import ABC, abstractmethod
from typing import List


class AbstractTrie(ABC):
    """An abstract Trie (Preix Tree)"""

    @abstractmethod
    def insert(self, suffix: str) -> bool:
        """
        Adds a suffix to this Trie
        Returns True if the suffix was added, False otherwise
        """
        raise NotImplementedError
    

    @abstractmethod
    def contains(self, suffix: str) -> bool:
        """Returns True if this Trie contains the suffix, False otherwise"""
        raise NotImplementedError


    @abstractmethod
    def delete(self, suffix: str) -> bool:
        """
        Deletes a suffix from this Trie
        Returns True if the suffix was deleted, False otherwise
        """
        raise NotImplementedError


    @abstractmethod
    def get_suffixes(self, prefix: str = "") -> List[str]:
        """
        Returns a list of all suffixes for the given prefix
        Returns an empty list if the prefix is not in this trie or
            the prefix has no suffixes
        If no arguement is provided, returns all suffixes in this trie
        """
        raise NotImplementedError
