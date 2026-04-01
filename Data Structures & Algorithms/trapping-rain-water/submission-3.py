class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        max_l, max_r = 0, 0
        if len(height) == 0:
            return 0
        
        else:
            l, r = 0, len(height)-1
            while l < r:
                max_l=max(max_l, height[l])
                max_r = max(max_r, height[r])

                if max_l >= max_r:
                    answer += max_r - height[r]
                    r -= 1
                else:
                    answer += max_l - height[l]
                    l += 1
                    
            return answer