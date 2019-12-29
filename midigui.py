#GUI For MIDI generator project

from tkinter import *

main = Tk()
main.title("MIDI Generator")
Label(main, text = "Key: ").grid(row = 0)
Label(main, text = "Octave: ").grid(row = 1)
Label(main, text = "Length: ").grid(row = 2)
Label(main, text = "BPM: ").grid(row = 3)
var1 = IntVar()
checkMinor = Checkbutton(main, text = "Minor key?", variable = var1).grid(row = 4, sticky = W)
#checkMinor.Pack()
minorKey = False

if checkMinor == 1:
    minorKey = True

keyEntry = entry(main)
octaveEntry = entry(main)
lengthEntry = entry(main)
bpmEntry = entry(main)

keyEntry.grid(row = 0, column = 1)
octaveEntry.grid(row = 1, column = 1)
lengthEntry.grid(row = 2, column = 1)
bpmEntry.grid(row = 3, column = 1)

button = tk.Button(main, text = "Generate MIDI File", width = 25, command = main.generateFile(str(keyEntry), int(octaveEntry), int(lengthEntry), int(bpmEntry), minorKey))
#button.pack()

def generateFile(root, octave, length, bpm, isMinor):
    rootKey = getRootKey(root, octave)

    scale = generateScale(rootKey, isMinor)

    track = createMidiTrack(scale, length)

    MyMIDI = MIDIFile(1)

    MyMIDI.addTempo(0,0,100)

    for i, pitch in enumerate(track):
        MyMIDI.addNote(0, 0, pitch, 0 + i, 1, 100)

    with open("testfile.mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)

main.mainloop()
