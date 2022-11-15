import random

explotionParticles = []

class Explotion:
    global particle
    global explotionParticles
    def Init(self, ledID, characterID, color, NUM_PARTICLES):
        for i in range(0, NUM_PARTICLES):
            particle = ExplotionParticle()
            particle.Init(color, ledID, characterID, i)
            explotionParticles.append(particle)
        
class ExplotionParticle:
    global NUM_LEDS
    speed = 0
    ledID = 0
    color = (0,0,0)
    characterID = 0
    num = 0
    desacelerate = 2.0
    def Init(self, color, ledID, characterID, num):
        self.speed = random.randrange(1, 10)        
        self.desacelerate = random.randrange(20, 40)/10
        self.num = num
        self.ledID = ledID
        self.characterID = characterID
        self.color = color
    def Update(self, NUM_LEDS):
        self.speed = self.speed / 1.075
        if self.speed < 1:
            self.color = (int(self.color[0] * self.speed), int(self.color[1] * self.speed), int(self.color[2] * self.speed))
        if self.num % 2 == 0:
            self.ledID = round(self.ledID-(self.speed/self.desacelerate))
        else:
            self.ledID = round(self.ledID+(self.speed/self.desacelerate))
            
        if self.ledID>=NUM_LEDS:
            self.ledID = 0
        if self.ledID<0:
            self.ledID = NUM_LEDS


