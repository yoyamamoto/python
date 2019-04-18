# -*- coding:utf-8 -*-
import tkinter

################################################
#
# GUIウィンドウを生成し、パーティクルを動かすテスト
# どこかでメモリリークしてるから重くなる
#
################################################

class Stage(tkinter.Tk):
    def __init__(self, title = 'ベースタイトル', size = (375, 480)):
        super().__init__()
        print('init')

        self.title(title)
        self.geometry("%dx%d"%(size))
        
        # Build Canvas & set position.
        self.canvas = tkinter.Canvas(self, width = size[0], height = size[1], bg = '#fff')
        self.canvas.place(x = 0, y = 0)

        # define property of the particle
        self.x = 30
        self.y = 10
        self.vx = 7
        self.vy = 5
        
        self.dia = 20

        # Animation
        self.on_enter_frame()

    # Animate enter frame
    def on_enter_frame(self):
        # clear canvas
        self.clear_canvas()

        # Get stage size
        w = self.winfo_width()
        h = self.winfo_height()

        # particle oparation
        self.x += self.vx
        self.y += self.vy
        
        if self.x > w or self.x < 0:
            self.vx = - self.vx
        if self.y > h or self.y < 0:
            self.vy = - self.vy

        # Draw particle on Canvas
        id = self.canvas.create_oval(self.x - self.dia/2, self.y - self.dia/2,
                                self.x + self.dia/2, self.y + self.dia/2,
                                fill="#333")
        self.after(10, self.on_enter_frame)


    # Clear canvas
    def clear_canvas(self):
        w = self.winfo_width()
        h = self.winfo_height()
        self.canvas.create_rectangle(0, 0, w, h, fill='#fff')



def main():
    stage = Stage(title = "パーティクルのテスト")

    # Call Main loop
    stage.mainloop()

if __name__ == "__main__":
    main()