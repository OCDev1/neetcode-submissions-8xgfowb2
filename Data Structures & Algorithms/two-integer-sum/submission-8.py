class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = defaultdict(set)
        for i,num in enumerate(nums): 
            if num not in mydict:
                mydict[num] = []
            mydict[num].append(i)
        
        for j in range(len(nums)):
            comp = (target - nums[j])
            if comp in mydict:
                if comp == nums[j]:
                    if len(mydict[comp]) > 1:  # Only return the second index if it's different
                        return [j, mydict[comp][1]]
                else:
                    return [j, mydict[comp][0]]  
                     