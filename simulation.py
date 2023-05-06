import tkinter as tk


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('1000x1000')

        self.play_button = tk.Button(self.root, text="Play", command=self.play)
        self.play_button.pack()

        self.slider = tk.Scale(self.root, from_=0, to=4054, orient='horizontal', command=self.update)
        self.slider.pack()

        self.canvas = tk.Canvas(self.root, width=1000, height=1000, bg='blue')
        self.canvas.pack()

        self.time = 0
        self.update()

        self.root.mainloop()

    def from_rgb(self, rgb):
        r, g, b = rgb
        return f"#{r:02x}{g:02x}{b:02x}"

    def play(self):
        for t in range(4055):
            self.slider.set(t)
            self.root.update()

    def update(self, val=None):
        if val:
            self.time = int(val)
        blue = int((1 - self.time / 4054) * 150)
        color = self.from_rgb((0, 0, 255 - blue))
        self.canvas.configure(bg=color)


app = App()
