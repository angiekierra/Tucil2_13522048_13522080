    for entry_x, entry_y in entry_widgets:
            x_value = entry_x.get()
            y_value = entry_y.get()
            control_points.append((int(x_value), int(y_value)))
        iterations = int(iteration_input.get())
        dialog.destroy()