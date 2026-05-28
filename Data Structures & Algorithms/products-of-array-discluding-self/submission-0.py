class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        res = [1 for _ in range(len(nums))]
        for idx in range(len(nums)):
            res[idx] *= pre
            pre *= nums[idx]
        print(res)
        post = 1
        for idx2 in range(len(nums)-1,-1,-1):
            res[idx2] *= post
            post *= nums[idx2]
        return res
            