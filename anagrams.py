"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/submissions/
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

import collections

def findAnagrams(s, p):
    
    res = []
    pCount = collections.Counter(p)
    sCount = collections.Counter(s[:len(p)-1])
    
    # use sliding window to compare counts of each character
    for i in range(len(p)-1, len(s)):
        left = i - len(p) + 1
        sCount[s[i]] += 1
        if sCount == pCount:
            res.append(left)
        sCount[s[left]] -= 1
        if not sCount[s[left]]:
            del sCount[s[left]]
        
    return res

"""
Time: O(n1 + n2)
Space: O(1)
"""

s = "cbaebabacd"
p = "abc"
ans = findAnagrams(s, p)
print(ans)
    