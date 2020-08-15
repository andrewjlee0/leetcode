def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0:
            return 0
        elif len(str) == 1:
            return int(str[0]) if str[0].isdigit() else 0

        # index of first non-whitespace char
        start = 0
        for i in range(len(str)):
            if str[i] != ' ':
                start = i
                break

        # get answer
        condition1 = str[start].isdigit()
        condition2 = str[start]=='-' and str[start+1].isdigit()
        condition3 = str[start]=='+' and str[start+1].isdigit()
        if condition1 or condition2 or condition3:

            ans = str[start]
            for j in range(start+1, len(str)):
                if str[j] == ' ':
                    break
                elif str[j].isdigit():
                    ans += str[j]
                else:
                    break
            try:
                int(ans)
            except:
                ans = float(ans)
            else:
                ans = int(ans)

            # number bounds
            if ans < -2**31:
                return -2**31
            elif ans > (2**31)-1:
                return (2**31)-1
            else:
                return ans

        else:
            return 0
