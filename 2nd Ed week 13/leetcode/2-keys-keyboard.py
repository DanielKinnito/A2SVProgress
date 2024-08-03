class Solution:
  def minSteps(self, n: int) -> int:
    curr = 1
    temp = 0
    answer = 0

    while curr < n:
        if n % curr == 0:
            temp = curr
            answer += 1
        
        curr += temp
        answer += 1

    return answer