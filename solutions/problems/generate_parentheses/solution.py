class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def genP(openP, closeP, s):
            if openP == closeP and openP + closeP == n * 2:
                result.append(s)
                return
            if openP < n:
                genP(openP + 1, closeP, s + "(")
            if closeP < openP:
                genP(openP, closeP + 1, s + ")")
        
        genP(0, 0, "")
        return result
