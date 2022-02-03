"""
https://leetcode.com/problems/permutation-in-string/
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.
"""

import collections

def checkPermutation(s1, s2):
    
    s1Count = collections.Counter(s1)
    s2Count = collections.Counter(s2[:len(s1)-1])
    
    for i in range(len(s1)-1, len(s2)):
        left = i - len(s1) + 1
        s2Count[s2[i]] += 1
        if s1Count == s2Count:
            return True
        s2Count[s2[left]] -= 1
        if s2Count[s2[left]] == 0:
            del s2Count[s2[left]]
            
    return False

"""
Time: O(n1 + n2)
Space: O(1)
"""

s1 = "ab"
s2 = "eidbaooo"
ans = checkPermutation(s1, s2)
print(ans)
