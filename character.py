import led
import explotion

class Character:
    # 0 = waiting
    # 1 = playing
    # 2 = explote
    speed = 0
    maxspeed = 1
    framerate = 3
    acceleration = 0.01
    state = 1 
    global explotion
    id = 0
    color = (255,0,0)
    
    def Init(self, id, framerate, acceleration):
        self.framerate = framerate
        self.acceleration = acceleration
        self.id = id
        self.pos = 0
        if id == 1:
            self.color = (0,0,255)
        else:
            self.color = (0,255,0)
    def Move(self, value, NUM_LEDS):
                
        if self.state == 1:            
            if self.speed < value:
                self.speed = self.speed + self.acceleration            
                if self.speed > self.maxspeed:
                    self.speed = self.maxspeed
            if self.speed > value:
                self.speed = self.speed - self.acceleration            
                if self.speed < 0:
                    self.speed = 0
            self.pos = self.pos + (self.speed*self.framerate)           
            if self.pos > NUM_LEDS:
                self.pos = 0
            
    def Explote(self, NUM_PARTICLES):
        self.speed = 0
       # print("Explote ", self.id)
        self.state = 2
        thisExplotion = explotion.Explotion()
        thisExplotion.Init(round(self.pos), self.id, self.color, NUM_PARTICLES)
        
    def WakeUp(self):        
        self.speed = 0
       # print("WakeUp ", self.id)
        self.state = 1



