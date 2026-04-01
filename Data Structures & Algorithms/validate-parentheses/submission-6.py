class Solution:
    def isValid(self, s: str) -> bool:
        par_map = {"(" : ")" , "[":"]" , "{":"}"}
        stack = []

        for p in s:
            if p == "{" or p == "(" or p == "[":
                stack.append(p)
            else:
                if stack and p == par_map[stack.pop()]:
                    continue
                else:
                    return False
        if not stack:
            return True
        return False