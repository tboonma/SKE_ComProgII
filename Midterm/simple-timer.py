import tkinter as tk
from tkinter import ttk

class SimpleTimer(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.str_remaining = tk.StringVar()
        self.time_remaining = 0
        self.str_remaining.set(f"{self.time_remaining} second(s)")
        self.timer_start = False
        self.create_widgets()

    def create_widgets(self):
        self.style = ttk.Style()
        self.style.configure("Remain.TLabel", font=("Arial", 24))
        self.mainframe = ttk.Frame(root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky="news")
        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(0, weight=1)

        self.btn_minus = ttk.Button(self.mainframe, text="-", command=self.decrease_time)
        self.btn_plus = ttk.Button(self.mainframe, text="+", command=self.increase_time)
        self.btn_start = ttk.Button(self.mainframe, text="Start", command=self.start_stop_timer)
        self.lbl_remain = ttk.Label(self.mainframe, style="Remain.TLabel",
                textvariable=self.str_remaining, padding="10 10 10 10")

        self.lbl_remain.grid(row=0, column=0, columnspan=3)
        self.btn_minus.grid(row=1, column=0)
        self.btn_start.grid(row=1, column=1)
        self.btn_plus.grid(row=1, column=2)

    def increase_time(self):
        self.time_remaining += 1
        self.str_remaining.set(f"{self.time_remaining} second(s)")
    
    def decrease_time(self):
        if self.time_remaining > 0:
            self.time_remaining += -1
        self.str_remaining.set(f"{self.time_remaining} second(s)")  

    def start_stop_timer(self):
        if not self.timer_start:
            self.start_timer()
        else:
            self.stop_timer()

    def start_timer(self):
        self.timer_start = True
        self.btn_minus.config(state="disabled")
        self.btn_plus.config(state="disabled")
        self.btn_start.config(text="Stop")
        if self.time_remaining > 0:
            self.time_remaining -= 1
        self.str_remaining.set(f"{self.time_remaining} second(s)")
        self.timer = self.after(1000, self.start_timer)
        if self.time_remaining == 0:
            self.str_remaining.set("Time's up!")
            self.stop_timer()
        
    
    def stop_timer(self):
        self.timer_start = False
        self.btn_minus.config(state="enabled")
        self.btn_plus.config(state="enabled")
        self.btn_start.config(text="Start")
        self.after_cancel(self.timer)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Simple Timer")
    app = SimpleTimer(root)
    root.mainloop()

