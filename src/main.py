
import tkinter as tk
from tkinter import ttk
from components import *

root = tk.Tk()
root.title("Main Window")

root.geometry("700x300")
root.configure(bg="#98e3d5")

title_label = ttk.Label(root, text="BEZIER CURVE", font=("Arial", 20, "bold"))
title_label.pack(pady=20) 

brute = ttk.Button(root, text="Brute Force", command=lambda: brute_force(root))
brute.pack(fill=tk.X, padx=20, pady=5) 
dnc = ttk.Button(root, text="Divide and Conquer (3 Points)", command=lambda: normal_dnc(root))
dnc.pack(fill=tk.X, padx=20, pady=5) 

n_dnc = ttk.Button(root, text="Divide and Conquer (N Points)", command=lambda: n_point_dnc(root))
n_dnc.pack(fill=tk.X, padx=20, pady=5)  

root.mainloop()
