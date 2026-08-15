class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for i in strs:
            x=len(i)
            encoded=encoded+str(x)+"#"+i
        return encoded

    def decode(self, s: str) -> List[str]:
        result=[]
        s1=""
        i=0
        while(i<len(s)):
            j=i

            while(s[j]!="#"):
                j+=1
            
            num=int(s[i:j])

            s1=s[j+1:j+1+num]
            result.append(s1)
            i=j+1+num
        return result








