class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x=Counter(nums)
        for k,v in x.items():
            if(v>1):
                return True
        return False
        