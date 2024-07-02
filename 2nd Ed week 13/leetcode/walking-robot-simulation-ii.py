class Robot:
    def __init__(self, width: int, height: int):
        """
        Initializes the Robot with the specified width and height.
        The robot is initially at (0, 0) facing "South" 
            which is "East" for a cartesian type grid.
        """
        self.isOrigin = True
        self.i = 0  # Index for tracking position in the 'pos' list

        # List of tuples representing positions and directions
        self.pos = [((0, 0), 'South')] + \
                   [((i, 0), 'East') for i in range(1, width)] + \
                   [((width - 1, j), 'North') for j in range(1, height)] + \
                   [((i, height - 1), 'West') for i in range(width - 2, -1, -1)] + \
                   [((0, j), 'South') for j in range(height - 2, 0, -1)]

    def step(self, num: int) -> None:
        """
        Moves the robot forward by the number of steps.
        Updates the index 'i' based on the number of steps taken.
        """
        self.isOrigin = False
        self.i = (self.i + num) % len(self.pos)

    def getPos(self) -> List[int]:
        """
        Return curr position as list [x, y].
        """
        return list(self.pos[self.i][0])

    def getDir(self) -> str:
        """
        If the robot is at the origin, returns "East", 
            otherwise, returns the direction from the 'pos' list.
        """
        return 'East' if self.isOrigin else self.pos[self.i][1]




# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()