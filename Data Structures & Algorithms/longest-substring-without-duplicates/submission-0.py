class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        mx_len = 0
        seenset = set()
        for r in range(len(s)):
            while s[r] in seenset:
                seenset.remove(s[l])
                l += 1
            seenset.add(s[r])
            mx_len = max(mx_len,r-l+1)
        return mx_len