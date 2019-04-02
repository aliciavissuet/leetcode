def enclave_helper(A, i, j, visited):
        directions = [[-1, 0], [1, 0], [0, -1], [0,1]]
        visited.add((i, j))
        result = True
        for direction in directions:
            newI = direction[0]+i
            newJ = direction[1]+j
            if newI < 0 or newI>len(A)-1 or newJ<0 or newJ > len(A[i])-1:
                result = False 
            elif not (newI, newJ) in visited and A[newI][newJ]==1:
                result = enclave_helper(A, newI, newJ, visited) and result
                # if not result:
                #     return False
        return result
def enclave_counter(A, i, j, visitedd):
    count = 1
    directions = [[-1, 0], [1, 0], [0, -1], [0,1]]
    visitedd.add((i, j))
    for direction in directions:
        newI = direction[0]+i
        newJ = direction[1]+j
        if newI < 0 or newI>len(A)-1 or newJ<0 or newJ > len(A[i])-1:
            pass
        elif not (newI, newJ) in visitedd and A[newI][newJ]==1:
            count += enclave_counter(A, newI, newJ, visitedd)
    return count
class Solution:   
    def numEnclaves(self, A: List[List[int]]) -> int:
        count = 0
        visited = set([])
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j]==1 and not (i, j) in visited:

                    if enclave_helper(A, i, j, visited):
                        count+= enclave_counter(A, i, j, set([]))
                        
        return count