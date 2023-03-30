from django.db import models

# Create your models here.

class HexBase():

    def __init__(self,r,g,b):
        self.r = int(r or 0)
        self.g = int(g or 0)
        self.b = int(b or 0)
    
class HexRegular(HexBase):

    def convert_digits(self,n):
        if n > 9:
            return 'ABCDEF'[n-10]
        return str(n)

    def hexify(self,num):
        return self.convert_digits(num//16)+self.convert_digits(num%16)
    
    def result(self):
        return self.hexify(self.r)+self.hexify(self.g)+self.hexify(self.b)

class HexLimiter(HexRegular):
    
    def __init__(self,r,g,b):
        self.r = self.limiter(r)
        self.g = self.limiter(g)        
        self.b = self.limiter(b)

    def limiter(self,num):
        if num > 255:
            return 255
        if num < 0:
            return 0
        return num           
    
class HexFactory(HexBase):
    
    def factory_result(self):
        for i in self.r,self.g,self.b:
            if i not in range(256):
                return HexLimiter(self.r,self.g,self.b).result()
        return HexRegular(self.r,self.g,self.b).result()