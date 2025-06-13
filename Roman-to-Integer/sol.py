class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i] == "I" and s[i + 1] == "V":
                total += 4
                i += 2
            elif i + 1 < len(s) and s[i] == "I" and s[i + 1] == "X":
                total += 9
                i += 2
            elif i + 1 < len(s) and s[i] == "X" and s[i + 1] == "L":
                total += 40
                i += 2
            elif i + 1 < len(s) and s[i] == "X" and s[i + 1] == "C":
                total += 90
                i += 2
            elif i + 1 < len(s) and s[i] == "C" and s[i + 1] == "D":
                total += 400
                i += 2
            elif i + 1 < len(s) and s[i] == "C" and s[i + 1] == "M":
                total += 900
                i += 2
            else:
                if s[i] == "I":
                    total += 1
                elif s[i] == "V":
                    total += 5
                elif s[i] == "X":
                    total += 10
                elif s[i] == "L":
                    total += 50
                elif s[i] == "C":
                    total += 100
                elif s[i] == "D":
                    total += 500
                elif s[i] == "M":
                    total += 1000
                i += 1
        return total

#method-2
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        for i in range(len(s) - 1, -1, -1):
            current_value = roman[s[i]]
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            prev_value = current_value
            
        return total
