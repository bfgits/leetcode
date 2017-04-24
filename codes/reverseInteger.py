#!/usr/bin/env python
#-*- coding: UTF-8 -*-
# Author: 'binfeng'
# Date:  4/24/17 
# License Type: GNU GENERAL PUBLIC LICENSE, Version 3


'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321


Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.


'''


class Solution(object):
    def reverse(self, s):
        """
        :type x: int
        :rtype: int
        """
        if not isinstance(s, int):
            return False
        s1 = str(s)
        print(s1)
        if s < 0:
            return - int(s1[::-1][:-1])
        elif s == 0:
            return 0
        else:
            return int(s1[::-1])


if __name__ == '__main__':
    s = Solution()
    s1 = s.reverse(-500389000340000)
    print(s1)