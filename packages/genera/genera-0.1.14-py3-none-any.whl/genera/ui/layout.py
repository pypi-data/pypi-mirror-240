from .root import root
import numpy as np
import tkinter as tk
from tkinter import ttk

padding = 5


def init(frames, elements, layout):
    frames_array = np.array(layout["frames"])
    for frame_key in np.unique(frames_array):
        if frame_key not in frames:
            frames[frame_key] = ttk.LabelFrame(root)
        if frame_key in layout:
            elements_array = np.array(layout[frame_key]["elements"])
        else:
            continue
        for element_key in np.unique(elements_array):
            if element_key in elements:
                continue
            if element_key.endswith("_button"):
                elements[element_key] = ttk.Button(frames[frame_key])
            elif element_key.endswith("_input"):
                elements[element_key] = ttk.Entry(frames[frame_key])
            elif element_key.endswith("_text"):
                elements[element_key] = tk.Text(frames[frame_key])
            elif element_key.endswith("_spinbox"):
                elements[element_key] = ttk.Spinbox(frames[frame_key])
            elif element_key.endswith("_label"):
                elements[element_key] = ttk.Label(frames[frame_key])
            elif element_key.endswith("_toggle"):
                elements[element_key] = ttk.Checkbutton(frames[frame_key])
            elif element_key.endswith("_table"):
                elements[element_key] = ttk.Treeview(frames[frame_key])
        arrange(elements, elements_array, padding)
    arrange(frames, frames_array, padding * 2)


# Set grid row, column, rowspan, columnspan
def arrange(ui_objects, layout_array, padding):
    dims = layout_array.shape
    positions = calculate_positions(layout_array)
    for key, value in positions.items():
        padx = [padding, padding]
        pady = [padding, padding]
        if value["row"] == 0:
            pady[0] *= 2
        elif value["row"] + value["rowspan"] == dims[0]:
            pady[1] *= 2
        if value["column"] == 0:
            padx[0] *= 2
        elif value["column"] + value["columnspan"] == dims[1]:
            padx[1] *= 2
        ui_objects[key].grid(
            row=value["row"],
            column=value["column"],
            rowspan=value["rowspan"],
            columnspan=value["columnspan"],
            padx=padx,
            pady=pady,
            sticky="nsew",
        )
        if isinstance(ui_objects[key], ttk.LabelFrame):
            rows, columns = ui_objects[key].grid_size()
            for row in range(rows):
                ui_objects[key].columnconfigure(row, weight=1)
            for column in range(columns):
                ui_objects[key].columnconfigure(column, weight=1)


def calculate_positions(layout_array):
    names = np.unique(layout_array)
    positions = {}
    for name in names:
        coords = np.argwhere(layout_array == name)
        positions[name] = {
            "row": coords[0, 0],
            "column": coords[0, 1],
            "rowspan": coords[-1, 0] - coords[0, 0] + 1,
            "columnspan": coords[-1, 1] - coords[0, 1] + 1,
        }
    return positions
