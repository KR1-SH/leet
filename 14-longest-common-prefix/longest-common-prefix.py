class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        pre = ""
        small = min(strs, key=len)
        
        for i in range(len(small)):
            char = small[i]
            
            for word in strs:
                if word[i] != char:
                    return pre
            
            pre += char
        
        return pre