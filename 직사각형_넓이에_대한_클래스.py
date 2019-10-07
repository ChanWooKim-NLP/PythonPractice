class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
    def check(self):
        if self.x1 == self.x2 or self.y1 == self.y2:
            return False
        else: return True
        
    def area(self):
        return abs(self.x1-self.x2)*abs(self.y1-self.y2)
    
    def __call__(self):
        if self.x1 == self.x2 or self.y1 == self.y2:
            return "출력 불가"
        else:
            return (self.x1, self.y1)
            return (self.x2, self.y2)
            return abs(self.x1-self.x2)*abs(self.y1-self.y2)
        
    def equal(self, x3, y3):
        self.x3 = x3
        self.y3 = y3
        if (x3 == self.x1 or x3 == self.x2) and (y3 == self.y1 or y3 == self.y2):
            return True
        else:
            if abs(x3-self.x1)*abs(y3-self.y1) == abs(self.x1-self.x2)*abs(self.y1-self.y2):
                return True
            elif abs(x3-self.x2)*abs(y3-self.y2) == abs(self.x1-self.x2)*abs(self.y1-self.y2):
                return True
            else:
                return False
            
