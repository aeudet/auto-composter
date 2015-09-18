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
  
STRUCTURE_CHAIN = {
    "A": {"A": 1, "B": 6, "C": 6, "D": 5, "E": 3, "F": 3, "G": 3},
    "B": {"A": 6, "B": 1, "C": 3, "D": 5, "E": 3, "F": 3, "G": 3},
    "C": {"A": 6, "B": 4, "C": 1, "D": 4, "E": 3, "F": 3, "G": 3},
    "D": {"A": 2, "B": 2, "C": 2, "D": 1, "E": 6, "F": 3, "G": 3},
    "E": {"A": 4, "B": 2, "C": 4, "D": 4, "E": 1, "F": 4, "G": 3},
    "F": {"A": 3, "B": 3, "C": 3, "D": 3, "E": 3, "F": 1, "G": 3},
    "G": {"A": 1, "B": 1, "C": 1, "D": 1, "E": 1, "F": 1, "G": 1}
}

MAJOR_CHAIN = {

# Starting Chords

    # Start
    "start": {
        # Primary
        "I": 60, "ii": 6, "iii": 0, "IV": 6, "V": 7, "vi": 1, "viiø7": 0,
        # Sevenths
        "I7": 0, "ii7": 0, "iii7": 0, "IV7": 0, "V7": 0, "vi7": 0,
        # Parallel/Relative
        "i": 0, "II": 0, "III": 0, "iv": 0, "v": 0, "VI": 0
        },

# Regular Tones Major
        
    # Tonic (I)
    "I": {
        # Primary
        "I": 60, "ii": 60, "iii": 60, "IV": 60, "V": 60, "vi": 60, "viiø7": 0,
        # Sevenths
        "I7": 2, "ii7": 4, "iii7": 0, "IV7": 0, "V7": 4, "vi7": 0,
        # Parallel/Relative
        "i": 0, "II": 0, "III": 0, "iv": 0, "v": 0, "VI": 0
        },

    # Super Tonic (ii)
    "ii": {
        # Primary
        "I": 3, "ii": 0, "iii": 0, "IV": 0, "V": 60, "vi": 0, "viiø7": 0,
        # Sevenths
        "I7": 0, "ii7": 0, "iii7": 0, "IV7": 2, "V7": 0, "vi7": 0,
        # Parallel/Relative
        "i": 0, "II": 0, "III": 0, "iv": 0, "v": 0, "VI": 0
        },

    # Mediant (iii)    
    "iii": {
        # Primary
        "I": 0, "ii": 60, "iii": 0, "IV": 60, "V": 0, "vi": 60, "viiø7": 0,
        # Sevenths
        "I7": 0, "ii7": 3, "iii7": 0, "IV7": 0, "V7": 0, "vi7": 0,
        # Parallel/Relative
        "i": 0, "II": 0, "III": 0, "iv": 0, "v": 0, "VI": 0
        },

    # Subdominant (IV)
    "IV": {
        # Primary
        "I": 0, "ii": 60, "iii": 0, "IV": 0, "V": 60, "vi": 0, "viiø7": 0,
        # Sevenths
        "I7": 0, "ii7": 2, "iii7": 0, "IV7": 0, "V7": 0, "vi7": 0,
        # Parallel/Relative
        "i": 0, "II": 0, "III": 0, "iv": 0, "v": 0, "VI": 0
        },

    # Dominant (V)
    "V": {
        # Primary
        "I": 60, "ii": 0, "iii": 0, "IV": 60, "V": 0, "vi": 60, "viiø7": 0,
        # Sevenths
        "I7": 0, "ii7": 0, "iii7": 0, "IV7": 2, "V7": 3, "vi7": 0,
        # Parallel/Relative
        "i": 0, "II": 0, "III": 0, "iv": 0, "v": 0, "VI": 0
        },

    # Submediant (vi)
    "vi": {
        # Primary
        "I": 0, "ii": 60, "iii": 0, "IV": 60, "V": 0, "vi": 0, "viiø7": 0,
        # Sevenths
        "I7": 0, "ii7": 2, "iii7": 0, "IV7": 0, "V7": 0, "vi7": 0,
        # Parallel/Relative
        "i": 0, "II": 0, "III": 0, "iv": 0, "v": 0, "VI": 0
        },

    # Leading Tone (vii)
    "vii°": {
        # Primary
        "I": 60, "ii": 0, "iii": 0, "IV": 0, "V": 0, "vi": 60, "viiø7": 0,
        # Sevenths
        "I7": 0, "ii7": 0, "iii7": 0, "IV7": 0, "V7": 0, "vi7": 0,
        # Parallel/Relative
        "i": 0, "II": 0, "III": 0, "iv": 0, "v": 0, "VI": 0
        },

# Irregular Tones Major

    # Parallel Minor Tonic (i)
    "i": {
        # Primary
        "I": 60, "ii": 60, "iii": 60, "IV": 60, "V": 60, "vi": 60, "viiø7": 0,
        # Sevenths
        "I7": 2, "ii7": 4, "iii7": 0, "IV7": 0, "V7": 4, "vi7": 0,
        # Parallel/Relative
        "i": 0, "II": 0, "III": 0, "iv": 0, "v": 0, "VI": 0
        },

    # Relative Major Chord (II)
    "II": {
        # Primary
        "I": 3, "ii": 0, "iii": 0, "IV": 0, "V": 60, "vi": 0, "viiø7": 0,
        # Sevenths
        "I7": 0, "ii7": 0, "iii7": 0, "IV7": 2, "V7": 0, "vi7": 0,
        # Parallel/Relative
        "i": 0, "II": 0, "III": 0, "iv": 0, "v": 0, "VI": 0
        },

    # Relative Major Chord (III)
    "III": {
        # Primary
        "I": 0, "ii": 60, "iii": 0, "IV": 60, "V": 0, "vi": 60, "viiø7": 0,
        # Sevenths
        "I7": 0, "ii7": 3, "iii7": 0, "IV7": 0, "V7": 0, "vi7": 0,
        # Parallel/Relative
        "i": 0, "II": 0, "III": 0, "iv": 0, "v": 0, "VI": 0
        },

    # Parallel Minor Chord (iv)
    "iv": {
        # Primary
        "I": 0, "ii": 60, "iii": 0, "IV": 0, "V": 60, "vi": 0, "viiø7": 0,
        # Sevenths
        "I7": 0, "ii7": 2, "iii7": 0, "IV7": 0, "V7": 0, "vi7": 0,
        # Parallel/Relative
        "i": 0, "II": 0, "III": 0, "iv": 0, "v": 0, "VI": 0
        }, 
    
    # Parallel Minor Chord (v)
    "v": {
        # Primary
        "I": 60, "ii": 0, "iii": 0, "IV": 60, "V": 0, "vi": 60, "viiø7": 0,
        # Sevenths
        "I7": 0, "ii7": 0, "iii7": 0, "IV7": 2, "V7": 3, "vi7": 0,
        # Parallel/Relative
        "i": 0, "II": 0, "III": 0, "iv": 0, "v": 0, "VI": 0
        },  

    # Relative Major Chord (VI)
    "VI": {
        # Primary
        "I": 0, "ii": 60, "iii": 0, "IV": 60, "V": 0, "vi": 0, "viiø7": 0,
        # Sevenths
        "I7": 0, "ii7": 2, "iii7": 0, "IV7": 0, "V7": 0, "vi7": 0,
        # Parallel/Relative
        "i": 0, "II": 0, "III": 0, "iv": 0, "v": 0, "VI": 0
        },

#Seventh Chords Major

    # Seventh (I7)
    "I7": {
        # Primary
        "I": 60, "ii": 60, "iii": 60, "IV": 60, "V": 60, "vi": 60, "viiø7": 0,
        # Sevenths
        "I7": 2, "ii7": 4, "iii7": 0, "IV7": 0, "V7": 4, "vi7": 0,
        # Parallel/Relative
        "i": 0, "II": 0, "III": 0, "iv": 0, "v": 0, "VI": 0
        },

    # Seventh (ii7)
    "ii7": {
        # Primary
        "I": 3, "ii": 0, "iii": 0, "IV": 0, "V": 60, "vi": 0, "viiø7": 0,
        # Sevenths
        "I7": 0, "ii7": 0, "iii7": 0, "IV7": 2, "V7": 0, "vi7": 0,
        # Parallel/Relative
        "i": 0, "II": 0, "III": 0, "iv": 0, "v": 0, "VI": 0
        },

    # Seventh (V7)
    "V7": {
        # Primary
        "I": 60, "ii": 0, "iii": 0, "IV": 60, "V": 0, "vi": 60, "viiø7": 0,
        # Sevenths
        "I7": 0, "ii7": 0, "iii7": 0, "IV7": 2, "V7": 3, "vi7": 0,
        # Parallel/Relative
        "i": 0, "II": 0, "III": 0, "iv": 0, "v": 0, "VI": 0
        },

    # Seventh (vii°7)
    "vii°7": {
        # Primary
        "I": 60, "ii": 0, "iii": 0, "IV": 0, "V": 0, "vi": 60, "viiø7": 0,
        # Sevenths
        "I7": 0, "ii7": 0, "iii7": 0, "IV7": 0, "V7": 0, "vi7": 0,
        # Parallel/Relative
        "i": 0, "II": 0, "III": 0, "iv": 0, "v": 0, "VI": 0
        },
    
#Ending Chords Major

    #End_I - Resolve Chords Starting First
    "end_I": {
        # Primary
        "I": 0, "ii": 15, "iii": 15, "IV": 15, "V": 60, "vi": 15, "viiø7": 0,
        # Sevenths
        "I7": 0, "ii7": 0, "iii7": 0, "IV7": 1, "V7": 0, "vi7": 0,
        # Parallel/Relative
        "i": 0, "II": 0, "III": 0, "iv": 0, "v": 0, "VI": 0
        },

    #End_other - Resolve Chords Starting Anything Else
    "end_other": {
        # Primary
        "I": 60, "ii": 0, "iii": 0, "IV": 15, "V": 15, "vi": 0, "viiø7": 0,
        # Sevenths
        "I7": 0, "ii7": 0, "iii7": 0, "IV7": 0, "V7": 2, "vi7": 0,
        # Parallel/Relative
        "i": 0, "II": 0, "III": 0, "iv": 0, "v": 0, "VI": 0
        },
}

