class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        left = 1
        right = position[-1] - position[0]

        def numBalls(force: int) -> int:
            balls = 0
            prev_position = -force
            for pos in position:
                if pos - prev_position >= force:
                    balls += 1
                    prev_position = pos
            
            return balls

        while left < right:
            middle = right - (right - left) // 2
            if numBalls(middle) >= m:
                left = middle
            else:
                right = middle - 1

        return left