from typing import List

class PascalTriangle:
    def generate_rows(self, numRows: int) -> List[List[int]]:
        if numRows < 1:
            return  []
    
        pascal_triangle = [[1]]

        if numRows == 1:
            return pascal_triangle[numRows - 1]

        current_row = 2
        while current_row <= numRows:
            prev_row = pascal_triangle[current_row - 2]
            row = [prev_row[0]]
            last_index = len(prev_row) - 1
            for i in range(last_index):
                row.append(prev_row[i] + prev_row[i + 1])
            row.append(prev_row[last_index])
            pascal_triangle.append(row)
            current_row += 1

        return pascal_triangle

    def print_PascalTriangle(self, numRows):
        print(f'Input: numRows = {numRows}')
        pascal_triangle = self.generate_rows(numRows)
        print(f'Output: {pascal_triangle}')

# Tests
PascalTriangle = PascalTriangle()
for numRows in range(10):
    PascalTriangle.print_PascalTriangle(numRows)