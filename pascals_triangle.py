from typing import List

class PascalTriangle:

    def generate_rows(self, num_rows: int) -> List[List[int]]:
        pascal_triangle = []
        
        if num_rows < 1:
            return pascal_triangle
    
        pascal_triangle.append([1])

        for row_num in range(2, num_rows + 1):
            prev_row = pascal_triangle[row_num - 2]
            new_row = [prev_row[0]]
            last_index = len(prev_row) - 1

            for i in range(last_index):
                new_row.append(prev_row[i] + prev_row[i + 1])

            new_row.append(prev_row[last_index])
            pascal_triangle.append(new_row)

        return pascal_triangle

    def print_rows(self, num_rows):
        print(f'Input: num_rows = {num_rows}')
        pascal_triangle = self.generate_rows(num_rows)
        print(f'Output: {pascal_triangle}')

# Tests
pascal_triangle = PascalTriangle()
for num_rows in range(12):
    pascal_triangle.print_rows(num_rows)