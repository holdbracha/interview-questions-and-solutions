# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

#  Example 1:
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

# Example 2:
# Input: s = "aa", p = "*"
# Output: true
# Explanation: '*' matches any sequence.

# Example 3:
# Input: s = "cb", p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

# Example 4:
# Input: s = "adceb", p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

# Example 5:
# Input: s = "acdcb", p = "a*c?b"
# Output: false

# https://leetcode.com/explore/interview/card/top-interview-questions-hard/119/backtracking/855/

def isMatch(s, p):
    if len(s)==0 and p=='*' * len(p):
        return True
    if len(p)==0 or len(s)==0:
        return False
    if p[0] == '?' or p[0] == s[0]:
        return isMatch(s[1:], p[1:])
    if p[0] == '*':
        j = 1
        while(j<len(p) and p[j]=='*'):
            j+=1
        for i in range(len(s)+1):
            if isMatch(s[i:], p[j:]):
                return True
    return False