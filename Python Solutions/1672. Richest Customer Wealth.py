# https://leetcode.com/problems/richest-customer-wealth/
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = None
        
        for account in accounts:
            wealth = sum(account)
            if not max_wealth:
                max_wealth = wealth
            else:
                max_wealth = max(wealth, max_wealth)
        
        return max_wealth
