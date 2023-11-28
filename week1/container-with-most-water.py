class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = 0
        left_pointer, right_pointer = 0, len(height) - 1

        while left_pointer < right_pointer:
            h_left, h_right = height[left_pointer], height[right_pointer]
            width = right_pointer - left_pointer
            current_water = min(h_left, h_right) * width

            max_water = max(max_water, current_water)

            if h_left < h_right:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_water