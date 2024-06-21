class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        target = total // k
        nums.sort(reverse=True)
        subset = [0] * k
        
        def dfs(idx):
            if idx == len(nums):
                return True
            
            for i in range(k):
                if subset[i] + nums[idx] <= target:
                    subset[i] += nums[idx]
                    if dfs(idx + 1):
                        return True
                    subset[i] -= nums[idx]
                
                if subset[i] == 0:
                    break
            
            return False
        
        return dfs(0)