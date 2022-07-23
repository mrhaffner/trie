SIZE_OF_ALPHABET = 26

class TrieNode:
    
    def __init__(self):
        self.edges = [None] * SIZE_OF_ALPHABET
        self.is_leaf = False


class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    
    def _letter_to_index(self, letter):
        return ord(letter.lower()) - ord('a')
    
    
    def add(self, word):
        node = self.root 

        for char in word:
            idx = self._letter_to_index(char)
            
            if not node.edges[idx]:
                node.edges[idx] = TrieNode()
            
            node = node.edges[idx]
        
        node.is_leaf = True
      
    
    def contains(self, word):
        node = self.root
        for char in word:
            idx = self._letter_to_index(char)
            node = node.edges[idx]
            
            if node is None:
                return False
            
        if node.is_leaf:
            return True
        return False