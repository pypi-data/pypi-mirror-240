import genera
from .ui import PrimerGeneratorUI
from .algo import PrimerGeneratorAlgo
from .data import PrimerGeneratorData
from typing import Tuple, List
from pandas import DataFrame


class PrimerGeneratorApp(genera.classes.App):
    def __init__(self, settings={}, options={}):
        super().__init__()
        self.settings = genera.utils.settings.merge(
            [genera.utils.settings.load(__file__, "app.json"), settings]
        )
        self.options = genera.utils.options.merge([{"UI": "full"}, options])
        self.ui = PrimerGeneratorUI(self.settings)
        self.algo = PrimerGeneratorAlgo(self.settings)
        self.data = PrimerGeneratorData(self.settings)
        self.init_app()

    def primer_generator(
        self,
        fragments: Tuple[str] = None,
        load_file_path: str = None,
        save_file_path: str = None,
    ) -> List[DataFrame]:
        # 1. Read fragments from file
        if fragments is None:
            if load_file_path is not None:
                self.data.fragments_file_path = load_file_path
            if self.data.fragments_file_path is not None:
                self.data.load_fragments()
        else:
            self.data.list_to_seq(fragments)
        self.data.reset_primers()

        # 2. Fetch primer parameters from UI or class settings input argument
        self.gather_primer_parameters()

        # 3. Use Primer3 to design primers for each fragment
        for fragment in self.data.fragments:
            primers = self.algo.generate_primers(fragment)
            self.data.add_primers(primers)

        # 4. write primers to an XLSX file
        self.data.extract_best_primers()
        if save_file_path is None and self.data.primers_file_path:
            self.data.write_primer_xlsx()
        elif save_file_path:
            self.data.primers_file_path = save_file_path
            self.data.write_primer_xlsx()

        return self.data.best_primers, self.data.primers

    def init_app(self):
        if self.options["UI"] == "full":
            self.ui.init_ui()
            self.ui.load_file_path.trace_add("write", self.load_file_callback)
            self.ui.save_file_path.trace_add("write", self.save_file_callback)
            self.ui.elements["generate_primers_button"].config(
                command=self.primer_generator
            )
            self.ui.elements["primer_checker_button"].config(command=self.check_primers)

    def load_file_callback(self, *args):
        file_path = self.ui.load_file_path.get()
        if file_path:
            self.data.fragments_file_path = file_path

    def save_file_callback(self, *args):
        file_path = self.ui.save_file_path.get()
        if file_path:
            self.data.primers_file_path = file_path

    def gather_primer_parameters(self):
        self.algo.parameters = {}
        if self.options["UI"] == "hide":
            for input_tag in self.ui.settings["T_inputs"]:
                self.algo.parameters[input_tag] = float(self.settings[input_tag])
            for input_tag in self.ui.settings["length_inputs"]:
                self.algo.parameters[input_tag] = int(self.settings[input_tag])
            self.algo.parameters["force_GC_end"] = int(self.settings["force_GC_end"])

        elif self.options["UI"] == "full":
            for input_tag in self.ui.settings["T_inputs"]:
                self.algo.parameters[input_tag] = float(
                    self.ui.elements[f"{input_tag}_spinbox"].get()
                )
            for input_tag in self.ui.settings["length_inputs"]:
                self.algo.parameters[input_tag] = int(
                    self.ui.elements[f"{input_tag}_spinbox"].get()
                )
            self.algo.parameters["force_GC_end"] = int(self.ui.force_GC_state.get())

    def check_primers(self):
        input_data = self.ui.elements["sequence_text"].get("1.0", "end-1c")
        sequence_list = [item.strip() for item in input_data.split(",")]
        df = self.algo.calculate_primer_properties(sequence_list)
        self.ui.init_primer_properties(df.columns.tolist(), df.values.tolist())
        pass


if __name__ == "__main__":
    app = PrimerGeneratorApp()
