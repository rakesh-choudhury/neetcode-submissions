class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        count = {}
        res = []
        for j in range(len(nums)):
            count[nums[j]] = count.get(nums[j],0) + 1
        # print(count)
        for key, val in count.items():
            bucket[val].append(key)
        # print(bucket)
        for arr in range(len(bucket)-1,0,-1):
            # bucket[arr]
            for number in bucket[arr]:
                res.append(number)
                print(res)
                if len(res) == k:
                    return res