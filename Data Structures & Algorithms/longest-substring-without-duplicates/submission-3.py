class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s1=set()
        res=0
        l=0
        for r in range(0,len(s)):
            while s[r] in s1:
                s1.remove(s[l])
                l+=1
            s1.add(s[r])
            res=max(res,r-l+1)
        return res
    