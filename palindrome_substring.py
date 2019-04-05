def longestPalindrome(self, s: str) -> str:
        longest = [0, 1]
        for i in range(1, len(s)):
            odd = self.get_pal(i-1, i+1, s)
            even = self.get_pal(i-1, i, s)
            cur_longest = max(odd, even, key=lambda x: x[1] - x[0])
            longest = max(cur_longest, longest, key=lambda x: x[1] - x[0])
        return s[longest[0]: longest[1]]

    def get_pal(self, left, right, s):
        while left <=0 and right<len(s):
            if s[left]!=s[right]:
                break
            left -=1
            right +=1
        return [left+1, right]
