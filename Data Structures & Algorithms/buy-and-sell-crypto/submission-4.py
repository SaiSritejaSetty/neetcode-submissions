class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 10
        best_profit = 0
        today_profit = 0
        for x in range(len(prices)):
            if prices[x] <= profit:
                profit = prices[x]
            elif prices[x] > profit:
                today_profit = prices[x] - profit
                best_profit = max(best_profit, today_profit)
        return best_profit

        
