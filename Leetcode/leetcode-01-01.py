#!/usr/bin/python
# Author: Karthick Kumaran <asvkarthick@gmail.com>

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = []
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                ret.append(dict.get(nums[i], 0))
                ret.append(i)
            else:
                dict[target - nums[i]] = i
        return ret

s = Solution()
print s.twoSum([2, 4, 6], 8)
