"""
https://leetcode.com/problems/remove-k-digits/
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.
"""

"""
Algorithm
1. pop stack if greater than next num (max of k times)
2. remove at least k digits
"""

def removeKdigits(num, k):
    
    s = []
    for n in num:
        while k and s and s[-1] > n:
            s.pop()
            k -= 1
        s.append(n)
        
    s = s[:-k] if k else s
    return ''.join(s).lstrip('0') or '0'

"""
Time: O(n)
Space: O(n)
"""

num = "1432219"
k = 3
ans = removeKdigits(num, k)
print(ans)

    
    