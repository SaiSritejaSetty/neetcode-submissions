class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = 0
        freq = {}
        for r in range(len(s)):
            if s[r] in freq:
                freq[s[r]] +=1
            elif s[r] not in freq:
                freq[s[r]] = 1 
            change = (r-l+1) - max(freq.values())
            if change <= k:
                count = max(count, r-l+1)
            elif change > k:
                freq[s[l]] -= 1
                l+=1
                
                
        return count
