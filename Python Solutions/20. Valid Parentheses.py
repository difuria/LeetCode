# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        closing_brackets = { ")", "}", "]" }
        mapping = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        
        queue = []
        for p in s:
            if p in closing_brackets:
                if len(queue) == 0:
                    return False
                last_par = queue.pop()
                
                if last_par != mapping[p]:
                    return False
            else:
                queue.append(p)

        return len(queue) == 0
