from machine import Pin
import rp2

global sm
global all
all = []

PIN_NUM = 22

@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()

sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(PIN_NUM))
sm.active(1)

def Update(NUM_LEDS):    
    dimmer_ar = array.array("I", [0 for _ in range(NUM_LEDS)])
    
def SetLeds(dimmer_ar, NUM):    
    sm.put(dimmer_ar,NUM)
    
    
