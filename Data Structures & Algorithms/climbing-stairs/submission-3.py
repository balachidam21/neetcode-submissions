class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=2:
            return n
        dp = [0] * (n+1) # dp[i] represents the no. of ways to reach step ith step
        dp[1], dp[2] = 1, 2 #base case: dp[0] = 0 -> 0 ways to reach 0 steps; dp[1] = 1 -> one way to reach 1st step; dp[2] = 2 -> two ways to reach 2nd step (1,1 | 2)
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[-1]
        # cache = [-1] * n
        # def dfs(i):
        #     if i >=n:
        #         return i == n
        #     if cache[i] != -1:
        #         return cache[i]
        #     cache[i] =  dfs(i+1) + dfs(i+2)
        #     return cache[i]
        # return dfs(0)