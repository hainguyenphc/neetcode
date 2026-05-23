class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = list()
        for i in range(0, 2):
            for num in nums:
                ans.append(num)
        return ans


# nums = [1, 4, 2]
# solution = Solution()
# ans = solution.getConcatenation(nums)
# print(ans)
