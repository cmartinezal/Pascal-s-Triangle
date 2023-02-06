from typing import List

class PascalTriangle:

    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        prev_row = self.getRow(rowIndex - 1)

        return [1] + [prev_row[i] + prev_row[i + 1] for i in range(0, len(prev_row) -  1) if rowIndex > 1] + [1]

    def generate_rows(self, num_rows: int) -> List[List[int]]:
        pascal_triangle = []

        if num_rows > 0:
            pascal_triangle += [self.getRow(i) for i in range(num_rows)]
        
        return pascal_triangle

    def print_rows(self, num_rows):
        print(f'Input: num_rows = {num_rows}')
        pascal_triangle = self.generate_rows(num_rows)
        print(f'Output: {pascal_triangle}')

# Tests
pascal_triangle = PascalTriangle()
for num_rows in range(12):
    pascal_triangle.print_rows(num_rows)