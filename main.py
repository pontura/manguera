import array, time
import math
import random
import character, explotion, leds, led, inputs

NUM_PARTICLES = 18
NUM_LEDS = 300

zone1 = [200,250]
leds_zone1 = []     
         
    
def Init():
    global character1
    global character2
    global NUM_LEDS
    
    framerate = 2.5
    acceleration = 0.02
    
    character1 = character.Character()
    character1.Init(1, framerate, acceleration)
    
    character2 = character.Character()
    character2.Init(2, framerate, acceleration)
    
    for i in range(NUM_LEDS):
        thisLed = led.Led(i)
        thisLed.Init(i)
        thisLed.SetOriginalValues(0)
        leds.all.append(thisLed)
    for i in range(zone1[0], zone1[1]):
        thisLed = leds.all[i]
        thisLed.SetCurve(0.5)
        leds_zone1.append(thisLed)

        
def Loop():
    while True:
        inputs.UpdatePot()
        character1.Move(inputs.pot1_value, NUM_LEDS)
        character2.Move(inputs.pot2_value, NUM_LEDS)
        dimmer_ar = array.array("I", [0 for _ in range(NUM_LEDS)])
        SetCurves(dimmer_ar)
        UpdateCollisions(dimmer_ar)
        if character1.state == 1:
            playCharacter(1, dimmer_ar)        
        if character2.state == 1:
            playCharacter(2, dimmer_ar)
        leds.SetLeds(dimmer_ar,8)
        time.sleep(0.01)
    
    
def UpdateCollisions(dimmer_ar):
    global characterID
    if len(explotion.explotionParticles) > 0:
        i = len(explotion.explotionParticles)
        while i > 0:
            particle = explotion.explotionParticles[i-1]
            characterID = particle.characterID
            particle.Update(NUM_LEDS)
            SetPixel(dimmer_ar, particle.color, particle.ledID)
            if particle.speed<=0.01:                
                explotion.explotionParticles.remove(particle)
                del particle;
            i = i-1

        if len(explotion.explotionParticles) ==0:
            if characterID==1:
                character1.WakeUp()
            else:
                character2.WakeUp()
            
            
    
def playCharacter(characterID, dimmer_ar):
    
    if characterID == 1:
        speed = character1.speed 
        id = math.floor(character1.pos)
        decimals = character1.pos% 1
    else:
        speed = character2.speed 
        id = math.floor(character2.pos)
        decimals = character2.pos% 1
        
    if id>=NUM_LEDS:
        id = 0
        
    ledsToCalculate = (speed * 8) + 2
    for i in range(ledsToCalculate):
        
        realID = int(id-i)
        
        if realID<0:
            realID = NUM_LEDS+realID
            
        led = leds.all[realID]
        curveValue = led.curveValue
        if curveValue >0 and curveValue < speed:
            if characterID == 1: 
                character1.Explote(NUM_PARTICLES)
            else:                    
                character2.Explote(NUM_PARTICLES)
        else: 
            maxColorValue = 50
            if i == 0:
                led.ChangeValues((maxColorValue*decimals))
            elif i == 1 :
                if speed < 0.2:
                    led.ChangeValues(maxColorValue*(1-decimals))
                else:
                    led.ChangeValues(maxColorValue)            
            else:
                led.Reset()
            
            if led.value >0:
                colorVar = int(led.value)
                
                if characterID == 1:   
                    SetPixel(dimmer_ar,(0,0,colorVar), realID)
                else:
                    SetPixel(dimmer_ar,(0,colorVar,0), realID)         
        
                
                
                
   
zoneLedOnID = 0 
def SetCurves(dimmer_ar):
    global zoneLedOnID
    zoneLedOnID = zoneLedOnID+1
    for i in range(0, len(leds_zone1)):
        thisLed = leds_zone1[i]
        
        if i % 2 == 0:
            zoneLedOnID = 0
        else:
            SetPixel(dimmer_ar, (5,0,0), thisLed.id) 
    

def SetPixel(dimmer_ar, color, id):
    c = setColor(color)
    r = int(((c >> 8) & 0xFF) )
    g = int(((c >> 16) & 0xFF))
    b = int((c & 0xFF) )
    dimmer_ar[id] = (g<<16) + (r<<8) + b      
   
   
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)

def setColor(color):
    return (color[1]<<16) + (color[0]<<8) + color[2]


        
def lerp(a: float, b: float, t: float) -> float:
    return (1 - t) * a + t * b

Init()
Loop()


     





