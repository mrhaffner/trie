from trie import Trie

t = Trie()

t.add("Apple")
t.add("AppleOrchard")

if __name__ == "__main__":
    assert t.contains("Apple")
    assert not t.contains("Apples")
    assert not t.contains("App")
    assert not t.contains("ple")
    assert not t.contains("ppl")
    assert t.contains("AppleOrchard")
    assert not t.contains("AppleOrchards")
    assert not t.contains("AppleOrchar")
    assert not t.contains("ppleOrchar")

    print("All tests passed!")

