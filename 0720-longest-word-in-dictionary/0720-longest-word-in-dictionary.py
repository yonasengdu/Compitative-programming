class TrieNode:
    def __init__(self):
        self.children = defaultdict(lambda:TrieNode())
        self.End = False
    
class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()
        
        for word in words:
            curr = root
            
            for char in word:
                curr = curr.children[char]
                
            curr.End = True
            
            
        ans = ""
        for word in words:
            curr = root
            
            ends = 0
            level = 0
            for char in word:
                curr = curr.children[char]
                if curr.End:
                    ends += 1
                level += 1
                
            if (ends == level and len(ans) < len(word)) or (ends == level and len(ans) == len(word) and word < ans):
                ans = word
                
            
        return ans
                
                
                
        