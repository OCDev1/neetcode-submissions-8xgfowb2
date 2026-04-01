class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def gen_par(cur_str:str, open_par:int, closed_par:int)->None:
            if len(cur_str) == 2*n:
                res.append(cur_str)
                return

            if open_par < n:
                gen_par(cur_str+"(", open_par+1, closed_par)
            if closed_par < open_par:
                gen_par(cur_str+")", open_par, closed_par+1)
        
        gen_par("", 0,0)
        
        return res