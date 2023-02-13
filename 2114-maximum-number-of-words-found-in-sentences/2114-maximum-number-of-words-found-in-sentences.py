class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count = 0
        for sen in  sentences:
            sent = sen.split(" ")
            if len(sent) > count:
                count = len(sent)
        return count 
        
            
        