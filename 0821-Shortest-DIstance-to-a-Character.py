class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        charIndices = []
        length = 0
        for index, char in enumerate(S):
            if char == C:
                charIndices.append(index)
                length += 1
        output = []
        minIndex = 0
        for index, char in enumerate(S):
            leftVal = abs(charIndices[minIndex] - index)
            if minIndex + 1 < length:
                rightVal = abs(charIndices[minIndex + 1] - index)
                if leftVal > rightVal:
                    output.append(rightVal)
                    minIndex += 1
                    continue
            output.append(leftVal)
        return output
