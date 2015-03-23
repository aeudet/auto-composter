# -*- coding: utf-8 -*-

import random
import string
import copy

#### Major/Minor ####

def generate_scale():
	return random.choice(["major"] * 6 + ["minor"] * 1)


#### Time Signature ####

def generate_time_signature():
	return random.choice([4])


#### Key Section ####

MAJOR_SCALE_INTERVAL = [2, 2, 1, 2, 2, 2, 1]
MINOR_SCALE_INTERVAL = [2, 1, 2, 2, 1, 2, 2]

MAJOR_KEYS = [
	"A Major", "Bb Major", "B Major", "C Major", "Db Major", "D Major", 
	"Eb Major", "E Major", "F Major", "F# Major", "G Major", "Ab Major"
	]

MINOR_KEYS = [
	"A Minor", "Bb Minor", "B Minor", "C Minor", "C# Minor", "D Minor", 
	"Eb Minor", "E Minor", "F Minor", "F# Minor", "G Minor", "G# Minor"
	]

def generate_key(scale):
	if scale == "major":
		return random.choice(MAJOR_KEYS)
	elif scale == "minor":
		return random.choice(MINOR_KEYS)


#### Tempo Section ####

def generate_bpm():
	return int(random.triangular(54, 141, 120))

def get_tempo(bpm):
	if bpm >= 54 and bpm < 65:
		return "Adagio"
	elif bpm >= 65 and bpm < 75:
		return "Adagietto"
	elif bpm >=75 and bpm < 84:
		return "Andantino"
	elif bpm >=84 and bpm < 90:
		return "Andante"
	elif bpm >=90 and bpm < 100:
		return "Andante Moderato"
	elif bpm >=100 and bpm < 112:
		return "Moderato"
	elif bpm >=112 and bpm < 116:
		return "Allegro Moderato"
	elif bpm >=116 and bpm < 141:
		return "Allegro"
	else:
		return "Error"

#### Song Chords ####

# Generates length of progression
def generate_progression_length():
	return random.choice([1] * 3 + [2] * 15 + [4] * 59 + [8] * 6)


def generate_section_length():
	return random.choice(range(2, 7))

# Generates list of chords per bar for a number_of_bars
def generate_chords_per_bar(number_of_bars):
	chord_list = []
	for i in xrange(number_of_bars):
		chord_list.append(
			random.choice([1] * 84 + [2] * 19 + [3] * 2 + [4] * 1))
	return chord_list

