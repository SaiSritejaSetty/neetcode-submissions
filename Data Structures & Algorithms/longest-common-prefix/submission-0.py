class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs:
            common = strs[0]
        else:
            return ""
        count = 0
        for i in range(len(common)):
            for s in strs:
                if i < len(s) and common[i] == s[i]:
                    continue
                else:
                    return common[:count]
            count += 1
        return common[:count]
