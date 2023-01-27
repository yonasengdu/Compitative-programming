class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        first = 0
        second = 0
        arr = []
        while first < len(word1) and second < len(word2):
            if ord(word1[first]) > ord(word2[second]):
                arr.append(word1[first])
                first += 1
            elif ord(word1[first]) < ord(word2[second]):
                arr.append(word2[second])
                second += 1
            else:
                if word1[first:] > word2[second:]:
                    arr.append(word1[first])
                    first +=1
                elif  word1[first:] < word2[second:]:
                    arr.append(word2[second])
                    second+=1
                else:
                    arr.append(word1[first])
                    first +=1
                
                    
                    
             
                    
                
        arr.extend(word1[first:])
        arr.extend(word2[second:])
        return "".join(arr)
    
    
    # aaaaba
    # aaab
     # b b b
     # b a b
                