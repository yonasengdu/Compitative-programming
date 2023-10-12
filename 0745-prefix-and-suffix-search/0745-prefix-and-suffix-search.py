Trie = lambda: collections.defaultdict(Trie)
WEIGHT = False


class WordFilter:

    def __init__(self, words: List[str]):
        self.trie =  Trie()
        
        for w,word in enumerate(words):
            word += "#"
            
            for i in range(len(word)):
                cur = self.trie
                cur[WEIGHT] = w
                for j in range(i,2*len(word)):
                    cur = cur[word[j % len(word)]]
                    cur[WEIGHT] = w
        

    def f(self, pref: str, suff: str) -> int:
        cur = self.trie
        for latter in suff + '#' + pref:
            if latter not in cur: return -1
            
            cur = cur[latter]
            
        return cur[WEIGHT]
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)