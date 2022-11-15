class Led:
    id = 0
    original_value = 0
    trail_speed = 1.7
    value = 0
    curveValue = 0
    def Init(self, id):
        self.id = id
        self.original_value = 0
        self.value = 0
    def SetOriginalValues(self, value):        
        self.original_value = value
    def ChangeValues(self, value):
        self.value = value
    def Reset(self):
        if self.value != self.original_value:
            if self.value > 1:
                self.value = self.value / self.trail_speed
            elif self.value < 1:
                self.value = self.original_value
    def SetCurve(self, value):
        self.curveValue = value
