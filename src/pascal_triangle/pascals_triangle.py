from typing import List

class PascalTriangle:

    def generate_row(self, row_index: int) -> List[int]:
        if row_index == 0:
            return [1]

        prev_row = self.generate_row(row_index - 1)

        return [1] + [prev_row[i] + prev_row[i + 1] for i in range(0, len(prev_row) -  1) if row_index > 1] + [1]

    def generate_pascal_triangle(self, num_rows: int) -> List[List[int]]:
        pascal_triangle = []
        pascal_triangle += [self.generate_row(i) for i in range(num_rows)]
        
        return pascal_triangle