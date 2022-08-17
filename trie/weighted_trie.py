import math

from trie.standard_trie import StandardTrie
from trie.weighted_trie_node import WeightedTrieNode
from typing import List, TypedDict


class SuffixEntry(TypedDict):
    suffix: str
    weight: int


class WeightedTrie(StandardTrie):
    
    def __init__(self, max_depth: int = math.inf) -> None:
        pass
        if max_depth < 0:
            raise ValueError("max_depth must be a positive integer")

        self._root = self._create_node()
        # automatically includes the empty string
        self._root.weight = 1
        self._max_depth = max_depth


    def _create_node(self) -> WeightedTrieNode:
        return WeightedTrieNode(StandardTrie.SIZE_CHAR_SET)


    def insert(self, suffix_dict: SuffixEntry) -> bool:
        suffix = suffix_dict["suffix"]
        weight = suffix_dict["weight"]

        if not self._is_valid_suffix(suffix):
            return False
        
        cur_node = self._root

        for char in suffix:
            hash_code = self._hash_char(char)

            # create new node if char not in trie
            if not cur_node.edges[hash_code]:
                cur_node.edges[hash_code] = self._create_node()

            cur_node = cur_node.edges[hash_code]

        # mark the end of the suffix
        cur_node.weight = weight

        return True


    def contains(self, suffix: str) -> bool:
        node = self._get_node_from_str(suffix)

        if node is None or node.weight == 0:
            return False
        else:
            return True


    def _get_node_from_str(self, word: str) -> WeightedTrieNode:
        cur_node = self._root

        for char in word:
            if not self._is_valid_suffix(word):
                return None
                
            hash_code = self._hash_char(char)
            cur_node = cur_node.edges[hash_code]

            if cur_node is None:
                return cur_node

        return cur_node


    def delete(self, suffix: str) -> bool:
        # cannot delete empty string
        if suffix == "":
            return False

        node = self._get_node_from_str(suffix)
        
        if node is None:
            return False

        node.weight = 0
        return True


    def get_suffixes(self, prefix: str = "") -> List[str]:
        node = self._get_node_from_str(prefix)
        
        if node is None:
            return []

        suffix_dicts = self._get_suffixes_from_node(node)
        suffix_dicts.sort(reverse=True, key=lambda d: d["weight"]) # and by alphabet?
        return [d["suffix"] for d in suffix_dicts]


    def _get_suffixes_from_node(self, node: WeightedTrieNode, suffix = "", suffixes = None) -> List[SuffixEntry]:
        if suffixes is None:
            suffixes = []

        # do not add "" to suffixes
        if node.weight > 0 and suffix != "":
            suffixes.append({"suffix": suffix, "weight": node.weight})

        for idx, node in enumerate(node.edges):
            if node:
                self._get_suffixes_from_node(node, suffix + self._reverse_hash_char(idx), suffixes)

        return suffixes