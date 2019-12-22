class music_data: 
    a_note = ["Ab","A","A#"]
    b_note = ["Bb","B","B#"]
    c_note = ["Cb","C","C#"]
    d_note = ["Db","D","D#"]
    e_note = ["Eb","E","E#"]
    f_note = ["Fb","F","F#"]
    g_note = ["Gb","G","G#"]
    
    total_notes = [a_note, b_note, c_note, d_note, e_note, f_note, g_note]
    total_intervals = 12

octave = ["a","b","c","d","e","f","g","a","b","c","d","e","f","g"]

print("Please Enter Harmonic Analysis Data.")
sharps = input("Enter the number of sharps.")
flats = input("Enter the number of flats. ")
total_chords = input("Enter the number of chords.")


for _ in range(int(total_chords)):
    print("Enter the notes in the chord. If there isn't a seventh, enter 0. ")
    note_1 = input("1. ")
    note_2 = input("2. ")
    note_3 = input("3. ")
    note_4 = input("4. ")
    
    chord = [note_1, note_2, note_3, note_4]

    if chord[3] == "0":
        chord.pop()



    for i in octave:
        if chord[0] == i:
            num = octave.index(i)
            num = num + 2
            for i in range(3):
                if chord[i] == octave[num]:
                    num = num + 2
                    for i in range(3):
                        if chord[i] == octave[num]:
                            print("The chord is " + chord[0])
        if chord[1] == i:
            num = octave.index(i)
            num = num + 2
            for i in range(3):
                if chord[i] == octave[num]:
                    num = num + 2
                    for i in range(3):
                        if chord[i] == octave[num]:
                            print("The chord is " + chord[1])
        if chord[2] == i:
            num = octave.index(i)
            num = num + 2
            for i in range(3):
                if chord[i] == octave[num]:
                    num = num + 2
                    for i in range(3):
                        if chord[i] == octave[num]:
                            print("The chord is " + chord[2])
        try:
            if chord[3] == i:
                num = octave.index(i)
                num = num + 2
                for i in range(3):
                    if chord[i] == octave[num]:
                        num = num + 2
                        for i in range(3):
                            if chord[i] == octave[num]:
                                print("The chord is " + chord[3])
        except:
            continue