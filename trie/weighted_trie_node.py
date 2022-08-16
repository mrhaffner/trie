class WeightedTrieNode():

    def __init__(self, length_edges, weight = 0):
        if length_edges < 0:
            raise ValueError("length_edges cannot be negative")
        if weight < 0:
            raise ValueError("weight cannot be negative")
        self.edges = [None] * length_edges
        self.weight = weight