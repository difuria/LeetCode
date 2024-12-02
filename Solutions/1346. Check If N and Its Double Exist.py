# https://leetcode.com/problems/check-if-n-and-its-double-exist/
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        memory = {}
        for index, num in enumerate(arr):
            memory[num] = index
        
        for index, num in enumerate(arr):
            double = (num * 2)
            if not double in memory:
                continue

            if index != memory[double]:
                return True
        
        return False
