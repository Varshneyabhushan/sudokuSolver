from Table import sudoku
puzzle = [[0,2,4,0],[1,0,0,3],[4,0,0,2],[0,1,3,0]]
table = sudoku(puzzle)
result = table.solve()
print(result)