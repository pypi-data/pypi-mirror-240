import genera
from .ui import FragmentAmpUI
from .algo import FragmentAmpAlgo
from .data import FragmentAmpData
from typing import Tuple, List
from pandas import DataFrame
import time


class FragmentAmpApp(genera.classes.App):
    def __init__(self, settings={}, options={}):
        super().__init__()
        self.settings = genera.utils.settings.merge(
            [genera.utils.settings.load(__file__, "app.json"), settings]
        )
        self.options = genera.utils.options.merge([{"UI": "full"}, options])
        self.apps["primer_generator"] = genera.apps.PrimerGeneratorApp(
            settings=self.settings
        )
        self.ui = FragmentAmpUI(self.settings)
        self.algo = FragmentAmpAlgo(self.settings)
        self.data = FragmentAmpData(self.settings)

        self.init_app()

    def fragment_amp(
        self,
        fragments: Tuple[str] = None,
        load_file_path: str = None,
        save_file_path: str = None,
    ) -> List[DataFrame]:
        # 1. Read fragments from file
        if fragments is None:
            if load_file_path is not None:
                self.apps["primer_generator"].data.fragments_file_path = load_file_path
            if self.apps["primer_generator"].data.fragments_file_path is not None:
                self.apps["primer_generator"].data.load_fragments()
        else:
            self.apps["primer_generator"].data.list_to_seq(fragments)

        # 2. Fetch fragment parameters from UI or class settings input argument
        self.gather_fragment_parameters()

        # 3. Use Primer Generator to find the optimal fragments and primers
        (
            self.data.fragments,
            self.data.primers,
            self.data.shifts,
            self.data.overlaps,
        ) = self.algo.optimize_fragments_with_overlap(
            self.apps["primer_generator"].data.fragments
        )

        # 4. Write fragments to a FASTA file and the primers to an XLSX file with shift information wrt the original fragments
        if (
            save_file_path is None
            and self.apps["primer_generator"].data.primers_file_path
        ):
            self.data.write_FASTA(self.apps["primer_generator"].data.primers_file_path)
            self.data.write_primer_xlsx(
                self.apps["primer_generator"].data.primers_file_path
            )
        elif save_file_path:
            self.apps["primer_generator"].data.primers_file_path = save_file_path
            self.data.write_FASTA(self.apps["primer_generator"].data.primers_file_path)
            self.data.write_primer_xlsx(
                self.apps["primer_generator"].data.primers_file_path
            )

        return (
            self.data.fragments,
            self.data.primers,
            self.data.overlaps,
            self.data.shifts,
        )

    def init_app(self):
        self.apps["primer_generator"].init_app()
        self.algo.init_algo(self.apps["primer_generator"].primer_generator)
        if self.options["UI"] == "full":
            self.ui.init_ui(self.apps["primer_generator"].ui)
            self.ui.elements["fragment_amp_button"].config(
                command=self.run_fragment_amp
            )

    def run_fragment_amp(self):
        self.ui.elements["status_label"].config(text="Running ...")
        genera.ui.root.update()
        start_time = time.time()
        self.fragment_amp()
        end_time = time.time()
        self.ui.elements["status_label"].config(
            text=f"Done. {round(end_time-start_time)}s"
        )

    def gather_fragment_parameters(self):
        if self.options["UI"] == "hide":
            self.algo.max_fragment_shift = int(self.settings["max_fragment_shift"])
        elif self.options["UI"] == "full":
            self.algo.max_fragment_shift = int(
                self.ui.elements["max_fragment_shift_spinbox"].get()
            )
            self.algo.min_fragment_overlap = int(
                self.ui.elements["min_fragment_overlap_spinbox"].get()
            )


if __name__ == "__main__":
    app = FragmentAmpApp()
