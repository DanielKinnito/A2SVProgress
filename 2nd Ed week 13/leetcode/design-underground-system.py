class UndergroundSystem:

    def __init__(self):
        self.checkin = {}
        self.journey = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, checkin_time = self.checkin[id]
        journey_time = t - checkin_time

        if (start, stationName) not in self.journey:
            self.journey[(start, stationName)] = [0, 0]

        self.journey[(start, stationName)][0] += journey_time
        self.journey[(start, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count = self.journey[(startStation, endStation)]
        average_T = total_time / count

        return average_T



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)