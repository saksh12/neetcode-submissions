class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l1=[]
        for i in range(0,len(nums)):
            res=1
            for j in range(0,len(nums)):
                if(i!=j):
                    res=res*nums[j]
            l1.append(res)
        return l1
            
        




        