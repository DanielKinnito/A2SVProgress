class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        for ghost in ghosts:
            distance_between_ghost = abs(ghost[0]-target[0])+abs(ghost[1]-target[1])
            distance_between_target = abs(target[0])+abs(target[1])

            if distance_between_ghost <= distance_between_target:
                return False
            
        return True