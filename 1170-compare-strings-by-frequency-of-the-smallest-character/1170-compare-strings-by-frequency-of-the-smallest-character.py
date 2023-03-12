class Solution:
    def numSmallerByFrequency(self, Q, W):
        f = lambda x: x.count(min(x))
        W = sorted(list(map(f, W)))
        return [len(W) - bisect_right(W, i) for i in map(f, Q)]