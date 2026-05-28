class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for indx in range(len(nums)):
            diff = target - nums[indx]
            if diff in seen.keys():
                return [seen[diff],indx]
            seen[nums[indx]] = indx
        