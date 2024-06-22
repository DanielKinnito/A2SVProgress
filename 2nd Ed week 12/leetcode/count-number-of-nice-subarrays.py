class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(k: int) -> int:
            answer = 0
            left, right = 0, 0

            while right <= len(nums):
                if k >= 0:
                    answer += right - left
                    if right == len(nums):
                        break
                    if nums[right] & 1:
                        k -= 1
                    right += 1
                else:
                    if nums[left] & 1:
                        k += 1
                    left += 1
            return answer

        return atMost(k) - atMost(k - 1)