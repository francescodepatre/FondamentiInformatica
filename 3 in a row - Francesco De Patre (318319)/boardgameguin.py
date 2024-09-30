#Author Francesco De Patre 318319
import g2d
from boardgame import BoardGame
from random import randint

W, H = 70, 70

class GUI:
    def __init__(self, g: BoardGame):
        self._game = g
        self.update_buttons()

    def tick(self):
        if g2d.key_pressed("LeftButton"):
            mouse = g2d.mouse_position()
            x, y = mouse[0] // W, mouse[1] // H
            
            self._game.play_at(x, y)
            self.update_buttons()
        if g2d.key_pressed("ArrowUp"):
            self._game.finished()
            

    def update_buttons(self):
        g2d.clear_canvas()
        cols, rows = self._game.cols(), self._game.rows()
        
        for y in range(0, rows):
            for x in range(0, cols):
                value = self._game.value_at(x, y)
                if (value == "G"):
                    g2d.set_color((68,68,68))
                elif (value == "B"):
                    g2d.set_color((255,255,255))
                elif (value == "N"):
                    g2d.set_color((0,0,0))
                g2d.fill_rect(((x*W),(y*H),W,H))
                
            
        
        for y in range(rows):
            g2d.draw_line((0, y * H), (cols * W, y * H))
            g2d.set_color((50, 50, 50))
            for x in range(cols):
                g2d.draw_line((x * W, 0), (x * W, rows * H))
                g2d.set_color((50, 50, 50))
        
        g2d.update_canvas()
        if self._game.finished():
            g2d.alert(self._game.message())
            g2d.close_canvas()

def gui_play(game: BoardGame):
    g2d.init_canvas((game.cols() * W, game.rows() * H))
    ui = BoardGameGui(game)
    g2d.main_loop(ui.tick)
