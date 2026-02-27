class Solution:

    def is_safe(self, board, row, col, N):

        # Check left side of row
        for i in range(col):
            if board[row][i] == 1:
                return False

        # Check upper-left diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # Check lower-left diagonal
        i, j = row, col
        while i < N and j >= 0:
            if board[i][j] == 1:
                return False
            i += 1
            j -= 1

        return True

    def solve_N_Queens(self, board, col, N):

        if col >= N:
            return True

        for row in range(N):

            if self.is_safe(board, row, col, N):

                board[row][col] = 1

                if self.solve_N_Queens(board, col + 1, N):
                    return True

                # Backtracking
                board[row][col] = 0

        return False


# Driver Code
N = 4
board = [[0] * N for _ in range(N)]

obj = Solution()

if obj.solve_N_Queens(board, 0, N):
    for row in board:
        print(row)
else:
    print("No Solution Exists")