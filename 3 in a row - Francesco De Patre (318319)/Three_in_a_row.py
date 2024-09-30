#Author Francesco De Patre 318319
from boardgame import BoardGame, console_play
from boardgameguin import gui_play
from random import randint

class Three(BoardGame):

    def __init__(self, w: int, h: int):
        self._w, self._h = w, h
        self._counter1 = 0
        self._counter2 = 0
        self._finish = False
        self._board = [[0 for x in range(self._w)] for y in range(self._h)]
        self._fisso = [(0,5),(1,1),(1,5),(1,4),(2,2),(3,3),(4,4),(3,5),(5,2)] #values that can't be changed
        self._board[5][0] = 2
        self._board[1][1] = 2
        self._board[5][1] = 2
        self._board[2][2] = 1
        self._board[3][3] = 1
        self._board[5][3] = 1
        self._board[4][4] = 2
        self._board[5][3] = 1
        self._board[2][5] = 1
        self._board[4][1] = 2
        
        
    def cols(self) -> int:
        return self._w

    def rows(self) -> int:
        return self._h

    def message(self) -> str:
        return "Well Done!"

    def value_at(self, x: int, y: int):
        if (self._board[y][x] == 0):
            return "G"
        elif (self._board[y][x] == 1):
            return "B"
        elif (self._board[y][x] == 2):
            return "N"
        
            
    def play_at(self, x: int, y: int):
        if(x,y) in self._fisso:
            pass
        else:
            if (self._board[y][x] == 0):
                self._board[y][x] = 1

            elif (self._board[y][x] == 1):
                self._board[y][x] = 2

            elif (self._board[y][x] == 2):
                self._board[y][x] = 0

        
    def flag_at(self, x: int, y: int):
        pass
    
    def finished(self) -> bool:
        kcol = 0
        krow = 0
        count1 = 0
        count2 = 0
        '''
        check cols
        '''
        for a in range (self._h):
            for b in range (self._w):
                if b <= (self._w - 3):
                    if (self._board[a][b] == 1) and (self._board[a][b+1] == 1) and (self._board[a][b+2] != 1):
                        count1 += 1
                    elif (self._board[a][b] == 1) and (self._board[a][b+1] != 1):
                        count1 += 1
                    elif (self._board[a][b] == 2) and (self._board[a][b+1] == 2) and (self._board[a][b+2] != 2):
                        count2 +=1
                    elif (self._board[a][b] == 2) and (self._board[a][b+1] != 2):
                        count2 += 1
                if b > (self._w - 3):
                    if self._board[a][b] == 1:
                        count1 += 1
                    elif self._board[a][b] == 2:
                        count2 += 1
            if (count1 == count2):
                    kcol +=1
            count1, count2 = 0,0
        '''
        check rows
        '''
        for a in range (self._h):
            for b in range (self._w):
                if b <= (self._w - 3):
                    if (self._board[a][b] == 1) and (self._board[a][b+1] == 1) and (self._board[a][b+2] != 1):
                        count1 += 1
                    elif (self._board[a][b] == 1) and (self._board[a][b+1] != 1):
                        count1 += 1
                    elif (self._board[a][b] == 2) and (self._board[a][b+1] == 2) and (self._board[a][b+2] != 2):
                        count2 +=2
                    elif (self._board[a][b] == 2) and (self._board[a][b+1] != 2):
                        count2 += 1
                if b > (self._w - 3):
                    if self._board[a][b] == 1:
                        count1 += 1
                    elif self._board[a][b] == 2:
                        count2 += 1
            if (count1 == count2):
                    krow +=1
            count1, count2 = 0,0
        if (krow == self._w) and (kcol == self._h):
            return True
        
def main():
    dim = str(input("inserisci dimensione (6x6,8x8,10x10): ")) #choose dimension
    if (dim == "6x6"):
        game = Three(6, 6)
    elif (dim == "8x8"):
        game = Three(8, 8)
    elif (dim == "10x10"):
        game = Three(10, 10)
    gui_play(game)
    
main()
