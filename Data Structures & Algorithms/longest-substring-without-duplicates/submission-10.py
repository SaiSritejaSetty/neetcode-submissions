class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        current = 0
        s_dup = ''
        for x in s:
            if x not in s_dup:
                s_dup += x
                current = len(s_dup)
                longest = max(longest, current)
            elif x in s_dup:
                s_dup = s_dup[s_dup.index(x)+1:]
                s_dup += x
                current = len(s_dup)
        return longest