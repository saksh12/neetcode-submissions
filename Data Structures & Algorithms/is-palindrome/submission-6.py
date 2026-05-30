class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2=s.lower()
        s1=''.join(s2.split())
        s3=""
        for c in s1:
            if c.isalnum():
                s3=s3+c
        print(s3)
        if(s3[::]==s3[::-1]):
            return True
        else:
            return False
        


       
        

        