import genera
from Bio import Seq, SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import pandas as pd
import os
import numpy as np


class FragmentAmpData(genera.classes.Data):
    def __init__(self, settings={}):
        super().__init__()
        self.settings = genera.utils.settings.merge(
            [genera.utils.settings.load(__file__, "data.json"), settings]
        )
        self.fragments = None
        self.shifts = None
        self.overlaps = None
        self.primers = None

    def write_FASTA(self, file_path):
        file_stem, file_extension = os.path.splitext(file_path)
        file_path = file_stem + ".fasta"

        if os.path.exists(file_path):
            os.remove(file_path)
        seq_records = [
            SeqRecord(Seq(self.fragments[i]), id=f"fragment{i+1}", description="")
            for i in range(len(self.fragments))
        ]
        with open(file_path, "w") as output_handle:
            SeqIO.write(seq_records, output_handle, "fasta")

    def write_primer_xlsx(self, file_path):
        file_stem, file_extension = os.path.splitext(file_path)
        file_path = file_stem + "_fragments.xlsx"
        if os.path.exists(file_path):
            os.remove(file_path)

        with pd.ExcelWriter(file_path) as writer:
            summary_df = self.primers.copy()
            if len(self.shifts.shape) == 1:
                summary_df.insert(
                    loc=1,
                    column="Fragment right shift",
                    value=np.append(self.shifts, 0),
                )
                summary_df.insert(
                    loc=1,
                    column="Fragment left shift",
                    value=np.insert(self.shifts, 0, 0),
                )
            else:
                summary_df.insert(
                    loc=1,
                    column="Fragment right overlap",
                    value=self.overlaps[:, 1],
                )
                summary_df.insert(
                    loc=1,
                    column="Fragment left overlap",
                    value=self.overlaps[:, 0],
                )
                summary_df.insert(
                    loc=1,
                    column="Fragment right shift",
                    value=self.shifts[:, 1],
                )
                summary_df.insert(
                    loc=1,
                    column="Fragment left shift",
                    value=self.shifts[:, 0],
                )
            summary_df.to_excel(writer, sheet_name=f"Best primers", index=False)
