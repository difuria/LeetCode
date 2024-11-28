# https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        current_majority = None
        for num in nums:
            if not num in count:
                count[num] = 0
            count[num] += 1
            
            if not current_majority or count[num] > count[current_majority]:
                current_majority = num
        
        return current_majority
