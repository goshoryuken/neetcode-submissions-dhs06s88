class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        buy = 0
        sell = buy + 1

        smallest_buy = 1000000000000000000

        while sell < len(prices):
            
            while buy < sell:
        
                current_buy = prices[buy]
                smallest_buy = min(prices[buy], smallest_buy)
                buy += 1
            current_profit = prices[sell] - smallest_buy
            profit = max(current_profit, profit)
            sell += 1;

        return profit

        