class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        wins = {}
        losses = {}

        for winner, loser in matches:
            # For wins
            if winner not in wins:
                wins[winner] = 1
            else:
                wins[winner] += 1

            # For losses
            if loser not in losses:
                losses[loser] = 1
            else:
                losses[loser] += 1

        no_losses = [player for player in wins if player not in losses]
        one_loss = [player for player, loss_count in losses.items() if loss_count == 1]

        no_losses.sort()
        one_loss.sort()

        return [no_losses, one_loss]