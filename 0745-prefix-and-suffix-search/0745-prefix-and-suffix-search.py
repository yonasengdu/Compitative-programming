import collections
Trie = lambda: collections.defaultdict(Trie)

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie =  Trie()
        for weight,word in enumerate(words):
            for i in range(len(word)+1):
                node = self.trie
                node['weight'] = weight
                
                word_to_insert = word[i:]+'#'+word
                for c in word_to_insert:
                    node = node[c]
                    node['weight'] = weight
    

    def f(self, pref: str, suff: str) -> int:
        cur = self.trie
        for letter in suff + '#' + pref:
            if letter not in cur: return -1
            
            cur = cur[letter]
            
        return cur['weight']
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)