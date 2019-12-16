# Problem URL: https://leetcode.com/problems/valid-parentheses

# Generic answer though
class Solution:
    def isValid(self, s: str) -> bool:
        closing = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        stack = []
        for i in range(len(s)):
            if (s[i] == '(' or s[i] == '[' or s[i] == '{'):
                stack.append(s[i])
            else:
                if len(stack) > 0:
                    last = stack.pop()
                    if (last != closing[s[i]]):
                        return False
                else:
                    return False

        return True if len(stack) == 0 else False
