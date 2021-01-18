  
# Basic sound output. Pretty horrible square wave buzz
#todo: check with logic analyser that it's doing what's expected

from machine import Pin
from rp2 import PIO, StateMachine, asm_pio
from time import sleep

max_count = 5000
freq = 1000000
#longest period  = freq/maxcount
#this does a spike
@asm_pio(sideset_init=PIO.OUT_LOW)
def pwm_prog():
    label("restart")
    pull(noblock) .side(0)
    mov(x, osr) # Keep most recent pull data stashed in X, for recycling by noblock
    mov(y, isr) # ISR must be preloaded with PWM count max
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

while True:
    for i in range(max_count):
        pwm_sm.put(i)
        print(i)


