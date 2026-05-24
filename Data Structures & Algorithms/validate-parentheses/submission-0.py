class Solution:
    def isOpenParenthesis(self, parenthesis: str) -> bool:
        return parenthesis == "[" or parenthesis == "(" or parenthesis == "{"

    def validClosingParenthesis(self, openParenthesis: str) -> str:
        if openParenthesis == "[":
            return "]"
        elif openParenthesis == "(":
            return ")"
        elif openParenthesis == "{":
            return "}"

    def isValid(self, s: str) -> bool:
        _stack = []
        for parenthesis in s:
            if self.isOpenParenthesis(parenthesis):
                _stack.append(parenthesis)
            else:
                if len(_stack) == 0:
                    return False
                poppedParenthesis = _stack.pop()
                if self.validClosingParenthesis(poppedParenthesis) != parenthesis:
                    return False
        if len(_stack) > 0:
            return False
        return True


if __name__ == "__main__":
    solution = Solution()
    # result = solution.isValid("[]") # True
    # result = solution.isValid("([{}])") # True
    # result = solution.isValid("[(])") # False
    # result = solution.isValid("[])") # False
    # result = solution.isValid("[)") # False
    # result = solution.isValid(")]") # False
    result = solution.isValid("{]")  # False
    # result = solution.isValid("{}")  # False
    print(result)
