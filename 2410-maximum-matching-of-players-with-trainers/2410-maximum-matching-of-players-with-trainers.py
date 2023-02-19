class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        player_ptr = 0
        trainer_ptr = 0
        matches = 0
        while player_ptr < len(players) and trainer_ptr < len(trainers):
            if trainers[trainer_ptr] < players[player_ptr]:
                trainer_ptr += 1
            else:
                matches += 1
                trainer_ptr += 1
                player_ptr += 1
        return matches
                