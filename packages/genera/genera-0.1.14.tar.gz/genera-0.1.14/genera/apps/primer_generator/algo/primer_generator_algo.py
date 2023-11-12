import genera
import primer3
from pandas import DataFrame
import numpy as np


class PrimerGeneratorAlgo(genera.classes.Algo):
    def __init__(self, settings={}):
        super().__init__()
        self.settings = genera.utils.settings.merge(
            [genera.utils.settings.load(__file__, "algo.json"), settings]
        )
        self.parameters = None

    def generate_primers(self, template: str) -> DataFrame:
        # We are doing multiple runs of primer3 with different sets of permissive parameters defined in algo.json
        results = []
        for i in range(len(self.settings["permissive_parameters"])):
            global_config = {
                **{
                    value: self.settings["permissive_parameters"][i][key]
                    for key, value in self.settings["parameter_inputs"].items()
                },
                **self.settings["additional_defaults"],
            }
            seq_config = {
                "SEQUENCE_ID": "example",
                "SEQUENCE_TEMPLATE": template,
                "SEQUENCE_INCLUDED_REGION": (0, len(template)),
                "PRIMER_PRODUCT_SIZE_RANGE": (len(template), len(template)),
            }
            results.append(primer3.bindings.design_primers(global_config, seq_config))

        df = DataFrame(columns=self.settings["output_labels"].values())
        for key in self.settings["output_labels"]:
            column_values = []
            for j in range(len(results)):
                if key == "PRIMER_LEFT_{}" or key == "PRIMER_RIGHT_{}":
                    column_values += [
                        results[j][key.format(i)][1]
                        for i in range(results[j]["PRIMER_PAIR_NUM_RETURNED"])
                    ]
                elif key == "PRIMER_LEFT_{}_TM" or key == "PRIMER_RIGHT_{}_TM":
                    column_values += [
                        results[j][key.format(i)] + self.settings["Tm_offset"]
                        for i in range(results[j]["PRIMER_PAIR_NUM_RETURNED"])
                    ]
                elif key == "pair_penalty":
                    pair_penalty, _, _ = self.calculate_penalty(results[j])
                    column_values += list(pair_penalty)
                elif key == "left_penalty":
                    _, left_penalty, _ = self.calculate_penalty(results[j])
                    column_values += list(left_penalty)
                elif key == "right_penalty":
                    _, _, right_penalty = self.calculate_penalty(results[j])
                    column_values += list(right_penalty)
                elif key == "pair_Tm_delta":
                    left_Tm = [
                        results[j]["PRIMER_LEFT_{}_TM".format(i)]
                        + self.settings["Tm_offset"]
                        for i in range(results[j]["PRIMER_PAIR_NUM_RETURNED"])
                    ]
                    right_Tm = [
                        results[j]["PRIMER_RIGHT_{}_TM".format(i)]
                        + self.settings["Tm_offset"]
                        for i in range(results[j]["PRIMER_PAIR_NUM_RETURNED"])
                    ]
                    column_values += [
                        abs(left_Tm[i] - right_Tm[i]) for i in range(len(left_Tm))
                    ]
                else:
                    column_values += [
                        results[j][key.format(i)]
                        for i in range(results[j]["PRIMER_PAIR_NUM_RETURNED"])
                    ]
            df[self.settings["output_labels"][key]] = column_values
        df.sort_values(by=self.settings["output_labels"]["pair_penalty"], inplace=True)
        df.reset_index(drop=True, inplace=True)
        df.drop_duplicates(inplace=True)
        df.reset_index(drop=True, inplace=True)
        return df

    def calculate_penalty(self, result):
        left_Tm = np.array(
            [
                result["PRIMER_LEFT_{}_TM".format(i)] + self.settings["Tm_offset"]
                for i in range(result["PRIMER_PAIR_NUM_RETURNED"])
            ]
        )
        right_Tm = np.array(
            [
                result["PRIMER_RIGHT_{}_TM".format(i)] + self.settings["Tm_offset"]
                for i in range(result["PRIMER_PAIR_NUM_RETURNED"])
            ]
        )
        left_hairpin_Tm = np.array(
            [
                result["PRIMER_LEFT_{}_HAIRPIN_TH".format(i)]
                for i in range(result["PRIMER_PAIR_NUM_RETURNED"])
            ]
        )
        right_hairpin_Tm = np.array(
            [
                result["PRIMER_RIGHT_{}_HAIRPIN_TH".format(i)]
                for i in range(result["PRIMER_PAIR_NUM_RETURNED"])
            ]
        )
        left_length = np.array(
            [
                result["PRIMER_LEFT_{}".format(i)][1]
                for i in range(result["PRIMER_PAIR_NUM_RETURNED"])
            ]
        )
        right_length = np.array(
            [
                result["PRIMER_RIGHT_{}".format(i)][1]
                for i in range(result["PRIMER_PAIR_NUM_RETURNED"])
            ]
        )

        pair_penalty = 0
        left_penalty = 0
        right_penalty = 0
        # delta Tm penalty
        pair_penalty += (
            np.maximum(0, np.abs(left_Tm - right_Tm) - self.parameters["max_Tm_delta"])
            ** 2
        )
        # hairpin penalty
        pair_penalty += (
            np.maximum(
                0,
                np.maximum(left_hairpin_Tm, right_hairpin_Tm)
                - self.parameters["max_hairpin_Tm"],
            )
            ** 2
        )
        left_penalty += (
            np.maximum(0, left_hairpin_Tm - self.parameters["max_hairpin_Tm"]) ** 2
        )
        right_penalty += (
            np.maximum(0, right_hairpin_Tm - self.parameters["max_hairpin_Tm"]) ** 2
        )
        # min Tm penalty
        pair_penalty += (
            np.maximum(0, self.parameters["min_Tm"] - np.minimum(left_Tm, right_Tm))
            ** 2
        )
        left_penalty += np.maximum(0, self.parameters["min_Tm"] - left_Tm) ** 2
        right_penalty += np.maximum(0, self.parameters["min_Tm"] - right_Tm) ** 2
        # max Tm penalty
        pair_penalty += (
            np.maximum(0, np.maximum(left_Tm, right_Tm) - self.parameters["max_Tm"])
            ** 2
        )
        left_penalty += np.maximum(0, left_Tm - self.parameters["max_Tm"]) ** 2
        right_penalty += np.maximum(0, left_Tm - self.parameters["max_Tm"]) ** 2
        # min length penalty
        pair_penalty += (
            np.maximum(
                0, self.parameters["min_length"] - np.minimum(left_length, right_length)
            )
            ** 2
        )
        left_penalty += np.maximum(0, self.parameters["min_length"] - left_length) ** 2
        right_penalty += (
            np.maximum(0, self.parameters["min_length"] - right_length) ** 2
        )
        # extra penalty if hairpin Tm > Tm
        pair_penalty[left_hairpin_Tm >= left_Tm] = np.Inf
        left_penalty[left_hairpin_Tm >= left_Tm] = np.Inf
        pair_penalty[right_hairpin_Tm >= right_Tm] = np.Inf
        right_penalty[right_hairpin_Tm >= right_Tm] = np.Inf
        return pair_penalty, left_penalty, right_penalty

    def calculate_primer_properties(self, primer_sequences):
        df = DataFrame(columns=self.settings["check_primer_labels"].values())
        df[self.settings["check_primer_labels"]["sequence"]] = primer_sequences
        df[self.settings["check_primer_labels"]["length"]] = [
            len(seq) for seq in primer_sequences
        ]
        df[self.settings["check_primer_labels"]["Tm"]] = [
            primer3.calc_tm(seq) for seq in primer_sequences
        ]
        df[self.settings["check_primer_labels"]["hairpin_Tm"]] = [
            primer3.calc_hairpin(seq).tm for seq in primer_sequences
        ]
        return df
