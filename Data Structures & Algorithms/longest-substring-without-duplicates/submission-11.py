class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        current = 0
        count = {}
        for x in range(len(s)):
            if s[x] not in count:
                count[s[x]] = x
                current = x-l+1
                longest = max(current, longest)
            elif s[x] in count:
                l = max(l, count[s[x]] + 1)
                count[s[x]] = x
                current = x-l+1
                longest = max(current, longest)
        return longest 

