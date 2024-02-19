class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        idx_map = {}
        for i in range(len(nums)):
            if nums[i] not in idx_map:
                idx_map[nums[i]] = [i]
            else:
                idx_map[nums[i]].append(i)

        answer = [0] * len(nums)
        
        for indices in idx_map.values():
            n = len(indices)
            total_distance = sum(indices)
            if n > 1:
                prefix = [0] * n
                suffix = [0] * n
                # temp = [0] * n

                prefix[0] = 0
                for i in range(1, n):
                    prefix[i] = prefix[i - 1] + i* (indices[i] - indices[i - 1])
                
                suffix[n - 1] = 0
                for i in range(n - 2, -1, -1):
                    suffix[i] = suffix[i + 1] + (n - 1 - i)* (indices[i + 1] - indices[i])
                
                for i in range(n):
                    answer[indices[i]] = prefix[i] + suffix[i]

        return answer