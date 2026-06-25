class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        sq= [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                new_num=board[i][j]
                if new_num ==".":
                    continue
                elif new_num in row[i] or new_num in col[j] or new_num in sq[3*(i//3)+(j//3)]:
                    print(row)
                    return False
                else:
                    row[i].add(new_num)
                    col[j].add(new_num)
                    sq[3*(i//3)+(j//3)].add(new_num)
        return True
        