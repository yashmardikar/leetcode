class Solution:
    def average(self, salary: List[int]) -> float:
        min_sal = min(salary)
        max_sal = max(salary)
        total_sal = sum(salary)
        
        return (total_sal - min_sal - max_sal)/(len(salary)-2)