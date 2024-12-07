# https://leetcode.com/problems/is-subsequence/submissions/
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        elif len(t) == 0:
            return False

        i: int = 0
        j: int = 0
            
        while j < len(t):
            if s[i] == t[j]:
                i += 1
                
            if i == len(s):
                return True
            j += 1
        
        return False
