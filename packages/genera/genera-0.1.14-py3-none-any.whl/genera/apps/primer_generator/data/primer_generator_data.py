import genera
from Bio import Seq, SeqIO
from Bio.Seq import Seq
import pandas as pd
import os
import numpy as np


class PrimerGeneratorData(genera.classes.Data):
    def __init__(self, settings={}):
        super().__init__()
        self.settings = genera.utils.settings.merge(
            [genera.utils.settings.load(__file__, "data.json"), settings]
        )
        self.fragments = None
        self.primers = None
        self.fragments_file_path = None
        self.primers_file_path = None
        self.best_primers = None

    def load_fragments(self, file_path=None):
        if file_path is None:
            file_path = self.fragments_file_path
        self.fragments = []
        for record in SeqIO.parse(file_path, "fasta"):
            self.fragments.append(record.seq)
        self.fragments = tuple(self.fragments)

    def add_primers(self, primers):
        if self.primers is None:
            self.primers = []
        self.primers.append(primers)

    def reset_primers(self):
        self.primers = None

    def extract_best_primers(self):
        rows = []
        for i, df in enumerate(self.primers):
            if df.empty:
                # Create a Series of NaNs with the same columns as the first DataFrame in self.primers
                rows.append(
                    pd.Series(
                        [np.nan] * len(self.primers[0].columns),
                        index=self.primers[0].columns,
                        name=f"DF{i}",
                    )
                )
            else:
                rows.append(df.iloc[0].rename(f"DF{i}"))
        self.best_primers = pd.concat(rows, axis=1).T.reset_index(drop=True)
        self.best_primers.insert(
            loc=0, column="Fragment", value=range(1, len(self.best_primers) + 1)
        )

    def write_primer_xlsx(self, file_path=None):
        if file_path is None:
            file_path = self.primers_file_path

        if os.path.exists(file_path):
            os.remove(file_path)

        with pd.ExcelWriter(file_path) as writer:
            self.best_primers.to_excel(writer, sheet_name=f"Best primers", index=False)
            for i in range(len(self.primers)):
                self.primers[i].to_excel(
                    writer, sheet_name=f"Fragment {i+1}", index=False
                )

    def list_to_seq(self, fragments):
        self.fragments = [Seq(seq) for seq in fragments]
