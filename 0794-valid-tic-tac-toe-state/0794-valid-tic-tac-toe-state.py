class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        countX = 0
        countO = 0
        Xwin = False
        Owin = False
      
        for row in range(len(board)):
            countD = f'{board[0][0]}{board[1][1]}{board[2][2]}'
            countDr = f'{board[0][~0]}{board[1][1]}{board[2][~2]}'
            countC = f'{board[0][row]}{board[1][row]}{board[2][row]}'
            countX+= board[row].count("X")
            if board[row].count("X")== 3 or countD.count("X") == 3 or countC.count("X") == 3 or countDr.count("X") == 3:
                Xwin = True
            countO+=board[row].count("O")
            if board[row].count("O") == 3 or countD.count("O") == 3 or countC.count("O") == 3 or countDr.count("O") == 3: 
                Owin = True
        print(countX,countO,Xwin,Owin)
        if countX == 0 and countO >0:
            return False
        elif countX-countO > 1 or countX - countO < 0:
            return False
        elif (countX >= 3 and Xwin) and countX-countO != 1:
            return False
        elif (countO >= 3 and Owin) and countX-countO != 0:
            return False 
        elif countX-countO == 0 and not Owin and countX+countO == 9 :
            return False
            
        else :
            return True 
            
            
       