class Solution:
    def romanToInt(self,s:str) -> int:
        strList = list(s)
        integer = 0
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        if(len(strList) == 1):
            return roman_map[strList[0]]
        i = 0
        while(i <= len(strList) - 1):
            if(i == len(strList) - 1):
                integer += roman_map[strList[i]]
                break
            j = i + 1
            if(roman_map[strList[i]] >= roman_map[strList[j]]):
                integer += roman_map[strList[i]]
            else:
                integer += roman_map[strList[j]] - roman_map[strList[i]]
                i += 2
                continue
            i += 1
        return integer