# https://leetcode.com/problems/merge-strings-alternately/
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_word = ""
        word1 = list(word1)
        word2 = list(word2)
        while word1 or word2:
            if word1:
                merged_word += word1.pop(0)
            if word2:
                merged_word += word2.pop(0)
        
        return merged_word
