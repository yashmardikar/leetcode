class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        end = 0
        sliding_diff = 0
        while start<len(prices) and end<len(prices):
            if start==end:
                end += 1
                continue
            if prices[start] > prices[end]:
                #diff in negative, inc i
                start += 1
                continue
            diff = prices[end] - prices[start]
            sliding_diff = max(diff, sliding_diff)
            end += 1
        return sliding_diff

            
        