class Solution:
    '''
    Accepted on leetcode(8)
    time - O(N)
    space - O(1)
'''

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # trim the extra spaces on right and left of string
        str = str.strip()
        retVal = 0

        # edge case
        # 1. length of string is 0 return 0
        # 2. if first character is not number and not (+,-)sign then return 0.
        if len(str) == 0 or (not str[0].isnumeric() and str[0] != '-' and str[0] != '+'):
            return retVal

        # if first element is '-' then take it as '-' else '+'
        sign = '-' if str[0] == '-' else '+'

        for i in range(len(str)):
            ch = str[i]

            # if first char is numeric, following edge cases about max limit.
            if ch.isnumeric():
                # go to next digit by multiplying current with 10 and add next digit.
                retVal = retVal * 10 + int(ch)

                # check for out of bounds
                if retVal >= 2147483648 and sign == '-':
                    return -2147483648
                elif retVal >= 2147483647 and sign == '+':
                    return 2147483647

            # as first character can be '-' sign , so we can only break after first char.
            elif i != 0:
                break
        # check signs
        if sign == '-':
            return -retVal
        else:
            return retVal