class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashmap = {}
        hashmapcol = {}
        hashmapbox = {}
        for i in range (len(board)):
            for j in range (len(board)):
                if board[i][j] != ".":
                    number =board[i][j]
                    box_row = i // 3
                    box_col = j // 3
                    if (i,number) in hashmap:
                        return False
                    if (j,number) in hashmapcol:
                        return False
                    if (box_row,box_col,number) in hashmapbox:
                        return False
                    else:
                        hashmap[i,number] = True
                        hashmapcol[j,number] = True
                        hashmapbox[box_row,box_col,number] = True
        return True
            