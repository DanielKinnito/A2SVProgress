class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        end = len(arr)
        answer = []

        for _ in range(len(arr)):
            max_idx = arr.index(end) + 1

            if 1 < max_idx and max_idx < end:
                segment = arr[0: max_idx]
                segment.reverse()
                arr[:max_idx] = segment

                end_segment = arr[:end]
                end_segment.reverse()
                arr[:end] = end_segment

                answer.append(max_idx)
                answer.append(end)
            
            elif max_idx == 1:
                end_segment = arr[:end]
                end_segment.reverse()
                arr[:end] = end_segment

                answer.append(end)
            end -= 1
        
        return answer