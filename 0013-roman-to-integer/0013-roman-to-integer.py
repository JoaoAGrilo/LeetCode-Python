class Solution:
    def romanToInt(self, s: str) -> int:   
         
        highestValue = 0
        output = 0

        symbolMap = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }

        for i in range(len(s)-1, -1, -1):
            if symbolMap[s[i]] >= highestValue:
                highestValue = symbolMap[s[i]]
                output += symbolMap[s[i]]
            else:
                output -= symbolMap[s[i]]
        return output
        