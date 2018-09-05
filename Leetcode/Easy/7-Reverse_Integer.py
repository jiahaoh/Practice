class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x in range(-2**31, 2**31-1):
            num_s = str(x)
            if num_s.startswith("-"):
                num_r = num_s[::-1]
                num_o = "-"+num_r[:-1]
                return int(num_o)
            else:
                num_o = num_s[::-1]
                return int(num_o)
        else:
            return 0

???