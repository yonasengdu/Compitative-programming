class Trie:
    def __init__(self):
        self.children = defaultdict(lambda:Trie())
        self.end = False
        self.onPath = 0
        
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = Trie()
        
        for word in words:
            curr = root
            for char in word:
                curr = curr.children[char]
                curr.onPath += 1
                
        ans = []
        for word in words:
            curr = root
            prefixes = 0
            for char in word:
                curr = curr.children[char]
                prefixes += curr.onPath

            ans.append(prefixes)
            
        return ans

        
        
        
                
                
        
        