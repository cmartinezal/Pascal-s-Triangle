from typing import List

class PascalTriangle:

    def generate_row(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        prev_row = self.generate_row(rowIndex - 1)

        return [1] + [prev_row[i] + prev_row[i + 1] for i in range(0, len(prev_row) -  1) if rowIndex > 1] + [1]

    def generate_pascal_triangle(self, num_rows: int) -> List[List[int]]:
        pascal_triangle = []
        pascal_triangle += [self.generate_row(i) for i in range(num_rows)]
        
        return pascal_triangle

# Tests
pascal_triangle = PascalTriangle()
for num_rows in range(12):
    print(f'Input: num_rows = {num_rows}')
    print(f'Output: {pascal_triangle.generate_pascal_triangle(num_rows)}')