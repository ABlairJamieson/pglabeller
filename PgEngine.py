import tkinter as tk
from tkinter import ttk                                                                                                                                                               
from tkinter import *
from tkinter import messagebox
import webbrowser
from LayerRenderer import LayerRenderer
from FilterProcessor import FilterProcessor
from BlobManager import BlobManager
from SceneEdit import SceneEdit
from SceneLabel import SceneLabel
from tkinter import filedialog 
import os


class PgEngine(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PgLabeller")
        self.geometry("800x600")
        self.minsize(800,800)
        #Create menu bar
        self.__create_menu_bar()

        #Data shared by all the scenes
        self.layer_renderer = LayerRenderer()
        self.filter_processor = FilterProcessor()
        self.filter_processor.bind_image(self.layer_renderer.current_fg)
        self.blob_manager = BlobManager()


        self.layer_renderer.load_foreground("./images/BlobTest.jpg")
        self.filter_processor.bind_image(self.layer_renderer.current_fg)


        
        #Now create scenes
        self.scene_map = {}
        self.add_scene("scene_edit", SceneEdit(self))
        self.add_scene("scene_label", SceneLabel(self))
        self.change_scene("scene_edit")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.style = ttk.Style()
        
        
        
        self.dark_palette = {
            "canvas_bg": "#555555",
            "bg": "#222222",
            "fg": "#ffffff",
            "button_bg": "#222222",
            "button_fg": "#ffffff",
            "button_active": "#333333",
            "check_bg": "#111111",
            "check_fg": "#ffffff",
            "check_active": "#222222",
            "entry_bg": "#444444",
            "entry_fg": "#ffffff",
            "scale_bg": "#222222",
            "trough": "#444444",
            "middle_bg": "#555555",   # gray in dark mode
            "menu_bg": "#333333",
            "menu_fg": "#ffffff",
            "error_bg": "#ff9999",
            "error_fg": "#ffffff"
        }
        
        self.light_palette = {
            "canvas_bg": "#ffffff",
            "bg": "#f0f0f0",
            "fg": "#000000",
            "button_bg": "#e0e0e0",
            "button_fg": "#000000",
            "button_active": "#eeeeee",
            "check_bg": "#f0f0f0",
            "check_fg": "#000000",
            "check_active": "#f0f0f0",
            "entry_bg": "#ffffff",
            "entry_fg": "#000000",
            "scale_bg": "#f0f0f0",
            "trough": "#cccccc",
            "middle_bg": "#ffffff",   # white in light mode
            "menu_bg": "#e0e0e0",
            "menu_fg": "#000000",
            "error_bg" : "#ff9999",
            "error_fg": "#ffffff"
        }
        self.style.theme_use("clam")
        self.change_palette(self.dark_palette)

        
    def __create_menu_bar(self):
        self.__menubar = tk.Menu(self, bg="black", fg="white", activebackground="gray", activeforeground="White")
        self.__filemenu = tk.Menu(self.__menubar, tearoff=0, bg="black", fg="white", activebackground="gray")
        self.__filemenu.add_command(label="Open", command=lambda:self.open(self.__filemenu))
        self.__filemenu.add_command(label="Save", command=self.save)
        self.__filemenu.add_command(label="Load Background", command=self.load_background)
        self.__filemenu.add_separator()
        self.__filemenu.add_command(label="Exit", command=self.quit)
        #filemenu.entryconfig(2, state="disabled")
        self.__menubar.add_cascade(label="File", menu=self.__filemenu)

         # Variable to track which mode is selected
        self.current_mode = tk.StringVar(value="scene_edit")

        self.__modemenu = tk.Menu(self.__menubar, tearoff=0, bg="black", fg="white", selectcolor="white", activebackground="gray")
        self.__modemenu.add_radiobutton(label="Edit Mode", 
                                 variable=self.current_mode, 
                                 value="scene_edit", 
                                 command=lambda: self.change_scene("scene_edit"))
        self.__modemenu.add_radiobutton(label="Label Mode", 
                                 variable=self.current_mode, 
                                 value="scene_label", 
                                 command=lambda: self.change_scene("scene_label"))
        self.__menubar.add_cascade(label="Mode", menu=self.__modemenu)
        
        #Preference
        # Variable to track which mode is selected
        self.preference = tk.StringVar(value="dark_mode")

        self.__preferencemenu = tk.Menu(self.__menubar, tearoff=0, bg="black", fg="white", selectcolor="white", activebackground="gray")
        self.__preferencemenu.add_radiobutton(label="Dark Mode", 
                                 variable=self.preference, 
                                 value="dark_mode", 
                                 command=lambda: self.change_palette(self.dark_palette))
        self.__preferencemenu.add_radiobutton(label="Light Mode", 
                                 variable=self.preference, 
                                 value="light_mode", 
                                 command=lambda: self.change_palette(self.light_palette))
        self.__menubar.add_cascade(label="Preference", menu=self.__preferencemenu)
        
        
        self.__helpmenu = tk.Menu(self.__menubar, tearoff=0, bg="black", fg="white", activebackground="gray")
        self.__helpmenu.add_command(label="Manual", command=lambda:webbrowser.open("https://github.com/ABlairJamieson/pglabeller"))
        self.__helpmenu.add_command(label="About", command=self.show_about)
        self.__menubar.add_cascade(label="Help", menu=self.__helpmenu)
        
        

        
        self.config(menu=self.__menubar)

    def change_palette(self, palette):
        for scene in self.scene_map.values():
            scene.set_canvas_bg(palette["canvas_bg"])
        
        self.style.configure("UiPanel.TFrame", background=palette["bg"])
        #self.style.configure("Bottombar.TFrame", background=palette["bg"])
            
        self.style.configure("Pg.TLabel", background=palette["bg"], foreground=palette["fg"])
        self.style.configure("Bold.TLabel", background=palette["bg"], foreground=palette["fg"])
        self.style.configure("Pg.TButton", background=palette["button_bg"], foreground=palette["button_fg"])
        self.style.map("Pg.TButton", background=[("active", palette["button_active"])])
        self.style.configure("Pg.TCheckbutton", background=palette["bg"], foreground=palette["fg"])
        self.style.map("Pg.TCheckbutton", background=[("active", palette["check_active"])])
        self.style.configure("Pg.TEntry", fieldbackground=palette["entry_bg"], foreground=palette["entry_fg"])
        self.style.configure("Pg.TSpinbox", fieldbackground=palette["entry_bg"], foreground=palette["entry_fg"])
        self.style.configure("TScale", background=palette["bg"], troughcolor=palette["trough"])
        self.style.configure("Pg.TCombobox", fieldbackground=palette["entry_bg"], background=palette["entry_bg"], foreground=palette["entry_fg"])

        self.style.configure("Error.TSpinbox", fieldbackground=palette["error_bg"], foreground=palette["error_fg"])
        self.style.configure("Error.TEntry", fieldbackground=palette["error_bg"], foreground=palette["error_fg"])
        
        #entry.configure(background=p["entry_bg"], foreground=p["entry_fg"])
    
        self.__menubar.configure(bg=palette["bg"], fg=palette["fg"])
        
        for menu in (self.__filemenu, self.__modemenu, self.__preferencemenu, self.__helpmenu):
            menu.configure(bg=palette["menu_bg"], fg=palette["menu_fg"], activebackground=palette["trough"], activeforeground=palette["fg"], selectcolor=palette["menu_fg"])

            
                
    def add_scene(self, name, scene):
        self.scene_map[name] = scene
        self.scene_map[name].grid(row=0, column=0, sticky="nsew")
        
    #Only opens image for now. Will later open .pg file 
    def open(self, filemenu):
        filepath = filedialog.askopenfilename(
            filetypes=[("Image files", ".jpg .jpeg .png .bmp .gif"), ("All files", "*.*")]
        )
        if filepath:
            filename,_ = os.path.splitext(os.path.basename(filepath))
            self.title(filename +" ["+filepath+"]"+" -PgLabeller")

            self.layer_renderer.load_foreground(filepath)
            self.filter_processor.bind_image(self.layer_renderer.current_fg)

            self.blob_manager.reset()
            #Fit the image to the screen
            for scene in self.scene_map.values():
                scene.fit_to_screen()

            self.scene_map[self.current_scene].show()
            

    def load_background(self):
        filepath = filedialog.askopenfilename(
            filetypes=[("Image files", ".jpg .jpeg .png .bmp .gif"), ("All files", "*.*")]
        )
        if filepath:
            self.layer_renderer.load_background(filepath)
            self.scene_map[self.current_scene].show()

            
    #Only saves image for now. Will later save .pg file 
    def save(self):
        if not self.layer_renderer.is_fg_loaded:
            return

        
        if self.image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG Files", "*.png"),
                                                                ("JPEG Files", "*.jpg"),
                                                                ("All Files", "*.*")])
            if file_path:
                self.image.save(file_path)

        
    def show_about(self):
        messagebox.showinfo(
            "About PgLabeller",
            "PgLabeller v1.0\n\nThis software lets you detect features, edit and label them easily.\n"
            "Created by Tapendra BC © 2025"
        )
        
    def change_scene(self, name):
        if name in self.scene_map:
            self.current_scene = name
            self.bind("<Configure>", self.scene_map[name].canvas.on_resize) 
            self.scene_map[name].tkraise()
            self.scene_map[name].show()
            
        else:
            print("Scene, " + name + ", doesn't exist.")
            
