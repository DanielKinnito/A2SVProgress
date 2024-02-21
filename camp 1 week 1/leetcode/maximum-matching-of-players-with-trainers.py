class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        count = 0
        right = 0

        for player in players:
            while right < len(trainers):
                if trainers[right] >= player:
                    count += 1
                    right += 1
                    break
                else:
                    right += 1
                
        return count