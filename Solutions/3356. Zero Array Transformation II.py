# https://leetcode.com/problems/zero-array-transformation-ii/submissions/
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        N = len(nums)
        Q = len(queries)

        def is_zero_array(k: int) -> bool:
            f = [0] * (N + 1)
            
            for start, end, value in queries[:k]:
                f[start] += value
                f[end+1] -= value
                
            for i in range(1, N+1):
                f[i] += f[i-1]
                
            for i in range(N):
                if nums[i] > f[i]:
                    return False
            return True
        
        left = 0
        right = Q + 1
        while left < right:
            mid = (left + right) // 2
            
            if is_zero_array(mid):
                right = mid
            else:
                left = mid + 1
        
        if left == Q + 1:
            return -1
        return left
            
