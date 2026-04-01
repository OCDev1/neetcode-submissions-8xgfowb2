class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)

            elif c == ")" or c == "]" or c == "}":
                if not stack:
                    return False
                
                openpar = stack.pop()
                if (c == ")" and openpar != "(") or (c == "]" and openpar != "[") or (c == "}" and openpar != "{"):
                    return False

        return not stack