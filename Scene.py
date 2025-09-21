import tkinter as tk
from tkinter import ttk
from PanZoomCanvas import PanZoomCanvas

class Scene(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.canvas = PanZoomCanvas(self)
        self.canvas.grid(row=0, column=0, sticky='nsew')
        self.fg_opacity = 1.0

        #Divide the frame
        self.right_frame = ttk.Frame(self, width=150, style="UiPanel.TFrame")
        self.right_frame.grid(row=0, column=1, sticky='ns')

        # Create the bottom frame (styled)
        self.bottom_frame = ttk.Frame(self, height=50, style="UiPanel.TFrame")
        self.bottom_frame.grid(row=1, column=0, columnspan=2, sticky='ew')

        # Configure grid weights so the canvas expands but has a minimum size
        self.grid_rowconfigure(0, weight=1, )  # Min height 200px
        self.grid_rowconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=1)  # Min width 300px
        self.grid_columnconfigure(1, weight=0)

        
    def show(self):
        self.canvas.redraw()

    def set_canvas_bg(self, canvas_bkg):
        self.canvas.configure(bg=canvas_bkg)

    def fit_to_screen(self):
        self.canvas.reset(self.master.layer_renderer.current_fg.width, self.master.layer_renderer.current_fg.height)
