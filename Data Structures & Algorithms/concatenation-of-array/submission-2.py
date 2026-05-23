# class Solution:
#     def getConcatenation(self, nums: list[int]) -> list[int]:
#         ans = list()
#         for i in range(0, 2):
#             for num in nums:
#                 ans.append(num)
#         return ans

# class Solution:
#     def getConcatenation(self, nums: list[int]) -> list[int]:
#         return nums * 2

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        tmp = []
        for i in nums:
            tmp.append(i)
        
        for t in tmp:
            nums.append(t)
        
        return nums


# nums = [1, 4, 2]
# solution = Solution()
# ans = solution.getConcatenation(nums)
# print(ans)
