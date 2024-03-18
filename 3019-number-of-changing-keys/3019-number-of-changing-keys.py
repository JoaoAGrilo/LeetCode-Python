class Solution:
    def countKeyChanges(self, s: str) -> int:
        lastUsed = s[0]
        changeCounter = 0

        lowerStr = s.lower()
        lastUsed = lowerStr[0]
        changeCounter = 0

        for i in range(1, len(lowerStr)):
            if lowerStr[i] != lastUsed:
                changeCounter += 1
            lastUsed = lowerStr[i]
        return changeCounter