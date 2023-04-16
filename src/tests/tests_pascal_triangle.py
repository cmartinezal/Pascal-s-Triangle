import os
import sys
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from pascal_triangle.pascals_triangle import PascalTriangle

def run_tests():
    pascal_triangle = PascalTriangle()
    for num_rows in range(12):
        print(f'Input: num_rows = {num_rows}')
        print(f'Output: {pascal_triangle.generate_pascal_triangle(num_rows)}')