class Solution:
    def countKeyChanges(self, s: str) -> int:
        lastUsed = s[0]
        changeCounter = 0

        lowerCase = s.lower()
        changeCounter = 0

        for i in range(1, len(lowerCase)):
            if lowerCase[i] != lowerCase[i-1]:
                changeCounter += 1
        return changeCounter