  
# Basic sound output.
# bit of a buzz-y square wave. Sounds better at higher frequencies than lower ones.


from machine import Pin
from rp2 import PIO, StateMachine, asm_pio
from time import sleep

max_count = 5000
freq = 1000000


@asm_pio(sideset_init=PIO.OUT_LOW)
def pwm_prog():
    label("restart")
    pull(noblock) .side(0)
    mov(x, osr) 
    mov(y, isr)
    label("pwmloop")
    jmp(x_not_y, "skip")
    nop()         .side(1)
    jmp("down")
    label("skip")
    jmp(y_dec, "pwmloop")
    label("down")
    mov(y, isr)
    label("down_loop")
    jmp(x_not_y, "skip_down")
    nop() .side(0)
    jmp("restart")
    label("skip_down")
    jmp(y_dec, "down_loop")
    
pwm_sm = StateMachine(0, pwm_prog, freq=freq, sideset_base=Pin(0))

pwm_sm.put(max_count)
pwm_sm.exec("pull()")
pwm_sm.exec("mov(isr, osr)")
pwm_sm.active(1)

#note - based on current values of max_count and freq
def calc_pitch(hertz):
    return int( -1 * (((1000000/hertz) -20000)/4))


notes = [392, 440, 494, 523, 587, 659, 698, 784]

notes_val = []
for note in notes:
    notes_val.append(calc_pitch(note))
'''
g4 = 392
a4 = 440
b4 = 494
c5 = 523
d5 = 587
e5 = 659
f5 = 698
g5 = 784
'''

note_len = 0.1
pause_len = 0.05

def play_note(note_len, pause_len, val, sm):
    sm.active(1)
    sm.put(val)
    sleep(note_len)
    sm.active(0)
    sleep(pause_len)

while True: 
    play_note(note_len*2, pause_len, notes_val[0], pwm_sm)
    play_note(note_len, pause_len, notes_val[0], pwm_sm)
    play_note(note_len*4, pause_len, notes_val[1], pwm_sm)
    play_note(note_len*4, pause_len, notes_val[0], pwm_sm)
    play_note(note_len*4, pause_len, notes_val[3], pwm_sm)
    play_note(note_len*8, pause_len, notes_val[2], pwm_sm)

    play_note(note_len*2, pause_len, notes_val[0], pwm_sm)
    play_note(note_len, pause_len, notes_val[0], pwm_sm)
    play_note(note_len*4, pause_len, notes_val[1], pwm_sm)
    play_note(note_len*4, pause_len, notes_val[0], pwm_sm)
    play_note(note_len*4, pause_len, notes_val[4], pwm_sm)
    play_note(note_len*8, pause_len, notes_val[3], pwm_sm)

    play_note(note_len*2, pause_len, notes_val[0], pwm_sm)
    play_note(note_len, pause_len, notes_val[0], pwm_sm)
    play_note(note_len*4, pause_len, notes_val[7], pwm_sm)
    play_note(note_len*4, pause_len, notes_val[5], pwm_sm)
    play_note(note_len*4, pause_len, notes_val[3], pwm_sm)
    play_note(note_len*4, pause_len, notes_val[2], pwm_sm)
    play_note(note_len*4, pause_len, notes_val[1], pwm_sm)

    play_note(note_len*2, pause_len, notes_val[0], pwm_sm)
    play_note(note_len, pause_len, notes_val[0], pwm_sm)
    play_note(note_len*4, pause_len, notes_val[1], pwm_sm)
    play_note(note_len*4, pause_len, notes_val[0], pwm_sm)
    play_note(note_len*4, pause_len, notes_val[4], pwm_sm)
    play_note(note_len*8, pause_len, notes_val[3], pwm_sm)
    sleep(2)
