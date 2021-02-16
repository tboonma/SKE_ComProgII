import tkinter as tk
from tkinter import ttk
class App(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.mainframe = ttk.Frame(root)
        self.mainframe.pack()
        self.feet = tk.StringVar()
        self.meters = tk.StringVar()
        self.feet_entry = ttk.Entry(self.mainframe, width=7, textvariable=self.feet) 
        self.feet_entry.pack()
        ttk.Label(self.mainframe, text="feet").pack()
        ttk.Label(self.mainframe, text="is equivalent to").pack() 
        ttk.Label(self.mainframe, textvariable=self.meters).pack() 
        ttk.Label(self.mainframe, text="meters").pack()
        ttk.Button(self.mainframe, text="Calculate", command=self.calculate).pack()

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