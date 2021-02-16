import tkinter as tk
from tkinter import ttk

class App(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.mainframe = ttk.Frame(root)
        self.mainframe.rowconfigure(2, weight=1) 
        self.mainframe.columnconfigure(0, weight=1) 
        self.mainframe.columnconfigure(1, weight=2) 
        self.mainframe.columnconfigure(2, weight=1)
        self.mainframe.grid(column=0, row=0, sticky="NEWS")
        parent.rowconfigure(0, weight=1) 
        parent.columnconfigure(0, weight=1)
        

        self.feet = tk.StringVar()
        self.meters = tk.StringVar()
        self.feet_entry = ttk.Entry(self.mainframe, width=7, textvariable=self.feet) 
        self.feet_entry.grid(column=1, row=0, sticky="WE")
        ttk.Label(self.mainframe, text="feet").grid(column=2, row=0, sticky="SW")
        ttk.Label(self.mainframe, text="is equivalent to").grid(column=0, row=1, sticky="NE")
        ttk.Label(self.mainframe, textvariable=self.meters).grid(column=1, row=1, sticky="NE")
        ttk.Label(self.mainframe, text="meters").grid(column=2, row=1, sticky="NW")
        ttk.Button(self.mainframe, text="Calculate", command=self.calculate).grid(column=2, row=2, sticky="SE")
        self.feet_entry.focus() 
        self.feet_entry.bind("<Return>", self.calculate)

    def calculate(self, *args):
        try:
            value = float(self.feet.get())
            self.meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0) 
        except ValueError:
            pass


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Feet to Meters")
    app = App(root)
    root.mainloop()