class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs != []:
            min_seq = min(strs, key = len)
            search_l = []
            for i in range (0, len(min_seq)+1):
                search = min_seq[0:i]
                num = 0
                for seq in strs:
                    if seq.startswith(search):
                        num += 1
                    else:
                        pass
                if num == len(strs):
                    search_l.append(search)
            if len(search_l) > 0 :
                return max(search_l, key = len)
            else:
                return ""
        else:
                return ""