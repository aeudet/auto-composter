import random
import string
import copy

#### Major/Minor ####

scale = random.choice(["major", "minor"])

#### Key Section ####

if scale == "major":
	key = random.choice(["C Major", "G Major", "D Major", "A Major", "E Major", "B Major", "F# Major", "Db Major", "Ab Major", "Eb Major", "Bb Major", "F Major"])
elif scale == "minor":
	key = random.choice(["A Minor", "E Minor", "B Minor", "F# Minor", "C# Minor", "G# Minor", "Eb Minor", "Bb Minor", "F Minor", "C Minor", "G Minor", "D Minor"])

#### Tempo Section ####

#bpm = random.choice(range(54,141)) # Chosen bpm
bpm = int(random.triangular(54,141,120)) # Chosen bpm
	
if bpm >= 54 and bpm < 65:
	tempo = "Adagio"
elif bpm >= 65 and bpm < 75:
	tempo = "Adagietto"
elif bpm >=75 and bpm < 84:
	tempo = "Andantino"
elif bpm >=84 and bpm < 90:
	tempo = "Andante"
elif bpm >=90 and bpm < 100:
	tempo = "Andante Moderato"
elif bpm >=100 and bpm < 112:
	tempo = "Moderato"
elif bpm >=112 and bpm < 116:
	tempo = "Allegro Moderato"
elif bpm >=116 and bpm < 141:
	tempo = "Allegro"
else:
	tempo = "Error"


#### Song Chords ####

# Generates length of progression
def generate_progression_length():
	return random.choice([1] * 3 + [2] * 25 + [4] * 59 + [8] * 4)

# Generates list of chords per bar for a number_of_bars
def generate_chords_per_bar(number_of_bars):
	chord_list = []
	for i in xrange(number_of_bars):
		chord_list.append(random.choice([1] * 84 + [2] * 19 + [3] * 2 + [4] * 1))
	return chord_list


chord_chain_major = {
	"start": {"I":4, "IV":1, "V":1},
	"I": {"I": 1, "ii": 1, "iii": 1, "IV": 1, "V": 1, "vi": 1, "vii": 0},
	"ii": {"V": 1, "vii": 0},
	"iii": {"vi": 1, "IV": 1, "ii": 1},
	"IV": {"V": 1, "vii": 0},
	"V": {"I": 1, "vi": 1},
	"vi": {"ii": 1, "IV": 1},
	#"vii": {"I": 1, "vi": 1}
}

chord_chain_minor = {
	"start": {"i":4, "iv":1, "v":1},
	"i": {"i": 1, "ii": 0, "III": 1, "iv": 1, "v": 1, "VI": 1, "VII": 1},
	#"ii": {"v": 1, "VII": 1},
	"III": {"VI": 1, "iv": 1, "ii": 0},
	"iv": {"ii": 0, "VII": 1, "v": 1, "i": 1},
	"v": {"i": 1, "VI": 1},
	"VI": {"iv": 1, "ii": 0},
	"VII": {"III": 1}
}

def generate_progression(chain, length):
	progression = []
	prev = "start"
	for i in xrange(length):
		try:
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

total_sections = random.choice(range(2,7))

chain = {
	"A": {"A": 1, "B": 4, "C": 4, "D": 4, "E": 3, "F": 3},
	"B": {"A": 4, "B": 1, "C": 4, "D": 3, "E": 3, "F": 3},
	"C": {"A": 4, "B": 4, "C": 1, "D": 4, "E": 3, "F": 3},
	"D": {"A": 2, "B": 2, "C": 2, "D": 1, "E": 4, "F": 3},
	"E": {"A": 3, "B": 3, "C": 3, "D": 3, "E": 1, "F": 4},
	"F": {"A": 3, "B": 3, "C": 3, "D": 3, "E": 3, "F": 1},
	"G": {"A": 1, "B": 1, "C": 1, "D": 1, "E": 1, "F": 1}
}

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

#### Repeat Number ####
	
def generate_repeats(bars_per_progression):
	repeat_base = random.choice([2] * 3 + [4] * 18 + [8] * 29 + [12] * 33 + [16] * 28 + [24] * 4)
	#repeat_modifier_low = random.choice([12] * 11 + [16] * 20 + [18] * 12 + [24] * 6 + [32] * 2)
	#repeat_modifier_hi = random.choice([2] * 10 + [4] * 15 + [8] * 18 + [12] * 5)
	#if bars_per_progression >= 1 and bars_per_progression < 4:
	#	return repeats + repeat_modifier_low
	#elif bars_per_progression >= 4 and bars_per_progression <= 8:
	#	return repeats + repeat_modifier_hi
	if bpm >= 54 and bpm < 84:
		repeat_modifier = random.choice([0] + [2])
	elif bpm >= 84 and bpm < 100:
		repeat_modifier = random.choice([4] + [6])
	elif bpm >= 100 and bpm < 116:
		repeat_modifier = random.choice([6] + [8])
	elif bpm >= 116 and bpm < 141:
		repeat_modifier = random.choice([8] + [10] + [12])
	repeats = (repeat_base + repeat_modifier)/bars_per_progression	
	if repeats == 0:
		return 1
	else:
		return repeats

#### Output ####

chords_per_bar = []
progression_lengths = []
progressions = []
for i in xrange(7):
	progression_lengths.append(generate_progression_length())
	chords_per_bar.append(generate_chords_per_bar(progression_lengths[-1]))
	progressions.append(generate_progression(chord_chain_major if scale == "major" else chord_chain_minor, sum(chords_per_bar[-1])))

progressions_with_bars = copy.deepcopy(progressions)
for i in xrange(7):
	cumulative = 0
	for bar in xrange(progression_lengths[i]):
		cumulative += chords_per_bar[i][bar]
		progressions_with_bars[i].insert(cumulative, "|")
		cumulative += 1

overall_structure = generate_structure(chain, "A", total_sections)

overall_structure_repeats = []
overall_structure_progressions = []
# same as above
alphabet = list(string.ascii_uppercase)
for section in overall_structure:
	for i in xrange(7):
		if section == alphabet[i]:
			overall_structure_progressions.append(progressions_with_bars[i])
			overall_structure_repeats.append(generate_repeats(len(chords_per_bar[i])))
			break

# Display key
print key
# Display tempo
print tempo + ": " + str(bpm) + " bpm"

for i in xrange(7):
	print alphabet[i] + ": | " + " ".join(progressions_with_bars[i])

print overall_structure
for i in xrange(len(overall_structure)):
	print overall_structure[i] + ": | " + " ".join(overall_structure_progressions[i]) + " x " + str(overall_structure_repeats[i])
	
# Display total time
time = 0
for section in xrange(len(overall_structure)):
	for progression in xrange(7):
		if overall_structure[section] == alphabet[progression]:
			time += progression_lengths[progression] * overall_structure_repeats[section]
			break
time = (time * 4) / float(bpm)
print str(round(time, 2)) + " minutes"
