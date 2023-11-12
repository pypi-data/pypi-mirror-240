# -*- coding: utf-8 -*-
"""
@author: franc
"""


import numpy as np
import time


print("===== SIMULATION VERSION 1 =====")



def perte(v1,v2,v3,pump):
    return .0001*(pump*(v1+2*v2+2*v3))**2

def flux(v1,v2,v3,pump,vol1):
    if(v1+v2+v3)>0:
        p = perte(v1,v2,v3,pump)
        if (p<0):
            p=0
        total = (pump**1.2)*.005
        if total > vol1:
            total = vol1
        else:
            pe = perte(v1,v2,v3,pump)*.005
            if( total - pe ) > 0:
                total = (total - pe)
        tv = ((1-.27*2)*v1 + .27*v2 + .27*v3)
        return [(1-.27*2)*v1/tv*total , .27*v2/tv*total , .27*v3/tv*total]
    else:
        return [0,0,0]

def gravite(vol2,vol3):
    coeff = .001
    a = coeff*vol2
    b = coeff*vol3
    if a < 0:
        a= 0
    else:
        a = a**.5
        if(a > vol2):
            a = vol2
    if b < 0:
        b = 0
    else:
        b = b**.5
        if(b > vol3):
            b = vol3
    return a, b




class systeme:
    
    
    def __init__(self,):     
        self.vol1 = 100
        self.vol2 = 30
        self.vol3 = 30
        self.valve1 = False
        self.valve1_count = 0
        self.valve1_cc = np.random.randint(10,30)


    def valeurs_actuelles(self):
        levels = {  
                    "r1":np.round(self.vol1/20,2),
                    "r2":np.round(self.vol2/20,2),
                    "r3":np.round(self.vol3/20,2)
                 }
        levels["valve1"] = self.valve1
        return levels
        

    def prochaine_action(self,pump,valve2,valve3):
        
        if (isinstance(pump,int) | isinstance(pump,float)):
            if ( (pump<0) | (pump>100) ):
                raise ValueError('La valeur de la pompe doit être entre 0 et 100')
        else:
            raise TypeError('La valeur de la pompe doit être un int ou un float')
        
        if( isinstance(valve2,bool) == False ):
            raise TypeError('La valeur de valve2 doit être un bool')
        if( isinstance(valve3,bool) == False ):
            raise TypeError('La valeur de valve3 doit être un bool')
        
        pump_value = pump
       
        valve1 = self.valve1 
       
        # Modify pump value if no open valve
        if( ((valve1) + (valve2) + (valve3))==0 ):
            pump_value = 0
        
        for _ in range(5):
            f_in = (flux(valve1,valve2,valve3,pump_value,self.vol1))
            f_out = (gravite(self.vol2,self.vol3))
            self.vol1 += -f_in[1] - f_in[2] + f_out[0] + f_out[1]
            self.vol2 +=  f_in[1] - f_out[0]
            self.vol3 +=  f_in[2] - f_out[1]
                    
        time.sleep(0.99)
        
        self.valve1_count += 1
        if(self.valve1_count >= self.valve1_cc):
            self.valve1 = (self.valve1 == False)
            self.valve1_count = 0
            self.valve1_cc = np.random.randint(10,30)
        


# TEST
if __name__ == "__main__":
    sys = systeme()
    print(sys.valeurs_actuelles())
    for _ in range(10):
        sys.prochaine_action(100,False,True)
        print(sys.valeurs_actuelles())

    sys.prochaine_action(103,True,False)