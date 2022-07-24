# equals method?
class TrieNode:
    
    def __init__(self, num_chars):
        self.edges = [None] * num_chars
        self.is_leaf = False



# perhaps can take in/inherit char mapping + max char set
# trie node would then need to take in variable char set
    # would then want a method to create a node of correct char set
class Trie:
    
    def __init__(self, num_chars):
        self._num_chars = num_chars
        self.root = self._create_node()
        
    
    def _create_node(self):
        return TrieNode(self._num_chars)


    def _letter_to_index(self, letter: str) -> int:
        # throw error if letter len is not right
        return ord(letter.lower()) - ord('a')
    
    
    def add(self, word: str) -> bool:
        # throw error if not a letter
        # do nothing if empty string
        cur_node = self.root 

        for char in word:
            idx = self._letter_to_index(char)
            
            if not cur_node.edges[idx]:
                cur_node.edges[idx] = self._create_node()
            
            cur_node = cur_node.edges[idx]
        
        cur_node.is_leaf = True
      
    
    def contains(self, word: str) -> bool:
        cur_node = self.root

        for char in word:
            idx = self._letter_to_index(char)
            cur_node = cur_node.edges[idx]
            
            if cur_node is None:
                return False
            
        if cur_node.is_leaf:
            return True
        return False

    
    def delete(self, word: str) -> bool:
        # empty word condition
        cur_node = delete_from = self.root
        delete_idx = self._letter_to_index(word[0])

        for char in word:
            idx = self._letter_to_index(char)

            if cur_node.is_leaf:
                delete_from = cur_node
                delete_idx = idx

            cur_node = cur_node.edges[idx]
            
            if cur_node is None:
                return False

        if cur_node.is_leaf:
            delete_from.edges[delete_idx] = None
            return True

        return False