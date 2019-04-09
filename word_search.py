def exist(self, board: List[List[str]], word: str) -> bool:

        for i in range(len(board)):
            for j in range(len(board[i])):
                been_here = defaultdict(lambda: None)
                if board[i][j] == word[0]:
                    new_been_here = copy(been_here)
                    new_been_here[(i, j)] = True
                    result = self.exist_helper(
                        board, word[1:], i, j, new_been_here)
                    if result:
                        return result
        return False

    def exist_helper(self, board, word, i, j, been_here):
        if len(word)==0:
            return True
        pot_pos = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        for pos in pot_pos:
            newI = pos[0]+i
            newJ = pos[1]+j
            
            if newI >= 0 and newI <len(board) and newJ >= 0 and newJ< len(board[newI]) and board[newI][newJ] and board[newI][newJ]==word[0] and  not been_here[(newI, newJ)]:
                new_been_here = copy(been_here)
                new_been_here[(newI, newJ)] = True
                result = self.exist_helper(board, word[1:], newI, newJ, new_been_here)
                if result:
                    return True
        return False
