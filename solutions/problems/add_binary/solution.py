class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        idxA = len(a) - 1
        idxB = len(b) - 1
        carry = 0
        while idxA >= 0 or idxB >= 0 or carry == 1:
            if idxA >= 0:
                carry += int(a[idxA])
                idxA -= 1
            if idxB >= 0:
                carry += int(b[idxB])
                idxB -= 1
            res.append(str(carry % 2))
            carry = carry // 2
        return ''.join(res[::-1])