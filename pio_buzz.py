  
# Basic sound output.
# bit of a buzz-y square wave. Sounds better at higher frequencies than lower ones.


from machine import Pin
from rp2 import PIO, StateMachine, asm_pio
from time import sleep

max_count = 5000
freq = 1000000

#set the pin low, then count down y (from max_count) until it reaches the value of x
#then set pin high, reset y and loop again. once y=x, the whole program wraps,
#pulls in new data if there is any, sets the pin low and starts again.
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

#need to load the maximum value into the input shift register
#this is used to populate the 'y' scratch register each loop so it can then count down from the same number
pwm_sm.put(max_count)
pwm_sm.exec("pull()")
pwm_sm.exec("mov(isr, osr)")
pwm_sm.active(1)

while True:
    for i in range(int(max_count/2),max_count):
        pwm_sm.put(i)
        sleep(0.001)
