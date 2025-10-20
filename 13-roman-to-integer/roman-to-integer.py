class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        value = 0
        i = 0

        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        while i<len(s):
            if i+1<len(s) and roman[s[i]] < roman[s[i+1]]:
                value += roman[s[i+1]] - roman[s[i]]
                i += 2
            else:
                value += roman[s[i]]
                i += 1
            
        return value

        