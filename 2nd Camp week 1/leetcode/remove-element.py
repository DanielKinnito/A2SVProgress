class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        holder = 0
        while holder < n and nums[holder] != val:
            holder += 1
        
        if holder == n:
            return n
        
        for seeker in range(holder + 1, n):
            if nums[seeker] != val:
                nums[holder] = nums[seeker]
                holder += 1
                
        return holder