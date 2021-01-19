# Basic sound output.
# bit of a buzz-y square wave. Sounds better at higher frequencies than lower ones.

#Connect a pair of headphones between pin 0 and ground
#You may also need a resistor in series (circa 220 ohms should be ok, but go up to 250-300 if your headphones are low resistance).
#You may be able to get away without a resistor, but don't blame me if you damage your Pico and/or headphones

from machine import Pin
from rp2 import PIO, StateMachine, asm_pio
from time import sleep

max_count = 5000
freq = 1000000

#based on the PWM example.
@asm_pio(sideset_init=PIO.OUT_LOW)
def square_prog():
    label("restart")
    pull(noblock) .side(0)
    mov(x, osr) 
    mov(y, isr)
    
    #start loop
    #here, the pin is low, and it will count down y
    #until y=x, then put the pin high and jump to the next secion
    label("uploop")
    jmp(x_not_y, "skip_up")
    nop()         .side(1)
    jmp("down")
    label("skip_up")
    jmp(y_dec, "uploop")
    
    #mirror the above loop, but with the pin high to form the second
    #half of the square wave
    label("down")
    mov(y, isr)
    label("down_loop")
    jmp(x_not_y, "skip_down")
    nop() .side(0)
    jmp("restart")
    label("skip_down")
    jmp(y_dec, "down_loop")
    
square_sm = StateMachine(0, square_prog, freq=freq, sideset_base=Pin(0))

#pre-load the isr with the value of max_count
square_sm.put(max_count)
square_sm.exec("pull()")
square_sm.exec("mov(isr, osr)")

#note - based on current values of max_count and freq
# this will be slightly out because of the initial mov instructions,
#but that should only have an effect at very high frequencies
def calc_pitch(hertz):
    return int( -1 * (((1000000/hertz) -20000)/4))


notes = [392, 440, 494, 523, 587, 659, 698, 784]

notes_val = []
for note in notes:
    notes_val.append(calc_pitch(note))

'''
note values in Hz
g4 = 392
a4 = 440
b4 = 494
c5 = 523
d5 = 587
e5 = 659
f5 = 698
g5 = 784
'''

#the length of a semi-quaver, the shortest note in the song
note_len = 0.1
pause_len = 0.05

def play_note(note_len, pause_len, val, sm):
    sm.active(1)
    sm.put(val)
    sleep(note_len)
    sm.active(0)
    sleep(pause_len)

while True: 
    play_note(note_len*2, pause_len, notes_val[0], square_sm)
    play_note(note_len, pause_len, notes_val[0], square_sm)
    play_note(note_len*4, pause_len, notes_val[1], square_sm)
    play_note(note_len*4, pause_len, notes_val[0], square_sm)
    play_note(note_len*4, pause_len, notes_val[3], square_sm)
    play_note(note_len*8, pause_len, notes_val[2], square_sm)

    play_note(note_len*2, pause_len, notes_val[0], square_sm)
    play_note(note_len, pause_len, notes_val[0], square_sm)
    play_note(note_len*4, pause_len, notes_val[1], square_sm)
    play_note(note_len*4, pause_len, notes_val[0], square_sm)
    play_note(note_len*4, pause_len, notes_val[4], square_sm)
    play_note(note_len*8, pause_len, notes_val[3], square_sm)

    play_note(note_len*2, pause_len, notes_val[0], square_sm)
    play_note(note_len, pause_len, notes_val[0], square_sm)
    play_note(note_len*4, pause_len, notes_val[7], square_sm)
    play_note(note_len*4, pause_len, notes_val[5], square_sm)
    play_note(note_len*4, pause_len, notes_val[3], square_sm)
    play_note(note_len*4, pause_len, notes_val[2], square_sm)
    play_note(note_len*4, pause_len, notes_val[1], square_sm)

    play_note(note_len*2, pause_len, notes_val[6], square_sm)
    play_note(note_len, pause_len, notes_val[6], square_sm)
    play_note(note_len*4, pause_len, notes_val[5], square_sm)
    play_note(note_len*4, pause_len, notes_val[3], square_sm)
    play_note(note_len*4, pause_len, notes_val[4], square_sm)
    play_note(note_len*8, pause_len, notes_val[3], square_sm)
    sleep(2)

