class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        for p in s:
            if p in mapping:
                if not stack or stack[-1] != mapping[p]:
                    return False
                stack.pop()
            else:
                stack.append(p)
        return not stack