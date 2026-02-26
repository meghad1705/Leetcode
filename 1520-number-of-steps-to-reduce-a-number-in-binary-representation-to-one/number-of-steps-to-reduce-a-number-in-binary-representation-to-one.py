class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
       

        steps = 0
        s = list(s)

        while len(s) > 1:

            # EVEN → divide by 2
            if s[-1] == '0':
                s.pop()

            # ODD → add 1
            else:
                i = len(s) - 1

                # handle carry
                while i >= 0 and s[i] == '1':
                    s[i] = '0'
                    i -= 1

                # if carry goes outside
                if i < 0:
                    s.insert(0, '1')
                else:
                    s[i] = '1'

            steps += 1

        return steps
