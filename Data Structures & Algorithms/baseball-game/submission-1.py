class Solution:
    def calPoints(self, operations: list[str]) -> int:
        _stack = []
        for op in operations:
            try:
                score = int(op)
                _stack.append(score)
            except ValueError:
                if op == "C":
                    _stack.pop()
                elif op == "D":
                    prev_score = int(_stack[-1])
                    _stack.append(prev_score * 2)
                elif op == "+":
                    prev_score1 = int(_stack[-1])
                    prev_score2 = int(_stack[-2])
                    _stack.append(prev_score1 + prev_score2)

        sum = 0
        for score in _stack:
            sum = sum + score
        return sum


print(__name__)
if __name__ == "__main__":
    # operations = ["5", "2", "C", "D", "+"]
    # operations = ["1", "2", "+", "C", "5", "D"]
    # operations = ["5", "D", "+", "C"]
    operations = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    solution = Solution()
    total_score = solution.calPoints(operations)
    print(total_score)
