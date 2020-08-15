def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    for index in range(0,len(nums)):
        current_number = nums[index]

        for addend_index in range(0,len(nums)):
            addend = nums[addend_index]
            if (addend_index != index) and (current_number + addend == target):
                    return [index,addend_index]

    return ['didnt work']
