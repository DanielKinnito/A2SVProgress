class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        far = 0.0000
        kelvin = 0.0000
        far = celsius * 1.80 + 32.00
        kelvin = celsius + 273.15
        answer=[kelvin,far]
        return answer