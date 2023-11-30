class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        average = 0.00000
        summ = 0
        for num in salary:
            summ += num
        summ -= min(salary) + max(salary)
        average += (float(summ) / float((len(salary)-2)))
        formatted_average = '{:.5f}'.format(average)
        return average        