# Basic sound output.
# bit of a buzz-y square wave. Sounds better at higher frequencies than lower ones.

#Connect a pair of headphones between pin 0 and ground
#You may also need a resistor if your headphones are low resistance

import PIOBeep
from time import sleep

beeper = PIOBeep.PIOBeep(0,0)

notes = [392, 440, 494, 523, 587, 659, 698, 784]

notes_val = []
for note in notes:
    notes_val.append(beeper.calc_pitch(note))

#the length of a semi-quaver, the shortest note in the song
note_len = 0.1
pause_len = 0.05


while True: 
    beeper.play_value(note_len*2, pause_len, notes_val[0])
    beeper.play_value(note_len, pause_len, notes_val[0])
    beeper.play_value(note_len*4, pause_len, notes_val[1])
    beeper.play_value(note_len*4, pause_len, notes_val[0])
    beeper.play_value(note_len*4, pause_len, notes_val[3])
    beeper.play_value(note_len*8, pause_len, notes_val[2])

    beeper.play_value(note_len*2, pause_len, notes_val[0])
    beeper.play_value(note_len, pause_len, notes_val[0])
    beeper.play_value(note_len*4, pause_len, notes_val[1])
    beeper.play_value(note_len*4, pause_len, notes_val[0])
    beeper.play_value(note_len*4, pause_len, notes_val[4])
    beeper.play_value(note_len*8, pause_len, notes_val[3])

    beeper.play_value(note_len*2, pause_len, notes_val[0])
    beeper.play_value(note_len, pause_len, notes_val[0])
    beeper.play_value(note_len*4, pause_len, notes_val[7])
    beeper.play_value(note_len*4, pause_len, notes_val[5])
    beeper.play_value(note_len*4, pause_len, notes_val[3])
    beeper.play_value(note_len*4, pause_len, notes_val[2])
    beeper.play_value(note_len*4, pause_len, notes_val[1])

    beeper.play_value(note_len*2, pause_len, notes_val[6])
    beeper.play_value(note_len, pause_len, notes_val[6])
    beeper.play_value(note_len*4, pause_len, notes_val[5])
    beeper.play_value(note_len*4, pause_len, notes_val[3])
    beeper.play_value(note_len*4, pause_len, notes_val[4])
    beeper.play_value(note_len*8, pause_len, notes_val[3])
    sleep(2)
