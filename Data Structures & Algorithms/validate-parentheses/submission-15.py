class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        if len(s) == 0:
            return True

        mySet = {}
        mySet['}'] = '{'
        mySet[')'] = '('
        mySet[']'] = '['
        
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if not stack:
                    return False
                tmp = stack.pop()
                if tmp != mySet[c]:
                    return False
        
        return not stack
            