import tkinter as tk
from tkinter import ttk

class InputBox(tk.Toplevel):
    def __init__(self, parent, n):
        super().__init__(parent)
        self.parent = parent
        self.title("Bezier Curve Inputs")

        # STYLING
        self.style = ttk.Style()
        self.style.configure('InputBox.TFrame', background='#f8c4cc')  
        self.style.configure('InputBox.TSpinbox', padding=5)  
        self.style.configure('InputBox.TButton', padding=5)  

        self.main_frame = ttk.Frame(self, style='InputBox.TFrame')
        self.main_frame.pack(padx=10, pady=10)

        # TITLE
        self.title_input = tk.Label(self.main_frame, text="INPUT BEZIER", font=("Arial", 24, "bold"))
        self.title_input.grid(row=0, column=0, columnspan=4, sticky=tk.E + tk.W, padx=5, pady=5)
        self.petunjuk = tk.Label(self.main_frame, text="Masukkan posisi titik kontrol dan jumlah iterasi", background='#F8C4CC', font=("Arial", 12))
        self.petunjuk.grid(row=1, column=0, columnspan=4, sticky=tk.E + tk.W, padx=5, pady=5)

        # INPUT CONTROL POINTS
        self.entry_widgets = []
        for i in range(0, n):
            temp = []
            # X
            label_x = ttk.Label(self.main_frame, text="X" + str(i+1) + ":")  
            label_x.grid(row=2+i, column=0, sticky=tk.E, padx=5, pady=5)
            entry_x = ttk.Entry(self.main_frame)
            entry_x.grid(row=2+i, column=1, padx=5, pady=5)
            temp.append(entry_x)
            # Y
            label_y = ttk.Label(self.main_frame, text="Y" + str(i+1) + ":") 
            label_y.grid(row=2+i, column=2, sticky=tk.E, padx=5, pady=5)
            entry_y = ttk.Entry(self.main_frame)
            entry_y.grid(row=2+i, column=3, padx=5, pady=5)
            temp.append(entry_y)
            self.entry_widgets.append((temp[0], temp[1]))

        # NUMBER OF ITERATIONS
        self.iteration_label = ttk.Label(self.main_frame, text="Jumlah Iterasi:")
        self.iteration_label.grid(row=n + 2, columnspan=2, sticky=tk.E + tk.W, padx=5, pady=5)
        self.iteration_input = ttk.Spinbox(self.main_frame, from_=1, to=1e10, increment=1)
        self.iteration_input.grid(row=n + 2, column=2, columnspan=2, sticky=tk.E + tk.W, padx=5, pady=5)

        # SUBMIT
        self.submit_button = ttk.Button(self.main_frame, text="Submit", command=self.submit, style='InputBox.TButton')
        self.submit_button.grid(row=n + 3, column=0, columnspan=4, sticky=tk.E + tk.W, padx=5, pady=5)

    def submit(self):
        global control_points
        global iterations
        
        control_points = []
        for entry_x, entry_y in self.entry_widgets:
            x_value = entry_x.get()
            y_value = entry_y.get()
            control_points.append(int(x_value), int(y_value))
        iterations = int(self.iteration_input.get())

        self.destroy()


# Example usage:
root = tk.Tk()

# Initialize global variables
control_points = []
iterations = 0

def plot_bezier_curve():
    # Your plot code using global control_points and iterations
    pass

def open_input_dialog():
    global control_points
    global iterations
    
    dialog = InputBox(root, 3)  # Assuming 3 control points
    root.wait_window(dialog)
    # After dialog is closed, use updated global variables
    print("Control Points:", control_points)
    print("Iterations:", iterations)
    plot_bezier_curve()

# Button to open input dialog
btn_open_dialog = tk.Button(root, text="Open Input Dialog", command=open_input_dialog)
btn_open_dialog.pack()

root.mainloop()
