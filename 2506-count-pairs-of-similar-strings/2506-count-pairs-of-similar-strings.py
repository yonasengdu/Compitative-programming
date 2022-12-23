class Solution:
    def similarPairs(self, words: List[str]) -> int:
        number_of_pairs = 0
        for word in range(len(words)):
            word_set = set(words[word])
            words[word] = ''.join(sorted(word_set))
        words_set_dictionary = Counter(words)
        for word, num_times_it_appered in words_set_dictionary.items():
            if num_times_it_appered > 1:
                number_of_pairs += comb( num_times_it_appered,2)
        return number_of_pairs
     
        