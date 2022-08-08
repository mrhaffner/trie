import math

from trie.abstract_trie import AbstractTrie
from trie.trie_node import TrieNode
from typing import List



class StandardTrie(AbstractTrie):
    """A Trie (Suffix Tree)"""

    # note about max.inf being a float
    # do we need to test this default max_depth behavior?
    def __init__(self, max_depth: int = math.inf) -> None:
        if max_depth < 0:
            raise ValueError('max_depth must be a positive integer')

        self._root = TrieNode(0)
        self._max_depth = max_depth

    
    def insert(self, suffix: str) -> bool:
        return self._is_valid_suffix(suffix)


    def _is_valid_suffix(self, suffix: str) -> bool:
        """
        A valid suffix may contain only english letters and/or spaces
        Returns True if the given suffix may be inserted into this Trie
        """
        if len(suffix) > self._max_depth:
            return False

        try:
            for char in suffix:
                self._hash_char(char)
        except TypeError:
            return False
        except ValueError:
            return False
        
        return True


    def _hash_char(self, char: str) -> int:
        """
        Converts and returns a single character to a hashcode
        Upper case letters are converted to lower case

        Examples:
            a = 0
            z = 25
            space = 26

        Raises ValueError if char is not an english letter or a space
        Raises TypeError if the length of char is not 1
        """
        if char == " ":
            return 26
        else:
            hash_code = ord(char.lower()) - ord("a")
            if hash_code < 0 or hash_code > 26:
                raise ValueError("Only accepts english letters or a space")

            return hash_code


    def contains(self, suffix: str) -> bool:
        pass


    def delete(self, suffix: str) -> bool:
        pass


    def get_all_suffixes(self) -> List[str]:
        pass


    def get_suffixes(self, prefix: str) -> List[str]:
        pass


