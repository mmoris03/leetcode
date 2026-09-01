class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        total_profit = 0
        for i in range(1, len(prices)):
            buy_price = min(prices[i], buy_price)
            if prices[i] > prices[i - 1]:
                total_profit += prices[i] - buy_price
                buy_price = prices[i]
        return total_profit