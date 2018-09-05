class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        seq = str(x)
        if len(seq) == 1:
            return True
        else:
            if seq.startswith("-") or seq.endswith("0"):
                return False
            else:
                if seq == seq[::-1]:
                    return True
                else:
                    return False

#########

return str(abs(x))[::-1] == x