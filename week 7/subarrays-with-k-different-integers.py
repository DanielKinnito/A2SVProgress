class Solution:
    def atMostK(self, nums: List[int], k: int) -> int:
            count = 0
            left = 0
            freq_map = {}

            for right in range(len(nums)):
                if nums[right] not in freq_map or freq_map[nums[right]] == 0:
                    k -= 1

                freq_map[nums[right]] = freq_map.get(nums[right], 0) + 1

                while k < 0:
                    freq_map[nums[left]] -= 1
                    if freq_map[nums[left]] == 0:
                        k += 1
                    left += 1

                count += right - left + 1

            return count
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        #  atmost(k) atmost(k - 1)        
        return self.atMostK(nums, k) - self.atMostK(nums, k - 1)