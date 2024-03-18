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

"""------------------FUNGSI VISUALISASI TITIK-------------------- """

def plot_points(result,control,runtime):
    curve_x, curve_y = zip(*result)
    control_x, control_y = zip(*control)

    plt.plot(curve_x, curve_y, label='Bezier Curve')
    plt.plot(control_x, control_y, color='red', label='Control Points')
    plt.title(f"Bezier Curve - Runtime (overall): {runtime} ms")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()

def animate(iteration, controlpoints, ax, runtime,n):
    ax.clear()
    if (n ==1):
        curve = bezier_brute_force(controlpoints,iteration)
    elif (n==2):
        curve = bezier_dnc(controlpoints, iteration)

    
    ax.plot(*zip(*curve), marker='o', color='b')
    ax.plot(*zip(*controlpoints), marker='o', color='r')
    ax.set_title(f"Iteration {iteration} - Runtime (overall): {runtime} ms")
    ax.set_aspect('equal', 'box')
    ax.grid(True)

def animate_bezier(controlpoints, iteration, runtime_ms,n):
    fig, ax = plt.subplots()
    
    def animate_wrapper(iteration):
        animate(iteration, controlpoints, ax, runtime_ms,n)
    
    ani = FuncAnimation(fig, animate_wrapper, frames=iteration+1, interval=1000, repeat=False)
    plt.show()

def plot_per_points_brute(result, control, runtime):
    curve_x, curve_y = [], []
    control_x, control_y = zip(*control)

    plt.plot(control_x, control_y, color='red', label='Control Points')

    plt.title(f"Bezier Curve - Runtime (overall): {runtime} ms")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.legend()

    for i in range(len(result)):
        curve_x.append(result[i][0])
        curve_y.append(result[i][1])
        plt.plot(curve_x, curve_y, marker='o', color='b')
        if i > 0:
            plt.plot([result[i-1][0], result[i][0]], [result[i-1][1], result[i][1]], color='b')
        plt.pause(0.3)  
    plt.show()

def plot_per_points_dnc(controlpoints, num_iterations,runtime):
    fig, ax = plt.subplots()
    
    for i in range(num_iterations):
        curve_points = bezier_dnc(controlpoints, i)
        for j in range(len(curve_points)):
            x, y = curve_points[j]
            ax.plot(x, y, marker='o', color='gray') 
            if j > 0:
                prev_x, prev_y = curve_points[j - 1]
                ax.plot([prev_x, x], [prev_y, y], color='gray')  
                
            plt.pause(0.3)  
        
    final_points = bezier_dnc(controlpoints, num_iterations)
    final_x, final_y = zip(*final_points)
    ax.plot(final_x, final_y, marker='o', color='red', label='Final Points', linestyle='-', linewidth=2)

    plt.title(f'Runtime (overall): {runtime} ms')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()  

def precompute_results_n_bezier(control_points, num_of_iterations):
    results = []
    for i in range(1, num_of_iterations + 1):
        result_points = n_bezier_dnc(control_points, i)
        results.append(result_points)
    return results

def animate_n_bezier(iteration, results, ax, control_points, runtime):
    ax.clear()
    result_points = results[iteration]
    curve_x, curve_y = zip(*result_points)
    ax.plot(*zip(*control_points), marker='o', color='r') 
    ax.plot(curve_x, curve_y, marker='o', color='b', label='Bezier Curve')
    control_x, control_y = zip(*control_points)
    ax.scatter(control_x, control_y, color='r', label='Control Points')
    ax.set_title(f"Iteration {iteration} - Runtime (overall): {runtime} ms")
    ax.legend()
    ax.set_aspect('equal', 'box')
    ax.grid(True)

def animate_bezier_n_bezier(control_points, num_of_iterations, run_time):
    results = precompute_results_n_bezier(control_points, num_of_iterations)
    fig, ax = plt.subplots()
    ani = FuncAnimation(fig, animate_n_bezier, frames=num_of_iterations, fargs=(results, ax, control_points, run_time), interval=1000, repeat=False)
    plt.show()

