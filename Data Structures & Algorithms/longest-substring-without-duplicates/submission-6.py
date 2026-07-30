class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_duplicate = ''
        length = 0
        best_length = 0
        for x in range(len(s)):
            if s[x] not in s_duplicate:
                s_duplicate+=s[x]
                length+=1
                best_length = max(length, best_length)
            elif s[x] in s_duplicate:
                length = 0
                s_duplicate = s_duplicate[s_duplicate.index(s[x]) + 1:]
                s_duplicate+= s[x]
                length+= len(s_duplicate)
        return best_length
