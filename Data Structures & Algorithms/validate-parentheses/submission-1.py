class Solution:
    def isValid(self, s: str) -> bool:
        matching = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c not in matching:
                stack.append(c)
            else:
                if not stack or stack[-1] != matching[c]:
                    return False
                stack.pop()
        return not stack


if __name__ == "__main__":
    solution = Solution()
    # result = solution.isValid("[]")      # True
    # result = solution.isValid("([{}])")  # True
    # result = solution.isValid("[(])")    # False
    # result = solution.isValid("[])")     # False
    # result = solution.isValid("[)")      # False
    # result = solution.isValid(")]")      # False
    # result = solution.isValid("{]")      # False
    result = solution.isValid("{}")        # True
    print(result)
