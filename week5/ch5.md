# HW2(八個皇后問題)
## (簡介)
   八皇后問題是一個以西洋棋為背景的問題：如何能夠在8×8的西洋棋棋盤上放置八個皇后，使得任何一個皇后都無法直接吃掉其他的皇后？為了達到此目的，任兩個皇后都不能處於同一條橫行、縱行或斜線上。

* ![維吉尼亞密碼的表格]

* picture
 <img src="../img/abc.jpg" width="300" height="200"  align=center /> 
 
## [程式碼](https://github.com/Yongsin0/ai109b/blob/main/homework/bbb.py):

```
board = [-1] * 8


def printboard(result):
    for v in result:
        length = len(result)
        print('□ '*v + '■ ' + '□ '* (length-v-1))
    print('\n')

def is_valid(board, row, col):
    for r in range(row):
        if col == board[r] or abs(row - r) == abs(col - board[r]):
            return False
        continue
    return True

def eightQueen(board, row):
    if row >= len(board):
        printboard(board)
        return True

    for col in range(len(board)):
        if is_valid(board, row, col):
            board[row] = col
            if eightQueen(board, row+1):
                pass
                #return True
    return False

eightQueen(board, 0)

```
## [結果](https://github.com/Yongsin0/ai109b/blob/main/homework/Queen.out.txt):
