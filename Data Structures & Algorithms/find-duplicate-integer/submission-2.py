class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            fast = nums[nums[fast]]     # move 2 steps forward
            slow = nums[slow]       # move 1 step forward
            if nums[slow] == nums[fast]:    # anacdotally to LL, this means slow.next == fast.next
                break   # the 2 different ptrs are on the same index, meaning there is a cycle
        slow2 = 0
        while True:     # finding the entrance to the cycle (the duplicate value)
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow     # the distance from the start to the entrance of the cycle will always equal
                                # the distance from the meeting point of slow & fast to the entrance of the cycle
            