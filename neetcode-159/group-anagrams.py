class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = defaultdict(list)
        
        for word in strs:
            toCheck = ''.join(sorted(word))
            mapper[toCheck].append(word)
            
        return [group for group in mapper.values()]
        
        