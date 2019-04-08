def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        curr_longest = [0, 1]
        start_idx = 0
        char_dict = {}
        for i, char in enumerate(s):
            if char in char_dict:
                start_idx = max(char_dict[char]+1, start_idx)
            if i+1 - start_idx > curr_longest[1] - curr_longest[0]:
                curr_longest = [start_idx, i+1]
            char_dict[char] = i
        return max(curr_longest[1]-curr_longest[0], len(s)-1 - start_idx)
