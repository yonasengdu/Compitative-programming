class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        counter_p = Counter(p)
        window_counter = defaultdict(int)
        start , end = 0,0
        anagram_index = []
        for ind in range(len(p)):
            window_counter[s[end]] += 1
            end += 1
        if counter_p == window_counter:
            anagram_index.append(start)
        while end < len(s):
            window_counter[s[end]] += 1
            window_counter[s[start]] -= 1
            
            if window_counter[s[start]] == 0:
                del(window_counter[s[start]])
            start += 1
            end += 1
            if counter_p == window_counter:
                anagram_index.append(start)
        return anagram_index
        
        