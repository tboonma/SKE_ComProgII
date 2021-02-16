import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Container Example")
style = ttk.Style()
style.configure(".", font=("Arial", 24))
top = ttk.Frame(name="top", borderwidth=5, padding=5, relief="ridge")
