class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l1=[]
        s1=""
        for i in range(0,len(s)):
            s1=""+s[i]
            for j in range(i+1,len(s)):
                if s[j] not in s1:
                    s1=s1+s[j]
                else:
                    break
            l1.append(len(s1))
        return max(l1) if l1 else 0
        
            



        