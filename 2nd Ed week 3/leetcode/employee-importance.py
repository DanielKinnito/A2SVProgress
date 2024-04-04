"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp_map = defaultdict(list)
        for emp in employees:
            emp_map[emp.id] = [emp.importance, emp.subordinates]

        def dfs(emp_id):
            total_importance = emp_map[emp_id][0]
            
            for sub_id in emp_map[emp_id][1]:
                total_importance += dfs(sub_id)
            
            return total_importance
        
        return dfs(id)