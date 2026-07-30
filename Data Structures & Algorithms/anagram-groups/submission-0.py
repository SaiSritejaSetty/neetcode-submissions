class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      g = {}
      for i in strs:
        h = "".join(sorted(i))
        if h not in g:
          g[h] = []
        
        g[h].append(i)
      
      return list(g.values())
            
                 