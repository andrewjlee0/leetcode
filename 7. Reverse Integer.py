def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        s = str(x)[::-1]

        if s[-1] == '-':
            s = '-' + s.replace('-','')

        return 0 if int(s) < -(2**31) or int(s) > 2**31 - 1 else int(s)
