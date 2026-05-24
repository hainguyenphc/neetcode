class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            elif not stack or stack[-1] != c:
                return False
            else:
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
