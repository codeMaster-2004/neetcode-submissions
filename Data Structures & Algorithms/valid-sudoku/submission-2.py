class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box_dict = defaultdict(set)
        #row check
        for i in range(len(board)):
            row_set = set()
            col_set = set()
            box_set = set()
            num_of_col_nums = 0
            num_of_row_nums = 0
            num_of_box_nums = 0
            for j in range(len(board)):
                if board[i][j] != '.':
                    num_of_row_nums += 1
                    row_set.add(board[i][j])
                if board[j][i] != '.':
                    num_of_col_nums += 1
                    col_set.add(board[j][i])
                if board[i][j] in box_dict[(i//3, j//3)]:
                    return False
                if (board[i][j] not in box_dict[(i//3, j//3)]) and board[i][j] != '.':
                    box_dict[(i//3, j//3)].add(board[i][j])
            if (len(row_set) != num_of_row_nums) or (len(col_set) != num_of_col_nums):
                return False
        return True 
        #box check