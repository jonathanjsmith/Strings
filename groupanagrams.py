"""
https://leetcode.com/problems/group-anagrams/
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

import collections

def groupAnagrams(strs):
    
    groups = collections.defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        groups[tuple(count)].append(s)
        
    return [groups[g] for g in groups]

"""
Time: O(n*k)
Space: O(1)
"""

strs = ["eat","tea","tan","ate","nat","bat"]
ans = groupAnagrams(strs)
print(ans)
