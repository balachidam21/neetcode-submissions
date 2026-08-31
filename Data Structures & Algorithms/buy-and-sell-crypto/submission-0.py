class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = 0
        for i in range(len(prices)):
            buy_price = prices[i]
            max_profit_for_this_buy_price = 0
            for j in range(i+1, len(prices)):
                if prices[j] > prices[i]:
                    max_profit_for_this_buy_price = max(max_profit_for_this_buy_price, prices[j] - prices[i])
            profits = max(profits, max_profit_for_this_buy_price)
        return profits

        