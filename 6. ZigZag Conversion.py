def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        # special case known to me by my daddy
        if numRows == 1:
            return s

        # row assignments
        l = []

        # counter
        row = 1

        # increase or decrease
        updown = 'increase'

        # create row assignments
        for char in s:
            l.append( (char,row) )

            if row == numRows:
                updown = 'decrease'
            elif row == 1:
                updown = 'increase'

            if updown == 'increase':
                row += 1
            else:
                row -= 1

        # get list of keys for each row num and append to str
        ans = ''
        for num in range(1, numRows+1):
            for char,row in l:
                if row==num:
                    ans += char

        return ans
