class Solution:
    def numMagicSquaresInside(self, G: List[List[int]]) -> int:
    	M, N, S, t = len(G)-2, len(G[0])-2, {(8,1,6,3,5,7,4,9,2),(6,1,8,7,5,3,2,9,4),(2,7,6,9,5,1,4,3,8),(6,7,2,1,5,9,8,3,4)}, range(3)
    	return sum((lambda x: x in S or x[::-1] in S)(tuple(sum([G[i+k][j:j+3] for k in t],[]))) for i,j in itertools.product(range(M),range(N)))
