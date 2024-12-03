# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/
class Solution:
    def is_increasing(self, nums: List[int], start: int, k: int) -> bool:
        end = start + k
        for i in range(start, end, 1):
            if nums[i] >= nums[i+1]:
                return False
        return True
        
    
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True 
        elif 2*k == len(nums):
             if self.is_increasing(nums, 0, k) and self.is_increasing(nums, k, k):
                return True           

        for i in range(len(nums)-(2*k)):
            if self.is_increasing(nums, i, k) and self.is_increasing(nums, i+k, k):
                return True
            
        return False
            
            
