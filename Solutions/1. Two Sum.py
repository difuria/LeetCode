# https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        locations = {}

        for i, num1 in enumerate(nums):
            needed = target - num1
            if needed in locations:
                return [locations[needed], i]
            
            locations[num1] = i
        
