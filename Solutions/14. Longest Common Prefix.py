# https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        
        if len(strs) == 0:
            return prefix
        elif len(strs) == 1:
            return strs[0]

        match = True
        for i in range(len(strs[0])):
            if len(strs[0]) <= i:
                break

            for s in strs[1:]:
                if len(s) <= i or s[i] != strs[0][i]:
                    match = False
                    break

            if not match:
                break
            
            prefix += s[i]
                
        return prefix
