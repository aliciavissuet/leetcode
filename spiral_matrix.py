def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        result = []
        while len(matrix) > 0:

            #get first row
            first_row = matrix.pop(0)
            result += first_row

            #get last col
            for row in range(len(matrix)):
                try:
                    el = matrix[row].pop(-1)
                    result.append(el)
                except:
                    continue

            #get bottom row in reverse
            if len(matrix) > 0:
                last_row = matrix.pop()[::-1]
                result += last_row
            #get first col from bottom to top

            for row in range(len(matrix)):
                try:
                    el = matrix[len(matrix)-row-1].pop(0)
                    result.append(el)
                except:
                    continue

        return result
