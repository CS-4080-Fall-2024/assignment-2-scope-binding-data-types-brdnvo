""" Brandon Vo
    CS 4080
    Question 3: Sudoku Solver
"""
class Sudoku:
    def solveSudoku(self, board):
        self.board = board
        board_size = 9 
        
        def empty_space(row, column, num):
            for i in range(board_size):
                # Scan board for the current Sudoku numbers. If duplicate is found, return False (find another number to input)
                if board[i][column] == num: # Check rows
                    return False
                if board[row][i] == num: # Check columns
                    return False          
                start_row = row - row % 3
                start_column = column - column % 3
                for i in range(3):
                    for j in range(3):
                        if board[i + start_row][j + start_column] == num:
                            return False
                
            # Else: return True
            return True

        def solve():
            # Iterate through each value of 2-D array sudoku board
            for i in range(board_size):
                for j in range(board_size):
                    if board[i][j] == 0: # If space isn't occupied, continue with algorithm
                        for num in range(1, board_size + 1):
                            if empty_space(i, j, num):
                                board[i][j] = num # If conditions are met, add 'num' to board
                                if solve(): # Check if the algorithm can fill the next column
                                    return True
                                board[i][j] = 0 # Backtrack by resetting the space as empty and use the next index
                        return False # Return false if another number is found on the conditional (row, col, 3x3) 
            return True

        # Once all rows and columns are filled, print out solved sudoku board
        if solve(): 
            for row in board:
                print(row)

# Example board in LeetCode
sudoku_board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9]]
sudokuTest = Sudoku() 
sudokuTest.solveSudoku(sudoku_board) # Method call for example board

# Inspiration for this program was taken from this reference https://leetcode.com/problems/sudoku-solver/solutions/1947604/python-easiest-recursive-solution 