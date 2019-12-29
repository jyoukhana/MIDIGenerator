#MIDI Generator

from midiutil import MIDIFile
import random


# midiNotes = {"C0":0, "C1":12, "C2":24, "C3":36, "C4":48, "C5":60, "C6":72, "C7":84, "C8":96, "C9":108, "C10":120,
# "C#0":1, "C#1":13, "C#2":25, "C#3":37, "C#4":49, "C#5":61, "C#6":73, "C#7":85, "C#8":97, "C#9":109, "C#10":121,
# "D0":2, "D1":14, "D2":26, "D3":38, "D4":50, "D5":62, "D6":74, "D7":86, "D8":98, "D9":110, "D10":122,
# "D#0":3, "D#1":15, "D#2":27, "D#3":39, "D#4":51, "D#5":63, "D#6":75, "D#7":87, "D#8":99, "D#9":111, "D#10":123,
# "E0":4, "E1":16, "E2":28, "E3":40, "E4":52, "E5":64, "E6":76, "E7":88, "E8":100, "E9":112, "E10":124,
# "F0":5, "F1":17, "F2":29, "F3":41, "F4":53, "F5":65, "F6":77, "F7":89, "F8":101, "F9":113, "F10":125,
# "F#0":6, "F#1":18, "F#2":30, "F#3":42, "F#4":54, "F#5":66, "F#6":78, "F#7":90, "F#8":102, "F#9":114, "F#10":126,
# "G0":7, "G1":19, "G2":31, "G3":43, "G4":55, "G5":67, "G6":79, "G7":91, "G8":103, "G9":115, "G10":127,
# "G#0":8, "G#1":20, "G#2":32, "G#3":44, "G#4":56, "G#5":68, "G#6":80, "G#7":92, "G#8":104, "G#9":116,
# "A0":9, "A1":21, "A2":33, "A3":45, "A4":57, "A5":69, "A6":81, "A7":93, "A8":105, "A9":117,
# "A#0":10, "A#1":22, "A#2":34, "A#3":46, "A#4":58, "A#5":70, "A#6":82, "A#7":94, "A#8":106, "A#9":118,
# "B0":11, "B1":23, "B2":35, "B3":47, "B4":59, "B5":71, "B6":83, "B7":95, "B8":107, "B9":119}

#Dictionary of all main non-sharp root notes at octave 0.
midiNotes = {"C":0, "D":2, "E":4, "F":5, "G":7, "A":9, "B":11}

#Checks if the user has input a sharp note. This is to simplify finding the MIDI note number
def isSharp(root, octave):
    note = root + str(octave)
    if note[1] == "#":
        return True
    else:
        return False

#Function to get the root key as a string and find the midi note
def getRootKey(root, octave):
    note = root + str(octave)
    midiRoot = 12 * octave + midiNotes.get(root[0])

    if isSharp(root, octave):
        midiRoot = int(midiRoot) + 1
    return midiRoot

#Takes the MIDI root note and returns either a major scale or minor scale of the note
def generateScale(midiRoot, minorKey):
    if minorKey == False:
        midiScale = [midiRoot, midiRoot+2, midiRoot+4, midiRoot + 5, midiRoot + 7, midiRoot + 9, midiRoot + 11, midiRoot + 12]
    else:
        midiScale = [midiRoot, midiRoot+2, midiRoot+3, midiRoot + 5, midiRoot + 7, midiRoot + 8, midiRoot + 10, midiRoot + 12]
    return midiScale

#Takes a scale and generates a track using randomly generated notes within that scale
def createMidiTrack(midiScale, length):
    track = [midiScale[0]]
    count = 0
    while (count < length-1):
        count = count + 1
        track.append(midiScale[random.randint(0, len(midiScale)-1)])
    return track

# rootKey = getRootKey("E", 5)
#
# scale = generateScale(rootKey, True)
#
# track = createMidiTrack(scale, 16)
#
# MyMIDI = MIDIFile(1)
#
# MyMIDI.addTempo(0,0,100)
#
# for i, pitch in enumerate(track):
#     MyMIDI.addNote(0, 0, pitch, 0 + i, 1, 100)
#
# with open("testfile.mid", "wb") as output_file:
#     MyMIDI.writeFile(output_file)
