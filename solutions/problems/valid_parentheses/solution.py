class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(': ')', '{': '}', '[': ']'}
        for e in s:
            if e in pairs:
                stack.append(e)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if pairs[top] != e:
                    return False
        return not stack
                