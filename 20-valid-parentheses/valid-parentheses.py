class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        brack = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in brack.values():
                stack.append(char)
            else: 
                if not stack or stack[-1] != brack[char]:
                    return False 
                stack.pop()

        return not stack

            
        