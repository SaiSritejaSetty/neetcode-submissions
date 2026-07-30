class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s
        if len(s) < len(t):
            return ""
        t_1 = {}
        for x in range(len(t)):
            if t[x] in t_1:
                t_1[t[x]] += 1
            elif t[x] not in t_1:
                t_1[t[x]] = 1
        l = 0
        have = 0
        need = len(t_1)
        window = {}
        res = ""
        reslen = float("inf")
        for r in range(len(s)):
            if s[r] not in window:
                window[s[r]] = 1
                if s[r] in t_1:
                    if window[s[r]] == t_1[s[r]]:
                        have += 1
            elif s[r] in window:
                window[s[r]] += 1
                if s[r] in t_1:
                    if window[s[r]] == t_1[s[r]]:
                        have += 1
            while have == need:
                if (r - l + 1) < reslen:
                    res = s[l:r+1]
                    reslen = r - l + 1
                window[s[l]] -= 1
                if s[l] in t_1 and window[s[l]] < t_1[s[l]]:
                    have -= 1
                l += 1
        return res
                

        
