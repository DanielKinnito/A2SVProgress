class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        n = len(skill)

        if n == 2:
            return skill[0] * skill[1]

        # elif sum(skill) % 2 != 0:
        #     return -1

        else:
            skill.sort()
            chemistry_sum = 0
            check = []

            for i in range(n // 2):
                check.append(skill[i] + skill[n - i - 1])
                chemistry_sum += skill[i] * skill[n - i - 1]
            check.sort()
            validate = all(x == check[0] for x in check)
            if not validate:
                return -1
            else:
                return chemistry_sum