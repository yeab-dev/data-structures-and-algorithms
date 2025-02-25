from typing import List
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for operation in operations:
            if operation.isnumeric():
                result.append(int(operation))
            elif operation == "C":
                result.pop()
            elif operation.startswith("-"):
                result.append(-int(operation[1:]))
            elif operation == "+":
                result.append(result[-1] + result[-2])
            else:
                result.append(result[-1] * 2)
        return sum(result)
