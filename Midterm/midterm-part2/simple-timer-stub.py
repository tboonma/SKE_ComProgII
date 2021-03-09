import tkinter as tk
from tkinter import ttk

class SimpleTimer(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.str_remaining = tk.StringVar()
        self.str_remaining.set("0 second(s)")
        self.create_widgets()

    def create_widgets(self):
        self.style = ttk.Style()
        self.style.configure("Remain.TLabel", font=("Arial", 24))
        self.mainframe = ttk.Frame(root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky="news")
        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(0, weight=1)

        self.btn_minus = ttk.Button(self.mainframe, text="-")
        self.btn_plus = ttk.Button(self.mainframe, text="+")
        self.btn_start = ttk.Button(self.mainframe, text="Start")
        self.lbl_remain = ttk.Label(self.mainframe, style="Remain.TLabel",
                textvariable=self.str_remaining, padding="10 10 10 10")

        self.lbl_remain.grid(row=0, column=0, columnspan=3)
        self.btn_minus.grid(row=1, column=0)
        self.btn_start.grid(row=1, column=1)
        self.btn_plus.grid(row=1, column=2)
    
    


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Simple Timer")
    app = SimpleTimer(root)
    root.mainloop()

