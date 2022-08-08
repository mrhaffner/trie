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
        if char == " ":
            return 26
        else:
            hash_code = ord(char.lower()) - ord("a")
            if hash_code < 0 or hash_code > 26:
                raise ValueError("Only accepts english letters or a space")

            return hash_code


    def delete(self, suffix: str) -> bool:
        pass


    def contains(self, suffix: str) -> bool:
        pass


    def get_all_suffixes(self) -> List[str]:
        pass


    def get_suffixes(self, prefix: str) -> List[str]:
        pass


