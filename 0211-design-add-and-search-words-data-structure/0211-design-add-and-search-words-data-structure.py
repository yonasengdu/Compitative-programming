class TrieNode:
    def __init__(self):
        self.children = defaultdict(lambda : TrieNode())
        self.isEnd = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            curr = curr.children[char]
            
        curr.isEnd = True
                
        

    def search(self, word: str) -> bool:
        
        def backtrack(curr,char,idx):
            # print(curr.isEnd,char,idx)
            if curr.isEnd and idx == len(word) - 1:
                return True
            
            if idx >= len(word) - 1:
                return False
             
            
            for neigh in curr.children:
                if neigh == char or char == ".":
                    if  backtrack(curr.children[neigh],word[idx + 1],idx + 1):
                        return True
                    
            
              
            
                
        word = list(word)    
        word.append('*')
        return backtrack(self.root,word[0],0)
            
            
        
            
        
    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)