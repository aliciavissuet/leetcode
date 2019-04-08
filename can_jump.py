 def canJump(self, nums: List[int]) -> bool:
        memo = [None] * len(nums)
        result = self.jump_helper(nums, 0, memo)
        return(result[1])
    def jump_helper(self, nums, index, memo):
        
        if memo[index] is not None:
            return (memo, memo[index])
        if index== len(nums)-1:
            # memo[index] = True
            return (memo, True)
        if index > len(nums)-1:
            memo[index] = False
            return (memo, False)
        for i in range(1, nums[index]+1):
            if memo[index+i] is not None:
                continue
            else:
                result = self.jump_helper(nums, index+i, memo)
                memo = result[0]
                if result[1]:
                    memo[index]=True
                    return (memo, True)
