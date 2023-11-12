import genera
from pandas import DataFrame
import numpy as np
from typing import List, Tuple


class FragmentAmpAlgo(genera.classes.Algo):
    def __init__(self, settings={}):
        super().__init__()
        self.settings = genera.utils.settings.merge(
            [genera.utils.settings.load(__file__, "algo.json"), settings]
        )
        self.max_fragment_shift = None
        self.min_fragment_overlap = None
        self.primer_generator_fun = None

    def init_algo(self, primer_generator_fun):
        self.primer_generator_fun = primer_generator_fun

    def optimize_fragments_with_overlap(self, fragments: Tuple[str]):
        best_fragments = []
        best_shifts = []
        for i in range(len(fragments)):
            (
                fragment_list,
                shift_list,
                penalty_list,
            ) = self.shift_fragment_screening_for_good_primers(
                fragments[i],
                fragments[i - 1] if i > 0 else None,
                fragments[i + 1] if i < len(fragments) - 1 else None,
                [-1, -1],
            )
            best_index = np.argmin(np.array(penalty_list))
            best_fragments.append(fragment_list[best_index])
            best_shifts.append(shift_list[best_index])
        best_shifts = np.array(best_shifts)
        junction_overlaps = self.calculate_overlap_between_fragments(best_fragments)[
            :, 0
        ][1:]
        # Increase the overlap between fragments where we cut too much away
        fragments_tried = []
        while np.min(junction_overlaps) < self.min_fragment_overlap:
            junction_id = np.argmin(junction_overlaps)
            if best_shifts[junction_id, 1] < 0 and (
                best_shifts[junction_id, 1] <= best_shifts[junction_id + 1, 0]
            ):
                i = junction_id

            elif best_shifts[junction_id + 1, 0] < 0 and (
                best_shifts[junction_id + 1, 0] <= best_shifts[junction_id, 1]
            ):
                i = junction_id + 1
            if i in fragments_tried:
                break
            (
                fragment_list,
                shift_list,
                penalty_list,
            ) = self.shift_fragment_screening_for_good_primers(
                fragments[i],
                fragments[i - 1] if i > 0 else None,
                fragments[i + 1] if i < len(fragments) - 1 else None,
                [1, 1],
            )
            best_index = np.argmin(np.array(penalty_list))
            best_fragments[i] = fragment_list[best_index]
            best_shifts[i] = shift_list[best_index]
            junction_overlaps = self.calculate_overlap_between_fragments(
                best_fragments
            )[:, 0][1:]
            fragments_tried.append(i)
        best_primers, _ = self.primer_generator_fun(
            fragments=best_fragments, save_file_path=""
        )
        best_overlaps = self.calculate_overlap_between_fragments(best_fragments)
        return best_fragments, best_primers, best_shifts, best_overlaps

    def optimize_fragments_no_overlap(self, fragments: List[str]):
        # We are doing multiple runs of Primer Generator with shifts of the fragment boundaries
        fragment_penalties = []
        fragments_list = []
        shift_vectors = []
        penalty_list = []
        primers_list = []
        best_fragments_found = False
        shift_vectors.append(np.zeros(len(fragments) - 1))
        while not best_fragments_found:
            fragments_shifted = self.shift_fragments(fragments, shift_vectors[-1])
            fragments_list.append(fragments_shifted)
            primers, _ = self.primer_generator_fun(fragments=fragments_shifted)
            primers_list.append(primers)
            # pair_penalty = primers["Pair penalty"].to_numpy(dtype=float)
            # pair_penalty = pair_penalty[1:] + pair_penalty[:-1]
            left_penalty = primers["Left penalty"].to_numpy(dtype=float)
            right_penalty = primers["Right penalty"].to_numpy(dtype=float)
            pair_penalty = left_penalty[1:] + right_penalty[:-1]
            pair_penalty[np.isnan(pair_penalty)] = np.Inf
            penalty_list.append(pair_penalty)
            # left_penalty[np.isnan(left_penalty)] = np.Inf
            # right_penalty[np.isnan(right_penalty)] = np.Inf
            fragment_penalties.append(np.sum(pair_penalty))
            print(primers["Pair penalty"].to_numpy())
            print(shift_vectors[-1])
            if fragment_penalties[-1] > 0:
                new_shift_vector = self.calculate_shift_vector_no_overlap(
                    pair_penalty, shift_vectors[-1]
                )
                if np.all(shift_vectors[-1] == new_shift_vector):
                    break
                shift_vectors.append(new_shift_vector)
            else:
                best_fragments_found = True
        if best_fragments_found:
            best_index = -1
        else:
            best_index = np.argmin(np.array(fragment_penalties))
            # best_shift_vector = self.build_optimal_shift_vector(
            #    shift_vectors, penalty_list
            # )
            # best_fragments = self.shift_fragments(fragments, best_shift_vector)
            # best_primers, _ = self.primer_generator_fun(fragments=best_fragments)
            # return best_fragments, best_shift_vector, best_primers
        return (
            fragments_list[best_index],
            primers_list[best_index],
            None,
            shift_vectors[best_index],
        )

    def shift_fragment_screening_for_good_primers(
        self, fragment, prev_fragment, next_fragment, shift_direction
    ):
        fragment_list = []
        shift_list = []
        penalty_list = []
        shift_list.append(np.zeros(2, dtype=int))
        best_fragment_found = False
        changed_direction = [False, False]
        while not best_fragment_found:
            fragment_shifted = self.shift_fragment_with_overlap(
                fragment, prev_fragment, next_fragment, shift_list[-1]
            )
            fragment_list.append(fragment_shifted)
            primers, _ = self.primer_generator_fun(
                fragments=[fragment_shifted], save_file_path=""
            )
            pair_penalty = primers["Pair penalty"].to_numpy(dtype=float)
            left_penalty = primers["Left penalty"].to_numpy(dtype=float)
            right_penalty = primers["Right penalty"].to_numpy(dtype=float)
            pair_penalty = pair_penalty if not np.isnan(pair_penalty) else np.Inf
            left_penalty = left_penalty if not np.isnan(left_penalty) else np.Inf
            right_penalty = right_penalty if not np.isnan(right_penalty) else np.Inf
            penalty_list.append(pair_penalty)
            if pair_penalty > self.settings["tolerance"]:
                new_shift = shift_list[-1] * 1.0
                if left_penalty > 0:
                    new_shift[0] += shift_direction[0]
                if right_penalty > 0:
                    new_shift[1] += shift_direction[1]
                if left_penalty == 0 and right_penalty == 0:
                    ind = np.argmin(np.abs(new_shift))
                    new_shift[ind] += shift_direction[ind]
                if np.abs(new_shift[0]) > self.max_fragment_shift:
                    if not changed_direction[0]:
                        new_shift[0] = -shift_direction[0]
                        shift_direction[0] *= -1
                        changed_direction[0] = True
                    else:
                        new_shift[0] = shift_direction[0] * self.max_fragment_shift
                if np.abs(new_shift[1]) > self.max_fragment_shift:
                    if not changed_direction[0]:
                        new_shift[1] = -shift_direction[0]
                        shift_direction[1] *= -1
                        changed_direction[1] = True
                    else:
                        new_shift[1] = shift_direction[1] * self.max_fragment_shift
                if np.all(shift_list[-1] == new_shift):
                    break
                shift_list.append(new_shift.astype(int))
            else:
                best_fragment_found = True
        return fragment_list, shift_list, penalty_list

    def build_optimal_shift_vector(self, shift_vectors, penalty_list):
        penalty_array = np.array(penalty_list).T
        min_penality_indices = np.argmin(penalty_array, axis=1)
        best_shift_vector = np.zeros(len(penalty_array))
        for i in range(len(best_shift_vector)):
            best_shift_vector[i] = shift_vectors[min_penality_indices[i]][i]
        return best_shift_vector

    def calculate_shift_vector_no_overlap(self, pair_penalty, previous_shift_vector):
        # We can't modify the start of the 1st fragment or the end of the last fragment.
        bad_junctions = pair_penalty > self.settings["tolerance"]
        # bad_junctions = primers["Primer penalty"].to_numpy() > 0
        # bad_junctions = bad_junctions[:-1] | bad_junctions[1:]
        # Calculate next shift vector
        if np.all(previous_shift_vector == 0):
            new_shift_vector = bad_junctions * 1.0
        else:
            new_shift_vector = previous_shift_vector * 1.0
            # If previously we have shifted in the positive direction, we reverse the direction of the shift.
            # If previously the shift was in the negative direction, we reverse the direction and increment the shift.
            new_shift_vector[previous_shift_vector < 0] -= 1
            new_shift_vector *= -1
            # Clamp the shift to the user defined maximum shift
            new_shift_vector[
                new_shift_vector > self.max_fragment_shift
            ] = -self.max_fragment_shift
            # We set the shifts to the previous shifts where the penalty is 0
            new_shift_vector[~bad_junctions] = previous_shift_vector[~bad_junctions]
        return new_shift_vector.astype(int)

    def shift_fragments_no_overlap(self, fragments, shift_vector):
        fragments_shifted = fragments[:]
        shift_vector = shift_vector.astype(int)
        for i, shift in enumerate(shift_vector):
            if shift < 0:
                fragments_shifted[i] = fragments[i][:shift]
                fragments_shifted[i + 1] = fragments[i][shift:] + fragments[i + 1]
            elif shift > 0:
                fragments_shifted[i] = fragments[i] + fragments[i + 1][:shift]
                fragments_shifted[i + 1] = fragments[i + 1][shift:]
        return fragments_shifted

    def shift_fragment_with_overlap(
        self, fragment, prev_fragment, next_fragment, shift
    ):
        if shift[0] > 0 and prev_fragment is not None:
            overlap = overlap_between_strings_end_start(prev_fragment, fragment)
            fragment = prev_fragment[-overlap - shift[0] : -overlap] + fragment
        elif shift[0] < 0:
            fragment = fragment[-shift[0] :]
        if shift[1] > 0 and next_fragment is not None:
            overlap = overlap_between_strings_end_start(fragment, next_fragment)
            fragment += next_fragment[overlap : overlap + shift[1]]
        elif shift[1] < 0:
            fragment = fragment[: shift[1]]
        return fragment

    def calculate_overlap_between_fragments(self, fragments):
        overlap = np.zeros(len(fragments) - 1)
        for i in range(len(overlap)):
            overlap[i] = overlap_between_strings_end_start(
                fragments[i], fragments[i + 1]
            )
        return np.vstack([np.insert(overlap, 0, 0), np.append(overlap, 0)]).T

    def calculate_relative_shift(self, old_fragments, new_fragments):
        relative_shift = []
        for i in range(len(old_fragments)):
            relative_shift.append(
                shift_between_strings(old_fragments[i], new_fragments[i])
            )
        return np.array(relative_shift)


def overlap_between_strings_end_start(str1, str2):
    overlap = 0
    for i in range(1, min(len(str1), len(str2)) + 1):
        if str1[-i:] == str2[:i]:
            overlap = i
    return overlap


def shift_between_strings(str1, str2):
    matrix = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    max_length = 0
    str1_end_position = 0
    str2_end_position = 0
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
                if matrix[i][j] > max_length:
                    max_length = matrix[i][j]
                    str1_end_position = i
                    str2_end_position = j
    shift_start = str2_end_position - str1_end_position
    shift_end = (len(str2) - str2_end_position) - (len(str1) - str1_end_position)
    return [shift_start, shift_end]
