#!/usr/bin/env python
#-*- coding: UTF-8 -*-
# Author: 'binfeng'
# Date:  4/24/17 
# License Type: GNU GENERAL PUBLIC LICENSE, Version 3


'''

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example
Given num = 38.
The process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return 2.

'''

class Solution:
    # @param {int} num a non-negative integer
    # @return {int} one digit
    def addDigits(self, num):
        # Write your code here
        while True:
            s1 = str(num)
            number = 0
            for i in s1:
                number = number + int(i)
            if number <10:
                return number
            else:
                num = number
                return self.addDigits(number)



if __name__ == '__main__':
    s = Solution()
    print(s.addDigits(99987))