MINOR_CHAIN = {
    
#Starting Chords

    # Start
    "start": {
        # Primary
        "i": 60, "ii°": 0, "III": 0, "iv": 5, "v": 5, "VI": 0, "VII": 0,
        # Sevenths
        "i7": 0, "iiø7": 0, "III7": 0, "iv7": 0, "V7": 0, "VII7": 0,
        # Parallel/Relative
        "I": 0, "II": 0, "iii": 0, "IV": 0, "V": 0, "vi": 0, "viiø7": 0
        },

#Regular Tones Minor

    # Tonic (i)
    "i": {
        # Primary
        "i": 60, "ii°": 0, "III": 60, "iv": 60, "v": 60, "VI": 60, "VII": 60,
        # Sevenths
        "i7": 0, "iiø7": 0, "III7": 0, "iv7": 0, "V7": 2, "VII7": 0,
        # Parallel/Relative
        "I": 0, "II": 0, "iii": 0, "IV": 0, "V": 0, "vi": 0, "viiø7": 0
        },

    # Super Tonic (ii°)
    "ii°": {
        # Primary
        "i": 5, "ii°": 0, "III": 0, "iv": 0, "v": 60, "VI": 0, "VII": 60,
        # Sevenths
        "i7": 0, "iiø7": 0, "III7": 0, "iv7": 0, "V7": 2, "VII7": 0,
        # Parallel/Relative
        "I": 0, "II": 0, "iii": 0, "IV": 0, "V": 0, "vi": 0, "viiø7": 0
        },

    # Mediant (III)
    "III": {
        # Primary
        "i": 0, "ii°": 0, "III": 0, "iv": 60, "v": 0, "VI": 60, "VII": 0,
        # Sevenths
        "i7": 0, "iiø7": 0, "III7": 0, "iv7": 0, "V7": 2, "VII7": 0,
        # Parallel/Relative
        "I": 0, "II": 0, "iii": 0, "IV": 0, "V": 0, "vi": 0, "viiø7": 0
        },

    # Subdominant (iv)
    "iv": {
        # Primary
        "i": 3, "ii°": 0, "III": 0, "iv": 0, "v": 60, "VI": 0, "VII": 60,
        # Sevenths
        "i7": 0, "iiø7": 0, "III7": 0, "iv7": 0, "V7": 2, "VII7": 0,
        # Parallel/Relative
        "I": 0, "II": 0, "iii": 0, "IV": 0, "V": 0, "vi": 0, "viiø7": 0
        },

    # Dominant (v)
    "v": {
        # Primary
        "i": 60, "ii°": 0, "III": 0, "iv": 0, "v": 0, "VI": 60, "VII": 0,
        # Sevenths
        "i7": 0, "iiø7": 0, "III7": 0, "iv7": 0, "V7": 2, "VII7": 0,
        # Parallel/Relative
        "I": 0, "II": 0, "iii": 0, "IV": 0, "V": 0, "vi": 0, "viiø7": 0
        },

    # Submediant (VI)
    "VI": {
        # Primary
        "i": 0, "ii°": 0, "III": 60, "iv": 60, "v": 0, "VI": 0, "VII": 0,
        # Sevenths
        "i7": 0, "iiø7": 0, "III7": 0, "iv7": 0, "V7": 0, "VII7": 0,
        # Parallel/Relative
        "I": 0, "II": 0, "iii": 0, "IV": 0, "V": 0, "vi": 0, "viiø7": 0
        },

    # Leading Tone (VII)  
    "VII": {
        # Primary
        "i": 0, "ii°": 0, "III": 60, "iv": 0, "v": 0, "VI": 0, "VII": 0,
        # Sevenths
        "i7": 0, "iiø7": 0, "III7": 0, "iv7": 0, "V7": 0, "VII7": 0,
        # Parallel/Relative
        "I": 0, "II": 0, "iii": 0, "IV": 0, "V": 0, "vi": 0, "viiø7": 0
        },

# Irregular Tones Minor

    # Relative Minor Chord (II)
    "II": {
        # Primary
        "i": 5, "ii°": 0, "III": 0, "iv": 0, "v": 60, "VI": 0, "VII": 60,
        # Sevenths
        "i7": 0, "iiø7": 0, "III7": 0, "iv7": 0, "V7": 2, "VII7": 0,
        # Parallel/Relative
        "I": 0, "II": 0, "iii": 0, "IV": 0, "V": 0, "vi": 0, "viiø7": 0
        },

    # Relative Minor Chord (iii)
    "iii": {
        # Primary
        "i": 0, "ii°": 0, "III": 0, "iv": 60, "v": 0, "VI": 60, "VII": 0,
        # Sevenths
        "i7": 0, "iiø7": 0, "III7": 0, "iv7": 0, "V7": 2, "VII7": 0,
        # Parallel/Relative
        "I": 0, "II": 0, "iii": 0, "IV": 0, "V": 0, "vi": 0, "viiø7": 0
        },

    # Parallel Major Chord (IV)
    "IV": {
        # Primary
        "i": 3, "ii°": 0, "III": 0, "iv": 0, "v": 60, "VI": 0, "VII": 60,
        # Sevenths
        "i7": 0, "iiø7": 0, "III7": 0, "iv7": 0, "V7": 2, "VII7": 0,
        # Parallel/Relative
        "I": 0, "II": 0, "iii": 0, "IV": 0, "V": 0, "vi": 0, "viiø7": 0
        },

    # Parallel Major Chord (V)  
    "V": {
        # Primary
        "i": 60, "ii°": 0, "III": 0, "iv": 0, "v": 0, "VI": 60, "VII": 0,
        # Sevenths
        "i7": 0, "iiø7": 0, "III7": 0, "iv7": 0, "V7": 2, "VII7": 0,
        # Parallel/Relative
        "I": 0, "II": 0, "iii": 0, "IV": 0, "V": 0, "vi": 0, "viiø7": 0
        },
    
    # Relative Minor Chord (vi) 
    "vi": {
        # Primary
        "i": 0, "ii°": 0, "III": 60, "iv": 0, "v": 0, "VI": 0, "VII": 0,
        # Sevenths
        "i7": 0, "iiø7": 0, "III7": 0, "iv7": 0, "V7": 0, "VII7": 0,
        # Parallel/Relative
        "I": 0, "II": 0, "iii": 0, "IV": 0, "V": 0, "vi": 0, "viiø7": 0
        },

    # Relative Minor Chord (viiø7)
    "VII": {
        # Primary
        "i": 0, "ii°": 0, "III": 60, "iv": 0, "v": 0, "VI": 0, "VII": 0,
        # Sevenths
        "i7": 0, "iiø7": 0, "III7": 0, "iv7": 0, "V7": 0, "VII7": 0,
        # Parallel/Relative
        "I": 0, "II": 0, "iii": 0, "IV": 0, "V": 0, "vi": 0, "viiø7": 0
        },

# Seventh Chords Minor

    # Seventh (ii)
    "iiø7": {
        # Primary
        "i": 0, "ii°": 0, "III": 0, "iv": 0, "v": 16, "VI": 16, "VII": 0,
        # Sevenths
        "i7": 0, "iiø7": 0, "III7": 0, "iv7": 0, "V7": 0, "VII7": 0,
        # Parallel/Relative
        "I": 0, "II": 0, "iii": 0, "IV": 0, "V": 0, "vi": 0, "viiø7": 0
        },

    # Seventh (v)
    "V7": {
        # Primary
        "i": 16, "ii°": 0, "III": 0, "iv": 0, "v": 0, "VI": 16, "VII": 0,
        # Sevenths
        "i7": 0, "iiø7": 0, "III7": 0, "iv7": 0, "V7": 0, "VII7": 0,
        # Parallel/Relative
        "I": 0, "II": 0, "iii": 0, "IV": 0, "V": 0, "vi": 0, "viiø7": 0
        },

    # Seventh (vii)
    "vii°7": {
        # Primary
        "i": 0, "ii°": 0, "III": 16, "iv": 0, "v": 0, "VI": 0, "VII": 0,
        # Sevenths
        "i7": 0, "iiø7": 0, "III7": 0, "iv7": 0, "V7": 0, "VII7": 0,
        # Parallel/Relative
        "I": 0, "II": 0, "iii": 0, "IV": 0, "V": 0, "vi": 0, "viiø7": 0 
       },
    

# Ending Chords Minor

    # Resolve Chords Starting First
    "end_I": {
        # Primary
        "i": 0, "ii°": 0, "III": 0, "iv": 1, "v": 60, "VI": 0, "VII": 0,
        # Sevenths
        "i7": 0, "iiø7": 0, "III7": 0, "iv7": 0, "V7": 0, "VII7": 0,
        # Parallel/Relative
        "I": 0, "II": 0, "iii": 0, "IV": 0, "V": 0, "vi": 0, "viiø7": 0
        },

    # Resolve Chords Starting Any
    "end_other": {
        # Primary
        "i": 60, "ii°": 0, "III": 0, "iv": 0, "v": 1, "VI": 0, "VII": 0,
        # Sevenths
        "i7": 0, "iiø7": 0, "III7": 0, "iv7": 0, "V7": 0, "VII7": 0,
        # Parallel/Relative
        "I": 0, "II": 0, "iii": 0, "IV": 0, "V": 0, "vi": 0, "viiø7": 0
        },
}
