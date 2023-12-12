class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        """
        1- find the even sum first then add or remove based on the next steps
        2- Iterate through the second array and for every element
            - add the first number on an index of the second number in the
                first array
        3- append to answer list
        """
        answer = []
        even_sum = sum([num for num in nums if num % 2 == 0])
        
        for query in queries:
            
            if nums[query[1]] % 2 == 0:
                even_sum -= nums[query[1]]
            
            nums[query[1]] += query[0]

            if (nums[query[1]]) % 2 == 0:
                
                even_sum += nums[query[1]]
                
            answer.append(even_sum)
        
        return answer