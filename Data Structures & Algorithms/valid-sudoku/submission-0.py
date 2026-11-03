class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        boxes = {}
        for i in range(9):
            for j in range(9):
                rows.setdefault(i, set())
                cols.setdefault(j, set())
                boxes.setdefault((i//3, j//3), set())
                if board[i][j] == ".":
                    continue
                elif board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in boxes[(i//3, j//3)]:
                    return False
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[(i//3, j//3)].add(board[i][j])
        return True