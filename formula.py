# -*- coding: utf-8 -*-

SCALE_FREQ = (
    ["major"] * 2 +
    ["minor"] * 1
    )

NUM_BARS_FREQ = (
    [1] * 3 +
    [2] * 15 +
    [4] * 59 +
    [8] * 6
    )

CHORDS_PER_BAR_FREQ = (
    [1] * 84 +
    [2] * 19 +
    [3] * 2 +
    [4] * 1
    )

TIME_SIG_FREQ = (
    [4]
    )

BPM_TRIANGLE = ( 54, 141, 120 ) # (min, max, mode)

NUM_SECTIONS_FREQ = range(2, 7)

# repeats = REPEAT_BASE_FREQ + REPEAT_TEMPO_MOD_FREQ / bars_per_progression

REPEAT_BASE_FREQ = (
    [2] * 3 +
    [4] * 18 +
    [8] * 29 +
    [12] * 33 +
    [16] * 28 +
    [24] * 4
    )

REPEAT_SLOW_MOD_FREQ = (
    [0] * 12  +
    [2] * 12 +
    [4] * 2 +
    [8] * 1
    )

REPEAT_MODERATE_SLOW_MOD_FREQ = (
    [4] * 12 +
    [6] * 12 +
    [8] * 2 +
    [12] * 1
    )

REPEAT_MODERATE_MOD_FREQ = (
    [6] * 12 +
    [8] * 12 +
    [12] * 1
    )

REPEAT_FAST_MOD_FREQ = (
    [8] * 16 +
    [10] * 16 +
    [12] * 16 +
    [16] * 2 +
    [20] * 1
    )

MODULATION_FREQ = (
    ["none"] * 22 +
    ["parallel"] * 2 +
    ["relative"] * 2 +
    ["neighbour_up"] * 2 +
    ["neighbour_down"] * 2
    )

MAJOR_CHAIN = {
    "start": {"I": 50, "IV": 16, "V": 16, "ii": 7, "vi": 7}, # Starting Chord
    "I": {"I": 16, "ii": 16, "ii7": 1, "iii": 16, "III": 1, "iv": 1, "IV": 16,
          "V": 16, "v": 1, "V7": 1, "vi": 16, "viiø7": 0}, # Tonic
    "i": {"I": 16, "ii": 16, "ii7": 1, "iii": 16, "IV": 16, "iv": 1, "V": 16,
          "v": 1, "V7": 1, "vi": 16, "VI": 1, "viiø7": 0}, # Parallel Minor Chord
    "ii": {"V": 16, "v": 1, "V7": 1, "viiø7": 0}, # Super Tonic
    "ii7": {"V": 16, "v": 1, "V7": 1, "viiø7": 0}, # Seventh Chord
    "II": {"V": 16, "v": 1, "V7": 1, "viiø7": 0}, # Relative Major Chord
    "iii": {"vi": 16, "VI": 1, "IV": 16, "iv": 1, "ii": 16, "ii7": 1}, # Mediant
    "III": {"vi": 16, "IV": 16, "iv": 1, "ii": 16, "ii7": 1}, # Relative Major Chord
    "IV": {"V": 16, "v": 1, "ii": 16, "ii7": 1, "viiø7": 0}, # Subdominant
    "iv": {"V": 16, "v": 1, "ii": 16, "ii7": 1, "viiø7": 0}, # Parallel Minor Chord
    "V": {"I": 16, "vi": 16, "VI": 1,}, # Dominant
    "V7": {"I": 16, "vi": 16, "VI": 1},  # Seventh Chord
    "v": {"I": 16, "vi": 16, "VI": 1}, # Parallel Minor Chord
    "vi": {"ii": 16, "ii7": 1, "IV": 16, "iv": 1}, # Submediant
    "VI": {"ii": 16, "ii7": 1, "IV": 16, "iv": 1}, # Relative Major Chord
    "vii°": {"I": 16, "vi": 16, "VI": 1}, # Leading Tone
    "viiø7": {"I": 16, "vi": 16, "VI": 1}, # Seventh Chord
    "end_I": {"V": 32, "V7": 1, "IV": 1}, # Resolve Chords Starting First
    "end_other": {"I": 16, "V": 1, "V7": 1} # Resolve Chords Starting Any
}

MINOR_CHAIN = {
    "start": {"i": 40, "iv": 16, "v": 16}, # Starting Chord
    "i": {"i": 16, "iiø7": 0, "ii": 1, "III": 16, "iii":1, "iv": 16, "IV": 1,
          "v": 16, "V7": 1, "V": 1, "VI": 16, "VII": 16}, # Tonic
    "ii°": {"i": 2,"v": 16, "V": 1, "VII": 16}, # Super Tonic
    "ii": {"v": 16, "V": 1, "VII": 16}, # Relative Minor Chord
    "iiø7": {"v": 16, "V": 1, "VII": 16}, # Seventh Chord
    "III": {"VI": 16, "vi": 1, "iv": 16, "IV": 1, "iiø7": 0}, # Mediant
    "iii": {"VI": 1, "vi": 1, "iv": 16, "IV": 1, "iiø7": 0}, # Relative Minor Chord
    "iv": {"iiø7": 0, "VII": 16, "v": 16, "V": 1, "i": 2}, # Subdominant
    "IV": {"iiø7": 0, "VII": 16, "v": 16, "V": 1, "i": 2}, # Parallel Major Chord
    "v": {"i": 16, "VI": 16, "vi": 1}, # Dominant 
    "V": {"i": 16, "VI": 16, "vi": 1}, # Parallel Major Chord
    "V7": {"i": 16, "VI": 16}, # Seventh Chord
    "VI": {"iv": 16, "IV": 1, "iiø7": 0, "III":16, "iii":1}, # Submediant
    "vi": {"iv": 16, "IV": 1, "iiø7": 0}, # Relative Minor Chord
    "VII": {"III": 16, "iii":1}, # Leading Tone
    "vii°7": {"III": 16, "iii":1}, # Seventh Chord
    "end_I": {"v":8, "iv":1}, # Resolve Chords Starting First
    "end_other": {"i":16, "v":1} # Resolve Chords Starting Any
}

STRUCTURE_CHAIN = {
    "A": {"A": 1, "B": 6, "C": 6, "D": 5, "E": 3, "F": 3, "G": 3},
    "B": {"A": 6, "B": 1, "C": 3, "D": 5, "E": 3, "F": 3, "G": 3},
    "C": {"A": 6, "B": 4, "C": 1, "D": 4, "E": 3, "F": 3, "G": 3},
    "D": {"A": 2, "B": 2, "C": 2, "D": 1, "E": 6, "F": 3, "G": 3},
    "E": {"A": 4, "B": 2, "C": 4, "D": 4, "E": 1, "F": 4, "G": 3},
    "F": {"A": 3, "B": 3, "C": 3, "D": 3, "E": 3, "F": 1, "G": 3},
    "G": {"A": 1, "B": 1, "C": 1, "D": 1, "E": 1, "F": 1, "G": 1}
}