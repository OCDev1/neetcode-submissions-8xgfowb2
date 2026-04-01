class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        my_map = {
            "2":("a","b","c"),
            "3":("d","e","f"),
            "4":("g","h","i"),
            "5":("j","k","l"),
            "6":("m","n","o"),
            "7":("p","q","r","s"),
            "8":("t","u","v"),
            "9":("w","x","y","z")
            }

        res = []

        def helper(i, cur_str):  # i = digit
            if i == len(digits):
                res.append(cur_str)
                return

            for letter in my_map[digits[i]]:    # call with all options for appended letter
                helper(i+1, cur_str + letter)   # append current letter option and recurse
                # Note: we dont need to pop or undo the appending beacuse in python "cur_str + letter" creates a new string
        
        # run the function
        helper(0,"")
        
        return res
    