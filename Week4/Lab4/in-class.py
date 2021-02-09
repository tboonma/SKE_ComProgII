import tkinter as tk
import tkinter.ttk as ttk
import datetime

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Digital Clock")
        self.geometry("400x100")
        self.str_date = "*** Current Date ***"
        self.str_time = "*** Current Time ***"
        self.date = tk.Label(self, text="date", font=("Arial",24))
        self.date.pack()
        self.time = tk.Label(self, text="time", font=("Arial",24))
        self.time.pack()
        self.quitBtn = tk.Button(self, text="Quit", font=("Arial",24), width=8)
        self.quitBtn.config(command=self.destroy)
        self.quitBtn.pack()
        self.update_time()

    def update_time(self):
        time = datetime.datetime.now()
        self.str_date = time.strftime("%d %B %Y")
        self.str_time = time.strftime("%H:%M:%S")
        self.date.config(text=self.str_date)
        self.time.config(text=self.str_time)
        self.date.after(200, self.update_time)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
