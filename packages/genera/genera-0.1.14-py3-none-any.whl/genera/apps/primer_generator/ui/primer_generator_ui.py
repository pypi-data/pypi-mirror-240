import genera

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from typing import List


class PrimerGeneratorUI(genera.classes.UI):
    def __init__(self, settings={}):
        super().__init__()
        self.settings = genera.utils.settings.merge(
            [genera.utils.settings.load(__file__, "ui.json"), settings]
        )
        self.load_file_path = None
        self.save_file_path = None

    def init_ui(self):
        genera.ui.layout.init(self.frames, self.elements, self.settings["layout_full"])
        self.frames["primer_generator_frame"].config(
            text=self.settings["primer_generator_frame_label"]
        )
        self.elements["load_file_button"].config(
            text=self.settings["load_file_label"],
            command=self.set_load_file_path,
        )
        self.load_file_path = tk.StringVar()
        self.elements["load_file_input"].config(
            textvariable=self.load_file_path, state="readonly"
        )
        for input_tag in self.settings["T_inputs"]:
            self.elements[f"{input_tag}_label"].config(
                text=self.settings["T_inputs"][input_tag],
            )
            self.elements[f"{input_tag}_spinbox"].config(
                from_=0,
                to=100,
                increment=self.settings["T_input_increment"],
            )
            self.elements[f"{input_tag}_spinbox"].delete(0, "end")
            self.elements[f"{input_tag}_spinbox"].insert(
                0, str(self.settings[input_tag])
            )

        for input_tag in self.settings["length_inputs"]:
            self.elements[f"{input_tag}_label"].config(
                text=self.settings["length_inputs"][input_tag],
            )
            self.elements[f"{input_tag}_spinbox"].config(from_=0, to=100, increment=1)
            self.elements[f"{input_tag}_spinbox"].delete(0, "end")
            self.elements[f"{input_tag}_spinbox"].insert(
                0, str(self.settings[input_tag])
            )

        self.force_GC_state = tk.IntVar()
        self.elements["force_GC_end_label"].config(
            text=self.settings["force_GC_end_label"]
        )
        self.elements["force_GC_end_toggle"].config(
            text="",
            variable=self.force_GC_state,
        )
        self.force_GC_state.set(self.settings["force_GC_end"])

        self.elements["save_file_button"].config(
            text=self.settings["save_file_label"],
            command=self.set_save_file_path,
        )
        self.save_file_path = tk.StringVar()
        self.elements["save_file_input"].config(
            textvariable=self.save_file_path, state="readonly"
        )
        self.elements["generate_primers_button"].config(
            text=self.settings["generate_primers_label"],
            command=self.set_save_file_path,
            state="disabled",
        )
        self.generate_primers_button_enabled = tk.BooleanVar(value=False)
        self.frames["primer_checker_frame"].config(
            text=self.settings["primer_checker_frame_label"],
        )

        self.elements["sequence_text"].config(height=5, width=40)

        self.elements["primer_checker_button"].config(text="Check primers")
        # Show UI
        self.frames["primer_properties_frame"].grid_remove()
        genera.ui.root.deiconify()

    def set_load_file_path(self):
        file_path = filedialog.askopenfilename(
            filetypes=[
                (self.settings["load_file_type"], self.settings["load_file_ext"])
            ]
        )
        if file_path != "":
            self.load_file_path.set(file_path)
            if self.save_file_path.get() != "":
                self.elements["generate_primers_button"].config(state="normal")
                self.generate_primers_button_enabled.set(True)

    def set_save_file_path(self):
        file_path = filedialog.asksaveasfilename(
            filetypes=[
                (self.settings["save_file_type"], self.settings["save_file_ext"])
            ]
        )
        if file_path != "":
            self.save_file_path.set(file_path)
            if self.load_file_path.get() != "":
                self.elements["generate_primers_button"].config(state="normal")
                self.generate_primers_button_enabled.set(True)

    def init_primer_properties(self, columns, values):
        self.frames["primer_properties_frame"].config(
            text=self.settings["primer_properties_frame_label"]
        )
        self.elements["property_table"].config(columns=columns, show="headings")
        for col in columns:
            self.elements["property_table"].heading(col, text=col)
            self.elements["property_table"].column(col, width=200)
        for data_row in values:
            self.elements["property_table"].insert("", tk.END, values=data_row)
        self.elements["property_table"].pack()
        self.frames["primer_properties_frame"].grid()
