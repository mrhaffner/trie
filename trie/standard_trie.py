from trie.abstract_trie import AbstractTrie
from typing import List


class StandardTrie(AbstractTrie):
    """A Trie (Suffix Tree)"""
    
    def insert(self, suffix: str) -> bool:
        pass


    def delete(self, suffix: str) -> bool:
        pass


    def contains(self, suffix: str) -> bool:
        pass


    def get_all_suffixes(self) -> List[str]:
        pass


    def get_suffixes(self, prefix: str) -> List[str]:
        pass


