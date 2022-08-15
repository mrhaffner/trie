import math

from trie.abstract_trie import AbstractTrie
from trie.trie_node import TrieNode
from typing import List


class StandardTrie(AbstractTrie):
    """
    A Trie (Prefix Tree)
    Invariant:
        1. A Trie is a tree representing a set of strings
        2. The edges of a node represent a charater in a char set
        3. A valid string in the trie is found by following a path from root to
           a child node marked "is_suffix_end"
    """

    SIZE_CHAR_SET = 27

    def __init__(self, max_depth: int = math.inf) -> None:
        """
        max_depth is defined to be an int.  However, the default value of math.inf 
            is actually a float.  While this is unfortunate, it should not matter
        Raises ValueError if max_depth is negative
        """
        if max_depth < 0:
            raise ValueError("max_depth must be a positive integer")

        self._root = self._create_node()
        # automatically includes the empty string
        self._root.is_suffix_end = True
        self._max_depth = max_depth

    
    def _create_node(self) -> TrieNode:
        """Creates a new TrieNode with length edges equal to SIZE_CHAR_SET"""
        return TrieNode(StandardTrie.SIZE_CHAR_SET)


    def insert(self, suffix: str) -> bool:
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
        cur_node.is_suffix_end = True

        return True


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
        except ValueError: # if not a valid char
            return False
        
        return True


    def _hash_char(self, char: str) -> int:
        """
        Converts and returns a single character to a hashcode
        Upper case letters are converted to lower case
        Example hash codes:
            a = 0
            ...
            z = 25
            space = 26

        Raises ValueError if char is not an english letter or a space
        """
        if char == " ":
            return 26
        else:
            hash_code = ord(char.lower()) - ord("a")
            if hash_code < 0 or hash_code > 26:
                raise ValueError("Only accepts english letters or a space")

            return hash_code


    def contains(self, suffix: str) -> bool:
        node = self._get_node_from_str(suffix)

        if node is None or not node.is_suffix_end:
            return False
        else:
            return True


    def _get_node_from_str(self, word: str) -> TrieNode:
        """
        Traverses this trie to get return the node at the end of word 
            if word is in this trie
        Returns None if the word is not a valid suffix or the word is
            not in this trie
        """
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

        node.is_suffix_end = False
        return True


    def get_suffixes(self, prefix: str = "") -> List[str]:
        node = self._get_node_from_str(prefix)
        
        if node is None:
            return []

        return self._get_suffixes_from_node(node)


    def _get_suffixes_from_node(self, node: TrieNode, suffix = "", suffixes = None) -> List[str]:
        """
        Returns an array of all suffixes from a given root node
        """
        if suffixes is None:
            suffixes = []

        # do not add "" to suffixes
        if node.is_suffix_end and suffix != "":
            suffixes.append(suffix)

        for idx, node in enumerate(node.edges):
            if node:
                self._get_suffixes_from_node(node, suffix + self._reverse_hash_char(idx), suffixes)

        return suffixes


    def _reverse_hash_char(self, index: int) -> str:
        """
        Converts and returns a char based by unhashing an edges index
        Example outputs:
            0 = a
            ...
            25 = z
            26 = space

        Raises ValueError if index is not between 0 and 26 inclusive
        """
        if (not 0 <= index <= 26):
            raise ValueError("Index must be between 0 and 26 inclusive")
        if index == 26:
            return " "
        return chr(index + ord("a"))
