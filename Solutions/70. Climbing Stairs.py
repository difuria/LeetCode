# https://leetcode.com/problems/climbing-stairs/submissions/
class Solution:
    found_steps = {}
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        elif n < 0:
            return 0

        if n in self.found_steps:
            return self.found_steps[n]
        
        self.found_steps[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.found_steps[n] 
