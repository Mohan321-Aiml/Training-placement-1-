class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        index=0
        for i in nums:
            if i>target:
                return index
            index+=1
        if index==len(nums):
            return index
