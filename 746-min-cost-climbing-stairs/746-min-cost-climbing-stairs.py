class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #bottom up approch (tabulation)
        dp = [cost[0], cost[1]] + [0]*(len(cost)-2)
        for i in range(2,len(cost)):
            dp[i] = min(cost[i] + dp[i-1], cost[i] + dp[i-2])
            
        print(dp)
        return min(dp[-1], dp[-2])