# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        
        queue = []
        for p in s:
            if p in mapping:
                if len(queue) == 0:
                    return False
                last_par = queue.pop()
                
                if last_par != mapping[p]:
                    return False
            else:
                queue.append(p)

        return len(queue) == 0
