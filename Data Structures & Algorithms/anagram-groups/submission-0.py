class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bucket = defaultdict(list)
        res = []
        for word in strs:
            anaList = [0 for i in range(26)]
            for letter in word:
                anaList[ord(letter) - ord('a')] += 1
            bucket[tuple(anaList)].append(word)
        for val in bucket.values():
            res.append(val)
        return res