from Table import sudoku
from tabulate import tabulate
puzzle_file = open("test/easy","r")
puzzleText = puzzle_file.read()
puzzle_file.close()
puzzle = []
puzzleTextRows = puzzleText.strip().split('\n')

for i in puzzleTextRows:
    puzzle.append(list(map(int,i)))

t = sudoku(puzzle)
result = t.solve()
print(tabulate(result['solution'],tablefmt="fancy_grid"))
print(result['timeTaken'])