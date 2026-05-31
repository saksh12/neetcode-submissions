class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for i,v in enumerate(temperatures):
            while stack and v>temperatures[stack[-1]]:
                ind=stack.pop()
                res[ind]=i-ind
            stack.append(i)
        return res
        