class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = 0
        while(nums):
            a = nums.pop(0)
            b = target - a
            if b in nums:
                return [index, nums.index(b)+index+1]
            index += 1

    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums = nums, target= target))
