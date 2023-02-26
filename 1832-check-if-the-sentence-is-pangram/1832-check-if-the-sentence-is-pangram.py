class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        strings = Counter(sentence)
        
        for latter in string.ascii_lowercase:
            if latter not in strings:
                return False
        return True
        
        
        
        