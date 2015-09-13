# -*- coding: utf-8 -*-

MAJOR_SCALE_INTERVALS = [ 0, 2, 2, 1, 2, 2, 2, 1 ]
MINOR_SCALE_INTERVALS = [ 0, 2, 1, 2, 2, 1, 2, 2 ]

MAJOR_KEYS = [ "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab" ]
MINOR_KEYS = [ "A", "Bb", "B", "C", "C#", "D", "Eb", "E", "F", "F#", "G", "G#" ]

KEY_TYPE_MAJOR = {
"A": "sharp",
"Bb": "flat",
"B": "sharp",
"C": "none",
"Db": "flat",
"D": "sharp",
"Eb": "flat",
"E": "sharp",
"F": "flat",
"Gb": "flat",
"G": "sharp",
"Ab": "flat"
}
KEY_TYPE_MINOR = {
"A": "none",
"Bb": "flat",
"B": "sharp",
"C": "flat",
"C#": "sharp",
"D": "flat", 
"Eb": "flat",
"E": "sharp",
"F": "flat",
"F#": "sharp",
"G": "flat",
"G#": "sharp"
}

NOTES_SHARP = [ "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#" ]
NOTES_FLAT =  [ "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab" ]

CHORD_DETAILS = {
"I": {"interval": 1, "type": ""},
"i": {"interval": 1, "type": "m"},
"I7": {"interval": 1, "type": "M7"},
"i7": {"interval": 1, "type": "m7"},
"II": {"interval": 2, "type": ""},
"ii": {"interval": 2, "type": "m"},
"ii7": {"interval": 2, "type": "m7"},
"ii°": {"interval": 2, "type": "°"},
"iiø7": {"interval": 2, "type": "ø7"},
"III": {"interval": 3, "type": ""},
"iii": {"interval": 3, "type": "m"},
"III7": {"interval": 3, "type": "M7"},
"iii7": {"interval": 3, "type": "m7"},
"IV": {"interval": 4, "type": ""},
"iv": {"interval": 4, "type": "m"},
"IV7": {"interval": 4, "type": "M7"},
"iv7": {"interval": 4, "type": "m7"},
"V": {"interval": 5, "type": ""},
"v": {"interval": 5, "type": "m"},
"V7": {"interval": 5, "type": "7"},
"VI": {"interval": 6, "type": ""},
"vi": {"interval": 6, "type": "m"},
"VI7": {"interval": 6, "type": "M7"},
"vi7": {"interval": 6, "type": "m7"},
"VII": {"interval": 7, "type": ""},
"vii": {"interval": 7, "type": "m"},
"vii°": {"interval": 7, "type": "°"},
"vii°7": {"interval": 7, "type": "°7"},
"viiø7": {"interval": 7, "type": "ø7"}
}

MODULATION_DESC = {
"none": {"semitones": 0, "change_scale": False},
"parallel": {"semitones": 0, "change_scale": True},
"relative_major": {"semitones": 3, "change_scale": True},
"relative_minor": {"semitones": -3, "change_scale": True},
"neighbour_up": {"semitones": 7, "change_scale": False},
"neighbour_down": {"semitones": -7, "change_scale": False}
}