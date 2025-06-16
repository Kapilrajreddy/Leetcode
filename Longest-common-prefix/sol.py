from typing import List 
class Solution:
    def longestCommmonPrefix(self,arr:List[str])->str:
        if not arr:
            return ""
        
        arr.sort()
        first,last = arr[0],arr[-1]

        i=0
        while(i<len(first) and i<len(last) and first[i]==last[i]):
            i+=1 
        return first[:i]




class Solution1:
    def longestCommonPrefix1(self,arr:List[str])->str:
        if not arr:
            return ""
        
        pref = arr[0]
        pref_len = len(pref)

        for i in arr[1:]:
            while pref!=i[0:pref_len]:
                pref_len-=1 
                if(pref_len==0):
                    return ""
                pref = pref[0:pref_len]
        return pref
    
sol = Solution1()

# Call the method
result = sol.longestCommonPrefix1(["flower", "flow", "floight"])
print(result)  # Output: 'fl'