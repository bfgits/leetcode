#!/usr/bin/env python
#-*- coding: UTF-8 -*-
# Author: 'binfeng'
# Date:  4/24/17 
# License Type: GNU GENERAL PUBLIC LICENSE, Version 3

'''
Problem description

Total Accepted: 483443
Total Submissions: 1485559
Difficulty: Easy
Contributor: LeetCode
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].


'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)<=1:
            return False

        tmpList = []
        for i in nums:
            if i <= target:
                tmpList.append(i)

        for litteNumber in tmpList:
            tmpList.remove(litteNumber)
            if target - litteNumber in tmpList:
                print([nums.index(litteNumber),nums.index(target - litteNumber)])
                return [nums.index(litteNumber),nums.index(target - litteNumber)]
            else:
                continue

        return -1, -1

    def twoSum2(self,nums,target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i



if __name__ == '__main__':
    s = Solution()
    s.twoSum2([3,4,3,5,5,2], 6)