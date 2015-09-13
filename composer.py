# -*- coding: utf-8 -*-

import random
import string
import formula
import music_def as mus

class Key:

    def __init__(self, scale=None, key=None):
        if scale == None:
            self.scale = self.generate_scale()
        else:
            self.scale = scale
        if key == None:
            self.key = self.generate_key()
        else:
            self.key = key
    
    def generate_scale(self):
        return random.choice(formula.SCALE_FREQ)
    
    def generate_key(self):
        if self.scale == "major":
            key = random.choice(mus.MAJOR_KEYS)
        elif self.scale == "minor":
            key = random.choice(mus.MINOR_KEYS)
        else:
            return None
        return key
    
    def get_type(self):
        if self.scale == "major":
            type = mus.KEY_TYPE_MAJOR[self.key]
        elif self.scale == "minor":
            type = mus.KEY_TYPE_MINOR[self.key]
        else:
            return None
        return type

    def modulate_key(self, semitones, change_scale=False):
        if self.scale == "major":
            index = mus.MAJOR_KEYS.index(self.key)
            if change_scale == False:
                keys = mus.MAJOR_KEYS
                new_scale = "major"
            else:
                keys = mus.MINOR_KEYS
                new_scale = "minor"
        elif self.scale == "minor":
            index = mus.MINOR_KEYS.index(self.key)
            if change_scale == False:
                keys = mus.MINOR_KEYS
                new_scale = "minor"
            else:
                keys = mus.MAJOR_KEYS
                new_scale = "major"
        else:
            return None
        index = (index + semitones) % 12
        new_key = keys[index]
        return Key(new_scale, new_key)
    
    def generate_modulation(self):
        mod_type = random.choice(formula.MODULATION_FREQ)
        if mod_type == "relative" and self.scale == "major":
            mod_type = "relative_minor"
        elif mod_type == "relative" and self.scale == "minor":
            mod_type = "relative_major"
        return self.modulate_key(
                mus.MODULATION_DESC[mod_type]["semitones"],
                mus.MODULATION_DESC[mod_type]["change_scale"]
                )
    
    def get_chord_note(self, chord):
        interval = mus.CHORD_DETAILS[chord]["interval"]
        if self.scale == "major":
            semitones = sum(mus.MAJOR_SCALE_INTERVALS[:interval])
        elif self.scale == "minor":
            semitones = sum(mus.MINOR_SCALE_INTERVALS[:interval])
        else:
            return None

        type = self.get_type()
        if type in ["sharp" ,"none"]:
            notes = mus.NOTES_SHARP
        elif type == "flat":
            notes = mus.NOTES_FLAT
        else:
            return None

        index = notes.index(self.key)
        note = notes[(index + semitones) % 12]
        return note

    def get_chord_type(self, chord):
        return mus.CHORD_DETAILS[chord]["type"]

    def get_chord(self, chord):
        return self.get_chord_note(chord) + self.get_chord_type(chord)

    def __str__(self):
        return "{0} {1}".format(self.key, self.scale)


class Progression:

    def __init__(self, scale):
        bars = self.generate_number_of_bars()
        self.chords_per_bar = self.generate_chords_per_bar(bars)
        if scale == "major":
            chain = formula.MAJOR_CHAIN
        elif scale == "minor":
            chain = formula.MINOR_CHAIN
        # TODO else?
        progression = self.generate_progression(chain, sum(self.chords_per_bar))
        self.progression = self.group_progression_into_bars(progression)
    
    def generate_number_of_bars(self):
        return random.choice(formula.NUM_BARS_FREQ)

    def generate_chords_per_bar(self, number_of_bars):
        chord_list = []
        for i in xrange(number_of_bars):
            chord_list.append(
                random.choice(formula.CHORDS_PER_BAR_FREQ))
        return chord_list

    def generate_progression(self, chain, length):
        progression = []
        prev = "start"
        for i in xrange(length):
            try:
                if i == length - 1 and len(progression) > 0:
                    if progression[0] in ["I", "i"]:
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

    def group_progression_into_bars(self, progression):
        grouped_progression = []
        i = 0
        for chords in self.chords_per_bar:
            grouped_progression.append(progression[i:chords + i])
            i += chords
        return grouped_progression

    def get_num_of_bars(self):
        return len(self.progression)

    def __str__(self):
        bars = [" ".join(bar) for bar in self.progression]
        return "║: {0} :║".format(" | ".join(bars))

