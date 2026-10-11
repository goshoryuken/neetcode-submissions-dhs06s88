class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = prices[0]
        max_profit = 0

        for price in prices:
            cheapest = min(cheapest, price)
            max_profit = max(price - cheapest, max_profit)
            
        return max_profit

        