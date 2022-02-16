class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start, end = 0, 1
        maxProfit = 0
        
        while end < len(prices):
            if prices[start] < prices[end]:
                #profitable transaction
                currProfit = prices[end] - prices[start]
                maxProfit = max(maxProfit, currProfit)
            else:
                #start changes only when next min is found
                start = end
            end += 1
        return maxProfit