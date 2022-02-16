class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix_matrix = []
        for row in matrix:
            temp = []
            running_sum = 0
            for cell in row:
                running_sum += cell
                temp.append(running_sum)
            self.prefix_matrix.append(temp)
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        pass
        result = 0
        for curr_row in range(row1, row2+1):
            result += (self.prefix_matrix[curr_row][col2] - self.prefix_matrix[curr_row][col1] + self.matrix[curr_row][col1])
        return result
            

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)