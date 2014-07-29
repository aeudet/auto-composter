import random

# Key Section

maj_key = ["C Major", "G Major", "D Major", "A Major", "E Major", "B Major", "Gb Major", "Db Major", "Ab Major", "Eb Major", "Bb Major", "F Major"]
min_key = ["A Minor", "E Minor", "B Minor", "F# Minor", "C# Minor", "G# Minor", "Eb Minor", "Bb Minor", "C Minor", "F Minor", "G Minor", "D Minor"]

# Tempo Section

bpm = range(55,140) # Range of bpm

#Chords

chord_list = ["I", "ii", "IV", "V", "vi"] # Chords in the chord pool
chord_rand = (random.choice(chord_list)) # Random chord selected from chord pool
chord_num_range = range(3,6) # Range of how many chords per progression
chord_num = (random.choice(chord_num_range)) # Number of chords per prgoression

# Output

print(random.choice(maj_key))
print (random.choice(bpm))
print chord_rand


