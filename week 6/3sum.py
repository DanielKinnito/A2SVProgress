class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer_set = set()

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                local_sum = nums[i] + nums[left] + nums[right]
                
                if local_sum == 0:
                    answer_set.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif local_sum < 0:
                    left += 1
                else:
                    right -= 1

        # Convert the set of tuples to a list of lists
        answer = [list(triplet) for triplet in answer_set]

        return answer