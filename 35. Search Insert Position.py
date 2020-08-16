def searchInsert(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    for i in range(len(nums)):
        if nums[i] == target or nums[i] > target:
            return i
        elif i == len(nums) - 1:
            return i + 1
