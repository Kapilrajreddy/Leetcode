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


class Solution:
    def romanToInt(self, s: str) -> int:
        romanNums = {"I" : 1, "V": 5, "X": 10, "L" : 50, "C": 100, "D": 500, "M" :1000}

        total = 0 
        i = 0

        #Subratraction rule because, CM = 900 but not 100+1000, smaller value first means subtract

        while i < len(s):
            if i + 1 < len(s) and romanNums[s[i]] < romanNums[s[i+1]]:
                total+= romanNums[s[i+1]] - romanNums[s[i]]
                i+=2
            else:
                total += romanNums[s[i]]
                i += 1
        return total


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        separate = []
        curr = ""
        temp = ""
        for char in s:
            if curr == "":
                curr = char
                temp = char
            else:
                curr = char
                if roman[curr] > roman[temp[len(temp)-1]]:
                    temp += char
                else:
                    separate.append(temp)
                    temp = curr
        separate.append(temp)
        sum = 0
        for term in separate:
            sum += roman[term]
        return sum

class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        res = 0
        r_d = {'I': 1, 'V':5, 'X':10, 'L':50, 'C': 100, 'D':500, 'M': 1000}
        lr = False
        i=0
        while i < n-1:
            curr = s[i]
            nxt = s[i+1]
            if r_d[curr] < r_d[nxt]:
                res += (r_d[nxt] - r_d[curr])
                i += 2    
            else:
                res += r_d[curr]
                i += 1
         
        if i == n-1:
            #last was not read
            res += r_d[s[-1]]
        return res    

class Solution:
    def romanToInt(self, s: str) -> int:
        s_original = s
        s = s.upper()
        roman_int = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        sum_int = 0
        while(True):
            if(len(s) == 1):
                sum_int += roman_int[s[0]]
                break
            if(len(s) < 1):
                break
            
            if(s[0] == 'M'):
                sum_int += roman_int[s[0]]
                s = s[1::]
                continue
            elif(s[0] == 'D'):
                if(s[1] == 'M'):
                    sum_int += roman_int[s[1]] - roman_int[s[0]]
                    s = s[2::]
                else:
                    sum_int += roman_int[s[0]]
                    s = s[1::]
                continue
            elif(s[0] == 'C'):
                if(s[1] == 'M' or s[1] == 'D'):
                    sum_int += roman_int[s[1]] - roman_int[s[0]]
                    s = s[2::]
                else:
                    sum_int += roman_int[s[0]]
                    s = s[1::]
                continue
            elif(s[0] == 'L'):
                if(s[1] == 'M' or s[1] == 'D' or s[1] == 'C'):
                    sum_int += roman_int[s[1]] - roman_int[s[0]]
                    s = s[2::]
                else:
                    sum_int += roman_int[s[0]]
                    s = s[1::]
                continue
            elif(s[0] == 'X'):
                if(s[1] == 'M' or s[1] == 'D' or s[1] == 'C' or s[1] == 'L'):
                    sum_int += roman_int[s[1]] - roman_int[s[0]]
                    s = s[2::]
                else:
                    sum_int += roman_int[s[0]]
                    s = s[1::]
                continue
            elif(s[0] == 'V'):
                if(s[1] == 'M' or s[1] == 'D' or s[1] == 'C' or s[1] == 'L' or s[1] == 'X'):
                    sum_int += roman_int[s[1]] - roman_int[s[0]]
                    s = s[2::]
                else:
                    sum_int += roman_int[s[0]]
                    s = s[1::]
                continue
            elif(s[0] == 'I'):
                if(s[1] == 'M' or s[1] == 'D' or s[1] == 'C' or s[1] == 'L' or s[1] == 'X' or s[1] == 'V'):
                    sum_int += roman_int[s[1]] - roman_int[s[0]]
                    s = s[2::]
                else:
                    sum_int += roman_int[s[0]]
                    s = s[1::]
                continue
            else:
                break
        
        return sum_int

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
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
        s = reversed(s)

        for char in s: 
            value = roman_map[char]
            if value < prev_value:
                total -= value
            else:
                total += value
                prev_value = value

        return total