"""------------------POP UP-------------------- """

def pop_up_normal_dnc(curve,control_points,runtime_ms,iteration):
    new_window = tk.Toplevel()
    new_window.title("Bezier Curve")
    texts = "Pilih hasil keluaran"
    label = tk.Label(new_window, text=texts, font=("Arial", 12), justify="center", anchor="center", fg="black", wraplength=500)
    label.grid(row=0, column=0)
    static = ttk.Button(new_window, text="Static Graph", command=lambda: plot_points(curve,control_points,runtime_ms))
    static.grid(row=1, column=0)
    animate1 = ttk.Button(new_window, text="Animation per iteration", command=lambda: animate_bezier(control_points, iteration,runtime_ms,2))
    animate1.grid(row=2, column=0)
    animate2 = ttk.Button(new_window, text="Animation per points", command=lambda: plot_per_points_dnc(control_points,iteration,runtime_ms))
    animate2.grid(row=3, column=0)

def pop_up_brute(curve,control_points,runtime_ms,iteration):
    new_window = tk.Toplevel()
    new_window.title("Bezier Curve")
    texts = "Pilih hasil keluaran"
    label = tk.Label(new_window, text=texts, font=("Arial", 12), justify="center", anchor="center", fg="black", wraplength=500)
    label.grid(row=0, column=0)
    static = ttk.Button(new_window, text="Static Graph", command=lambda: plot_points(curve,control_points,runtime_ms))
    static.grid(row=1, column=0)
    animate1 = ttk.Button(new_window, text="Animation per iteration", command=lambda: animate_bezier(control_points, iteration,runtime_ms,1))
    animate1.grid(row=2, column=0)
    animate2 = ttk.Button(new_window, text="Animation per points", command=lambda: plot_per_points_brute(curve,control_points,runtime_ms))
    animate2.grid(row=3, column=0)

def pop_up_n(curve,control_points,runtime_ms,iteration):
    new_window = tk.Toplevel()
    new_window.title("Bezier Curve")
    texts = "Pilih hasil keluaran"
    label = tk.Label(new_window, text=texts, font=("Arial", 12), justify="center", anchor="center", fg="black", wraplength=500)
    label.grid(row=0, column=0)
    static = ttk.Button(new_window, text="Static Graph", command=lambda: plot_points(curve,control_points,runtime_ms))
    static.grid(row=1, column=0)
    animate1 = ttk.Button(new_window, text="Animation per iteration", command=lambda: animate_bezier_n_bezier(control_points, iteration,runtime_ms))
    animate1.grid(row=2, column=0)
  

"""------------------BUTTON INITIALIZE-------------------- """

def normal_dnc(root):
    control_points, iterations = input_box(root, 3)

    start_time = time.time()
    curve = bezier_dnc(control_points,iterations)
    end_time = time.time()
    runtime_ms = (end_time-start_time) * 1000

    pop_up_normal_dnc(curve,control_points,runtime_ms,iterations)
 
def brute_force(root):
    control_points, iterations = input_box(root, 3)

    start_time = time.time()
    curve = bezier_brute_force(control_points,iterations)
    end_time = time.time()

    runtime_ms = (end_time-start_time) * 1000
    pop_up_brute(curve,control_points,runtime_ms,iterations)

def n_point_dnc(root):
    n = simpledialog.askinteger("Jumlah Titik Kontrol", "Masukkan jumlah titik kontrol (lebih dari 2)")
    control_points, iterations = input_box(root, n)

    start_time = time.time()
    curve = n_bezier_dnc(control_points,iterations)
    end_time = time.time()

    runtime_ms = (end_time-start_time) * 1000
    pop_up_n(curve,control_points,runtime_ms,iterations)

