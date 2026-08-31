class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_so_far, best = prices[0], 0
        for p in prices:
            min_so_far = min(min_so_far, p)
            best = max(best, p - min_so_far)
        return best

        