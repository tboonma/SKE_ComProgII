import tkinter as tk
from datetime import datetime

class AnalogClock(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        parent.rowconfigure(0, weight=1)
        parent.columnconfigure(0, weight=1)
        self.config(bg="brown")
        self.grid(row=0, column=0, sticky="NEWS")
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0, bg="yellow")
        self.canvas.grid(row=0, column=0, padx=10, pady=10, sticky="NEWS")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.prepare_items()
        self.canvas.bind('<Configure>', lambda x: self.update_clock())
        

    def prepare_items(self):
        self.clock_face = self.canvas.create_oval(0, 0, 0, 0, width=3, outline="blue")
        self.center_pin = self.canvas.create_oval(0, 0, 0, 0, fill="green")
        self.second_hand = self.canvas.create_line(0, 0, 0, 0, fill="gray", width=1)
        self.minute_hand = self.canvas.create_line(0, 0, 0, 0, fill="black", width=4)
        self.hour_hand   = self.canvas.create_line(0, 0, 0, 0, fill="black", width=8)
        

    def center_coords(self):
        '''
        Return a tuple (x,y) representing the current center coordinates of the canvas
        '''
        return self.canvas.winfo_width()/2, self.canvas.winfo_height()/2
 
    def clock_radius(self):
        '''
        Return the desired clock's radius, which is set to be 90% of the canvas's shorter side
        '''
        cx,cy = self.center_coords()
        return min(cx,cy)*0.9

    def update_clock(self):
        cx,cy = self.center_coords()
        radius = self.clock_radius()
        # update the item self.clock_face so that it has the radius of self.clock_radius() 
        # and is centered at coordinates (cx,cy)
        cx1 = cx-radius
        cy1 = cy-radius
        cx2 = cx+radius
        cy2 = cy+radius
        self.canvas.coords(self.clock_face, cx1, cy1, cx2, cy2)
        # update the item self.center_pin so that it has the radius of 5 pixels and 
        # is centered at coordinates (cx,cy)
        self.canvas.coords(self.center_pin, cx-5, cy+5, cx+5, cy-5)
        now = datetime.now()
        sec_angle = now.second/60*360
        x1,y1 = self.polar_to_canvas(radius*0.9, sec_angle)
        self.canvas.coords(self.second_hand, cx, cy, x1, y1)
        min_angle = now.minute/60*360 + sec_angle/60
        x2,y2 = self.polar_to_canvas(radius*0.7, min_angle)
        self.canvas.coords(self.minute_hand, cx, cy, x2, y2)
        hour_angle = now.hour/12*360 + min_angle/12
        x3,y3 = self.polar_to_canvas(radius*0.5, hour_angle)
        self.canvas.coords(self.hour_hand, cx, cy, x3, y3)
        self.canvas.after(1000, self.update_clock)

    def polar_to_canvas(self, radius, theta):
        import math
        '''
        Take polar coordinates (radius,theta) and return a tuple (x,y)
        representing the Cartesian coordinates on the canvas, with respect to
        the canvas's center.
        '''
        cx,cy = self.center_coords()
        x = cx + radius*math.sin(math.radians(180)-math.radians(theta))
        y = cy + radius*math.cos(math.radians(180)-math.radians(theta))
        return x,y

    
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x300")
    root.title("Analog Clock")
    clock = AnalogClock(root)
    root.mainloop()