def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        biggest_ss = 1

        # iterate over all indexes except last
        for i in range(len(s)):
            sub = ''

            # iterate over characters after current index
            for char in s[i:]:

                if char in sub:
                    break
                else:
                    sub += char
                    if len(sub) > biggest_ss:
                        biggest_ss = len(sub)

        return biggest_ss if s!='' else 0
