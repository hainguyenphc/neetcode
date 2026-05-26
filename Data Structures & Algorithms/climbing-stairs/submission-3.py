
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n # n elements
        def df(s):
            if s > n:
                return 0
            if cache[s] != -1:
                return cache[s]
            if s == n:
                return 1
            if s == (n - 1):
                return 1
            if s == (n - 2):
                return 2
            cache[s] = df(s + 1) + df(s + 2)
            return cache[s]
        return df(0)

solution = Solution()
print(solution.climbStairs(38))
print(solution.climbStairs(45))