CHORD_CHAIN_MAJOR = {
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

CHORD_CHAIN_MINOR = {
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

# Generates a chord progression of specified length
def generate_progression(chain, length):
	progression = []
	prev = "start"
	for i in xrange(length):
		try:
			if i == length - 1 and len(progression) > 0:
				if progression[0] == "I" or progression[0] == "i":
					prev = "end_I"
				else:
					prev = "end_other"
			choice = random.randint(1, sum(chain[prev].values()))
			cumulative = 0
			for item, chance in sorted(chain[prev].items()):
				cumulative += chance
				if choice <= cumulative:
					progression.append(item)
					prev =  item
					break
		except KeyError:
			print "KEYERROR: CHORD"
			break
	return progression

#### Song Structure ####

STRUCTURE_CHAIN = {
	"A": {"A": 1, "B": 6, "C": 6, "D": 5, "E": 3, "F": 3, "G": 3},
	"B": {"A": 6, "B": 1, "C": 3, "D": 5, "E": 3, "F": 3, "G": 3},
	"C": {"A": 6, "B": 4, "C": 1, "D": 4, "E": 3, "F": 3, "G": 3},
	"D": {"A": 2, "B": 2, "C": 2, "D": 1, "E": 6, "F": 3, "G": 3},
	"E": {"A": 4, "B": 2, "C": 4, "D": 4, "E": 1, "F": 4, "G": 3},
	"F": {"A": 3, "B": 3, "C": 3, "D": 3, "E": 3, "F": 1, "G": 3},
	"G": {"A": 1, "B": 1, "C": 1, "D": 1, "E": 1, "F": 1, "G": 1}
}

# Generates a song structure of specified length
def generate_structure(chain, start, length):
	structure = []
	depth = 1
	prev = start[-1:]
	structure.append(start)
	adjusted_length = range(length - 1)
	for i in adjusted_length:
		try:
			choice = random.randint(1, sum(chain[prev].values()))
			cumulative = 0
			for item, chance in sorted(chain[prev].items()):
				cumulative += chance
				if choice <= cumulative:
					if sorted(chain[prev]).index(item) <= depth:
						structure.append(item)
						prev = item
						if sorted(chain[prev]).index(item) == depth:
							depth += 1
					else:
						adjusted_length.append(1)
					break
		except KeyError:
			print "KEYERROR: STRUCTURE"
			break
	return structure

#### Modulation ####

def modulate_key(key, semitones, change_scale=False):
	if "Major" in key:
		index = MAJOR_KEYS.index(key)
		if change_scale == False:
			keys = MAJOR_KEYS
		else:
			keys = MINOR_KEYS
	elif "Minor" in key:
		index = MINOR_KEYS.index(key)
		if change_scale == False:
			keys = MINOR_KEYS
		else:
			keys = MAJOR_KEYS
	else:
		return key
	index = (index + semitones) % 12
	return keys[index]

MODULATION_TYPE = {
	"none": {"semitones": 0, "change_scale": False},
	"parallel": {"semitones": 0, "change_scale": True},
	"relative_major": {"semitones": 3, "change_scale": True},
	"relative_minor": {"semitones": -3, "change_scale": True},
	"neighbour_up": {"semitones": 7, "change_scale": False},
	"neighbour_down": {"semitones": -7, "change_scale": False}
}
MODULATION_LIST = (
	["none"] * 22 +
	["parallel"] * 2 +
	["relative"] * 2 +
	["neighbour_up"] * 2 +
	["neighbour_down"] * 2
	)

def modulate_section(key):
	mod_type = random.choice(MODULATION_LIST)
	if mod_type == "relative" and "Major" in key:
		mod_type = "relative_minor"
	elif mod_type == "relative" and "Minor" in key:
		mod_type = "relative_major"
	return modulate_key(
			key, 
			MODULATION_TYPE[mod_type]["semitones"],
			MODULATION_TYPE[mod_type]["change_scale"]
			)
		
#### Repeat Number ####
	
# Generates the number of times a section is repeated
def generate_repeats(bars_per_progression):
	repeat_base = random.choice(
			[2] * 3 + [4] * 18 + [8] * 29 + [12] * 33 + [16] * 28 + [24] * 4)
	if bpm >= 54 and bpm < 84:
		repeat_modifier = random.choice([0] * 12  + [2] * 12 + [4] * 2 + [8] * 1)
	elif bpm >= 84 and bpm < 100:
		repeat_modifier = random.choice([4] * 12 + [6] * 12 + [8] * 2 + [12] * 1)
	elif bpm >= 100 and bpm < 116:
		repeat_modifier = random.choice([6] * 12 + [8] * 12 + [12] * 1)
	elif bpm >= 116 and bpm < 141:
		repeat_modifier = random.choice(
				[8] * 16 + [10] * 16 + [12] * 16 + [16] * 2 + [20] * 1)
	repeats = (repeat_base + repeat_modifier) / bars_per_progression	
	if repeats == 0:
		return 1
	else:
		return repeats

####

scale = generate_scale()
bpm = generate_bpm()
tempo = get_tempo(bpm)
key = generate_key(scale)

#### Structure ####

# Generate progressions for each potential section
chords_per_bar = []
progression_lengths = []
progressions = []
progression_keys = []
progression_scales = []
for i in xrange(7):
	progression_keys.append(modulate_section(key))
	if "Major" in progression_keys[i]:
		progression_scale = "major"
	elif "Minor" in progression_keys[i]:
		progression_scale = "minor"
	progression_lengths.append(generate_progression_length())
	chords_per_bar.append(generate_chords_per_bar(progression_lengths[-1]))
	progressions.append(
			generate_progression(
				CHORD_CHAIN_MAJOR if progression_scale == "major" else CHORD_CHAIN_MINOR,
				sum(chords_per_bar[-1])))

# Makes a copy of the chord progressions with bar lines inserted
progressions_with_bars = copy.deepcopy(progressions)
for i in xrange(7):
	cumulative = 0
	for bar in xrange(progression_lengths[i] - 1):
		cumulative += chords_per_bar[i][bar]
		progressions_with_bars[i].insert(cumulative, "|")
		cumulative += 1

# Generate overall structure
overall_structure = generate_structure(
		STRUCTURE_CHAIN, "A", generate_section_length())

# Fill in song structure with the appropriate chord progressions and determines section repeats
overall_structure_repeats = []
overall_structure_progressions = []
overall_structure_keys = []
alphabet = list(string.ascii_uppercase)
for section in overall_structure:
	for i in xrange(7):
		if section == alphabet[i]:
			overall_structure_progressions.append(
					progressions_with_bars[i])
			overall_structure_repeats.append(
					generate_repeats(len(chords_per_bar[i])))
			break

#### Output ####

beats_per_bar = generate_time_signature()

# Display key
print key

# Display tempo
print tempo + ": " + str(bpm) + " bpm"

for i in xrange(7):
	print (alphabet[i] + ": (" + progression_keys[i] + ") | " + 
			" ".join(progressions_with_bars[i]))
			

print overall_structure
for i in xrange(len(overall_structure)):
	print (overall_structure[i] + ": "  + "(" + progression_keys[i] + ") " + 
	      "║: " + " ".join(overall_structure_progressions[i]) + " :║ x " +
		  str(overall_structure_repeats[i]))
	
# Display total song duration 
time = 0
for section in xrange(len(overall_structure)):
	for progression in xrange(7):
		if overall_structure[section] == alphabet[progression]:
			time += (progression_lengths[progression] *
			        overall_structure_repeats[section])
			break
time = int(round((time * beats_per_bar * 60) / float(bpm)))
minutes = time / 60
seconds = time % 60
print "{:0>2d}:{:0>2d}".format(minutes, seconds)
