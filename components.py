import time
import tkinter as tk
from tkinter import ttk,simpledialog
from functions import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def input_box(parent, n):
    control_points = []
    iterations = 0
    dialog = tk.Toplevel(parent)
    dialog.title("Bezier Curve Inputs")

    # STYLING
    style = ttk.Style()
    style.configure('InputBox.TFrame', background='#f8c4cc')  
    style.configure('InputBox.TSpinbox', padding=5)  
    style.configure('InputBox.TButton', padding=5)  

    main_frame = ttk.Frame(dialog, style='InputBox.TFrame')
    main_frame.pack(padx=10, pady=10)

    # TITLE
    title_input = tk.Label(main_frame, text="INPUT BEZIER", font=("Arial", 24, "bold"))
    title_input.grid(row=0, column=0, columnspan=4, sticky=tk.E + tk.W, padx=5, pady=5)
    petunjuk = tk.Label(main_frame, text="Masukkan posisi titik kontrol dan jumlah iterasi", background='#F8C4CC', font=("Arial", 12))
    petunjuk.grid(row=1, column=0, columnspan=4, sticky=tk.E + tk.W, padx=5, pady=5)

    entry_widgets = []
    for i in range(0, n):
        temp = []
        # X
        label_x = ttk.Label(main_frame, text="X" + str(i+1) + ":")  
        label_x.grid(row=2+i, column=0, sticky=tk.E, padx=5, pady=5)
        entry_x = ttk.Entry(main_frame)
        entry_x.grid(row=2+i, column=1, padx=5, pady=5)
        temp.append(entry_x)
        # Y
        label_y = ttk.Label(main_frame, text="Y" + str(i+1) + ":") 
        label_y.grid(row=2+i, column=2, sticky=tk.E, padx=5, pady=5)
        entry_y = ttk.Entry(main_frame)
        entry_y.grid(row=2+i, column=3, padx=5, pady=5)
        temp.append(entry_y)
        entry_widgets.append((temp[0], temp[1]))

    # NUMBER OF ITERATIONS
    iteration_label = ttk.Label(main_frame, text="Jumlah Iterasi:")
    iteration_label.grid(row=n + 2, columnspan=2, sticky=tk.E + tk.W, padx=5, pady=5)
    iteration_input = ttk.Spinbox(main_frame, from_=1, to=1e10, increment=1)
    iteration_input.grid(row=n + 2, column=2, columnspan=2, sticky=tk.E + tk.W, padx=5, pady=5)

    # SUBMIT
    def submit():
        nonlocal control_points, iterations
        control_points = []
        for entry_x, entry_y in entry_widgets:
            x_value = entry_x.get()
            y_value = entry_y.get()
            control_points.append((int(x_value), int(y_value)))
        iterations = int(iteration_input.get())
        dialog.destroy()

    submit_button = ttk.Button(main_frame, text="Submit", command=submit, style='InputBox.TButton')
    submit_button.grid(row=n + 3, column=0, columnspan=4, sticky=tk.E + tk.W, padx=5, pady=5)

    dialog.wait_window()
    return control_points, iterations




    
def normal_dnc(root):
    control_points, iterations = input_box(root, 3)

    start_time = time.time()
    curve = bezier_dnc(control_points,iterations)
    end_time = time.time()
    runtime_ms = (end_time-start_time) * 1000

    pop_up_normal_dnc(curve,control_points,runtime_ms,iterations)

    # pop_up(control_points,iterations,runtime_ms)

def pop_up_normal_dnc(curve,control_points,runtime_ms,iteration):
    new_window = tk.Toplevel()
    new_window.title("Bezier Curve")
    texts = "Pilih hasil keluaran"
    label = tk.Label(new_window, text=texts, font=("Arial", 12), justify="center", anchor="center", fg="black", wraplength=500)
    label.grid(row=0, column=0)
    static = ttk.Button(new_window, text="Static Graph", command=lambda: plot_points(curve,control_points,runtime_ms))
    static.grid(row=1, column=0)
    animate1 = ttk.Button(new_window, text="Animation per iteration", command=lambda: animate_bezier(control_points, iteration,runtime_ms))
    animate1.grid(row=2, column=0)

def brute_force(root):
    control_points, iterations = input_box(root, 3)

    start_time = time.time()
    curve = bezier_brute_force(control_points,iterations)
    end_time = time.time()

    plot_points(curve,control_points)

    runtime_ms = (end_time-start_time) * 1000
    pop_up(control_points,iterations,runtime_ms)

def n_point_dnc(root):
    n = simpledialog.askinteger("Jumlah Titik Kontrol", "Masukkan jumlah titik kontrol (lebih dari 2)")
    control_points, iterations = input_box(root, n)

    start_time = time.time()
    curve = n_bezier_dnc(control_points,iterations)
    end_time = time.time()

    plot_points(curve,control_points)

    runtime_ms = (end_time-start_time) * 1000
    pop_up(control_points,iterations,runtime_ms)


