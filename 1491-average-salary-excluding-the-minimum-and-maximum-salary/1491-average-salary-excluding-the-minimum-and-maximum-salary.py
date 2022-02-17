class Solution:
    def average(self, salary: List[int]) -> float:
        min_sal = float("inf")
        max_sal = 0
        running_sum = 0
        
        for sal in salary:
            print(min_sal, max_sal, running_sum)
            if sal < min_sal:
                min_sal = sal
            if sal > max_sal:
                max_sal = sal
            running_sum += sal
        return (running_sum-(min_sal+max_sal))/(len(salary)-2)
            
            