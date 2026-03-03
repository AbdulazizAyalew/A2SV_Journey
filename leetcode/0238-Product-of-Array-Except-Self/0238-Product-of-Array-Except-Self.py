class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pref = []
        mult = 1
        for i in range(len(nums)):
            pref.append(mult)
            mult *= nums[i]
        
        suff = [0] * len(nums) 
        mult = 1
        for j in range(len(nums)-1, -1 , -1):
            suff[j] = mult
            mult *= nums[j]


        res = []
        for i in range(len(nums)):
            res.append(suff[i] * pref[i])

        return res