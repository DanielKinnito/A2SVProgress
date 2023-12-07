class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        list1_dict = {}
        list2_dict = {}
        result = []

        for index, item in enumerate(list1):
            list1_dict[item] = index

        for index, item in enumerate(list2):
            list2_dict[item] = index

        min_index_sum = float('inf')

        for item in list1:
            if item in list2:
                temp = list1_dict[item] + list2_dict[item]
                if temp < min_index_sum:
                    result = [item]
                    min_index_sum = temp
                elif temp == min_index_sum:
                    result.append(item)

        return result