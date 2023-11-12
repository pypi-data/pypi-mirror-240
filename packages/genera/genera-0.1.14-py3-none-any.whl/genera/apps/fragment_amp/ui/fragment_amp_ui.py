import genera

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from typing import List


class FragmentAmpUI(genera.classes.UI):
    def __init__(self, settings={}):
        super().__init__()
        self.settings = genera.utils.settings.merge(
            [genera.utils.settings.load(__file__, "ui.json"), settings]
        )
        self.load_file_path = None
        self.save_file_path = None
        self.primer_generator_ui = None

    def init_ui(self, primer_generator_ui):
        self.primer_generator_ui = primer_generator_ui
        self.frames = self.primer_generator_ui.frames
        genera.ui.layout.init(self.frames, self.elements, self.settings["layout_full"])
        self.frames["primer_properties_frame"].grid_remove()
        self.frames["fragment_amp_frame"].config(
            text=self.settings["fragment_amp_frame_label"]
        )
        self.primer_generator_ui.generate_primers_button_enabled.trace_add(
            "write", self.set_fragment_amp_button_state
        )
        self.primer_generator_ui.elements["generate_primers_button"].grid_remove()
        self.elements["max_fragment_shift_spinbox"].config(
            from_=0,
            to=100,
            increment=1,
        )
        self.elements["max_fragment_shift_spinbox"].delete(0, "end")
        self.elements["max_fragment_shift_spinbox"].insert(
            0, str(self.settings["max_fragment_shift"])
        )
        self.elements["min_fragment_overlap_spinbox"].delete(0, "end")
        self.elements["min_fragment_overlap_spinbox"].insert(
            0, str(self.settings["min_fragment_overlap"])
        )
        self.elements["fragment_amp_button"].config(
            state="disabled", text=self.settings["fragment_amp_button_label"]
        )
        self.elements["max_fragment_shift_label"].config(
            text=self.settings["max_fragment_shift_label"]
        )
        self.elements["min_fragment_overlap_label"].config(
            text=self.settings["min_fragment_overlap_label"]
        )

    def set_fragment_amp_button_state(self, *args):
        if self.primer_generator_ui.generate_primers_button_enabled.get():
            state = "normal"
        else:
            state = "disabled"
        self.elements["fragment_amp_button"].config(state=state)