class Section:

    def __init__(self, name, song_key, song_time_sig, song_bpm):
        self.name = name
        self.time_signature = song_time_sig
        self.bpm = song_bpm
        self.key = song_key.generate_modulation()
        self.progression = Progression(self.key.scale)
        self.repeats = self.generate_repeats(len(self.progression.progression))

    def generate_repeats(self, bars_per_progression):
        repeat_base = random.choice(formula.REPEAT_BASE_FREQ)

        if 54 <= self.bpm < 84:
            repeat_modifier = random.choice(formula.REPEAT_SLOW_MOD_FREQ)
        elif 84 <= self.bpm < 100:
            repeat_modifier = random.choice(formula.REPEAT_MODERATE_SLOW_MOD_FREQ)
        elif 100 <= self.bpm < 116:
            repeat_modifier = random.choice(formula.REPEAT_MODERATE_MOD_FREQ)
        elif 116 <= self.bpm < 141:
            repeat_modifier = random.choice(formula.REPEAT_FAST_MOD_FREQ)
        else:
            repeat_modifier = 0

        repeats = (repeat_base + repeat_modifier) / bars_per_progression  
        if repeats == 0:
            return 1
        else:
            return repeats

    def get_progression_in_key(self):
        return [[self.key.get_chord(c) for c in bar] for bar in self.progression.progression]

    def get_seconds(self):
        beats = self.progression.get_num_of_bars() * self.time_signature * self.repeats
        seconds = round((beats * 60) / float(self.bpm))
        return seconds

    def __str__(self):
        bars = [" ".join(bar) for bar in self.get_progression_in_key()]
        return "{0}: ({1}) ║: {2} :║ x {3}".format(self.name, self.key, " | ".join(bars), self.repeats)


class Song:

    def __init__(self):
        self.time_signature = self.generate_time_signature()
        self.bpm = self.generate_bpm()
        self.key = Key()
        length = self.generate_number_of_sections()
        self.structure = self.generate_structure(length)

        self.sections = {}
        for i in range(self.get_structure_depth()):
            letter = (list(string.ascii_uppercase)[i])
            self.sections[letter] = Section(letter, self.key, self.time_signature, self.bpm)
        self.overall_sections = [self.sections[letter] for letter in self.structure]

    ## Time ##

    def generate_time_signature(self):
        return random.choice(formula.TIME_SIG_FREQ) # assumed to be in quarter notes
    
    def generate_bpm(self):
        return int(random.triangular(*formula.BPM_TRIANGLE))
    
    def get_tempo(self):
        if 54 <= self.bpm < 65:
            return "Adagio"
        elif 65 <= self.bpm < 75:
            return "Adagietto"
        elif 75 <= self.bpm < 84:
            return "Andantino"
        elif 84 <= self.bpm < 90:
            return "Andante"
        elif 90 <= self.bpm < 100:
            return "Andante Moderato"
        elif 100 <= self.bpm < 112:
            return "Moderato"
        elif 112 <= self.bpm < 116:
            return "Allegro Moderato"
        elif 116 <= self.bpm < 141:
            return "Allegro"
        else:
            return None

    def get_tempo_desc(self):
        return "{0} bpm: {1}".format(self.bpm, self.get_tempo())

    ## Structure ##

    def generate_number_of_sections(self):
        return random.choice(formula.NUM_SECTIONS_FREQ)

    def generate_structure(self, length):
        chain = formula.STRUCTURE_CHAIN
        structure = []
        depth = 1
        prev = "A"
        structure.append(prev)
        for i in range(length):
            try:
                choice = random.randint(1, sum(chain[prev].values()[:depth + 1]))
                cumulative = 0
                for item, chance in sorted(chain[prev].items()):
                    cumulative += chance
                    if choice <= cumulative:
                        if sorted(chain[prev]).index(item) == depth:
                            depth += 1
                        structure.append(item)
                        prev = item
                        break
            except KeyError:
                print "KEYERROR: STRUCTURE"
                break
        return structure
    
    def get_structure_depth(self):
        depth = 0
        for letter in list(string.ascii_uppercase):
            if letter in self.structure:
                depth += 1
            else:
                break
        return depth

    def get_duration(self):
        total_seconds = 0
        for sect in self.overall_sections:
            total_seconds += sect.get_seconds()
        seconds = int(round(total_seconds)) % 60
        minutes = int(round(total_seconds)) / 60
        return "{:0>2d}:{:0>2d}".format(minutes, seconds)

    def __str__(self):
        string = str(self.key) + "\n" + self.get_tempo_desc()
        for sect in self.overall_sections:
            string += "\n" + str(sect)
        string += "\n" + self.get_duration()
        return string


if __name__ == "__main__":
    song = Song()
    print song
