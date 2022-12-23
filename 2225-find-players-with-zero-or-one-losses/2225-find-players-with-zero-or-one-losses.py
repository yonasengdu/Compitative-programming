class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner_players = {}
        loser_players = {}
        answer = [[],[]]
        for player1,player2 in matches:
            if player1 not in  winner_players:
                winner_players[player1] = 1
            else:
                winner_players[player1]+=1
            if player2 not in  loser_players:
                loser_players[player2] = 1
            else:
                loser_players[player2]+=1
        for player in winner_players.keys():
            if player not in loser_players:
                answer[0].append(player)
        for player in loser_players:
            if loser_players[player] ==1:
                answer[1].append(player)
        answer[0].sort()
        answer[1].sort()
        return  answer
                
            
        