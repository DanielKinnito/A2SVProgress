class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        answer = []
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                answer.append(nums1[i])
                nums1.pop(i)
                nums2.pop(j)
            
            elif nums1[i] < nums2[j]:
                i += 1
            
            else:
                j += 1

        return answer