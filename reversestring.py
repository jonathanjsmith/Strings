"""
https://leetcode.com/problems/reverse-string/
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
"""

def reverse(l, r, s):
    if l >= r:
        return
    s[l], s[r] = s[r], s[l]
    reverse(l+1, r-1, s)

def reverseString(s):
    reverse(0, len(s)-1, s)
    
"""
Time: O(n)
Space: O(1)
"""

s = ["h","e","l","l","o"]
reverseString(s)
print(s)
