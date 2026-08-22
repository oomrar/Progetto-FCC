def dfs_n_queens(n):

    if n < 1:
        return []
    
    solutions = []
    stack = [[]]
    
    while stack:
        board = stack.pop()
        row = len(board)
        
        if row == n:
            solutions.append(board)
            continue
        
        for col in range(n - 1, -1, -1):
            if is_safe(board, row, col):
                stack.append(board + [col])
                
    return solutions

def is_safe(board, row, col):
    for r, c in enumerate(board):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True
