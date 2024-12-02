# https://leetcode.com/problems/find-the-difference/
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t_dictionary = {}
        for letter in t:
            if not letter in t_dictionary:
                t_dictionary[letter] = 0
            
            t_dictionary[letter] += 1
        
        for letter in s:
            if not letter in t_dictionary:
                return letter
            else:
                t_dictionary[letter] -= 1
            
            if t_dictionary[letter] == 0:
                t_dictionary.pop(letter)
        
        return list(t_dictionary.keys())[0]
          
