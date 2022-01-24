"""
https://leetcode.com/problems/detect-capital/solution/
We define the usage of capitals in a word to be right when one of the following cases holds:
    1. All letters in this word are capitals, like "USA".
    2. All letters in this word are not capitals, like "leetcode".
    3. Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.
"""

# Case 1: spiderman
# Case 2: Spiderman
# Case 3: SPIDERMAN
def correctUse(word):
    
    if len(word) == 1:
        return True
    
    # case 3
    if word[0].isupper() and word[1].isupper():
        for i in range(2, len(word)):
            if word[i].islower():
                return False
        return True
    # case 1 and 2
    else:
        for i in range(1, len(word)):
            if word[i].isupper():
                return False
        return True
    
    
"""
Time: O(n)
Space: O(1)
"""

word = "USA"
ans = correctUse(word)
print(ans)

word = "FlaG"
ans = correctUse(word)
print(ans)