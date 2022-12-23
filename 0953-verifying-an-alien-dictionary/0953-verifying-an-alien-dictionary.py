class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dictionary = {}
        word_length = len(words)
        order_length = len(order)
        if word_length == 1:
            return True
        
        for position in range(order_length):
            key = order[position]
            order_dictionary[key] = position

        
        for word_pointer in range((word_length)-1):
            word1 = words[word_pointer]
            word2 = words[word_pointer+1]
            min_length_word1_word2 = min(len(word1),len(word2))
            counter = 0
             
            for latter_pointer in range(min_length_word1_word2):
                word1_latter = word1[latter_pointer]
                word2_latter = word2[latter_pointer]
                if order_dictionary[word1_latter] > order_dictionary[word2_latter]:
                    return False
                elif  order_dictionary[word1_latter] == order_dictionary[word2_latter]:
                    counter+=1
                    continue
                else: 
                    break
                    
            if counter == min_length_word1_word2 and len(word1)> len(word2):
                return False
        return True
                
            
            
                
                
        
            
        
        