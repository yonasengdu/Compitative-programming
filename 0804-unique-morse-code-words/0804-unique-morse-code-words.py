class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_mapper = {}
        
        transformations = set()
        for i,code in enumerate(morse):
            morse_mapper[chr(i+97)] = code
            
            
        for word in words:
            morse_code = ''
            for char in word:
                morse_code += morse_mapper[char]
                
            transformations.add(morse_code)
            
            
        return len(transformations)
        
        
    