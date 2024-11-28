# https://leetcode.com/problems/zero-array-transformation-i/
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        temp = [0][:] * len(nums)
        
        for i, j in queries:
            temp[i] += 1

            upper_index = j + 1
            if upper_index < len(temp):
                temp[upper_index] -= 1
        
        count = 0
        for i in range(len(temp)):
            count += temp[i]
            temp[i] = count

        for i in range(len(temp)):
            if temp[i] < nums[i]:
                return False
        
        return True
