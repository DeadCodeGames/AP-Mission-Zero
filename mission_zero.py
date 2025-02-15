from sense_hat import SenseHat
import time
import random

sense = SenseHat()
sense.clear()

sense.color.gain = 60
sense.color.integration_cycles = 64


# Colors
rgb = sense.color
bcg = (rgb.red, rgb.green, rgb.blue)
o = (255, 126, 0) #kytka no.1
limetka = (34, 139, 34) #no.1
vypln = (168, 230, 29) #1
gold = (255, 194, 14)#1
ylw = (255, 255, 0)#1
bcg2 = (255, 255, 255) #2
db = (9, 9, 54)#3
b = (9, 5, 247)#3
txc  = (13, 255, 0)#3
p = (247, 0, 185)#3
gg = (0, 255, 136)#3
f = (157, 0, 255)#3

def get_background_color():
    global bcg
    temp = sense.get_temperature()
    if temp < 1: 
        bcg = (100, 149, 237)
        return bcg
    elif temp > 99:
        bcg = (255, 140, 0)
        return bcg
    else:
        bcg = (rgb.red, rgb.green, rgb.blue)
        return bcg

def get_pressure():
    high_pressure = False
    press = sense.get_pressure()
    if press > 760:
        high_pressure = True
    return high_pressure
    

sense.set_rotation(270)

plant_stage = 0
for i in range(8):
    get_background_color()
    if not get_pressure():
        plant_states = [
        [bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg],
    
        [bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, gold, o, o, o, o, gold, bcg],
    
        [bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, gold, bcg, bcg, gold, bcg, bcg,
        gold, o, o, ylw, ylw, o, o, gold,
        bcg, gold, o, o, o, o, gold, bcg],
    
        [bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        gold, bcg, bcg, bcg, bcg, bcg, bcg, gold,
        o, o, gold, o, o, gold, o, o,
        gold, o, o, ylw, ylw, o, o, gold,
        bcg, gold, o, o, o, o, gold, bcg],
    
        [bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        gold, o, vypln, limetka, limetka, vypln, o, gold,
        o, o, gold, o, o, gold, o, o,
        gold, o, o, ylw, ylw, o, o, gold,
        bcg, gold, o, o, o, o, gold, bcg],

        [bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, vypln, limetka, limetka, limetka, limetka, vypln, bcg,
        gold, o, vypln, limetka, limetka, vypln, o, gold,
        o, o, gold, o, o, gold, o, o,
        gold, o, o, ylw, ylw, o, o, gold,
        bcg, gold, o, o, o, o, gold, bcg], 
    
        [bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, limetka, vypln, limetka, limetka, vypln, limetka, bcg,
        bcg, vypln, limetka, limetka, limetka, limetka, vypln, bcg,
        gold, o, vypln, limetka, limetka, vypln, o, gold,
        o, o, gold, o, o, gold, o, o,
        gold, o, o, ylw, ylw, o, o, gold,
        bcg, gold, o, o, o, o, gold, bcg],

        [bcg, bcg, bcg, limetka, vypln, bcg, bcg, bcg,
        bcg, bcg, bcg, vypln, limetka, bcg, bcg, bcg,
        bcg, limetka, vypln, limetka, limetka, vypln, limetka, bcg,
        bcg, vypln, limetka, limetka, limetka, limetka, vypln, bcg,
        gold, o, vypln, limetka, limetka, vypln, o, gold,
        o, o, gold, o, o, gold, o, o,
        gold, o, o, ylw, ylw, o, o, gold,
        bcg, gold, o, o, o, o, gold, bcg]
]
    else:
        plant_states = [
        [bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg],
    
        [bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, gold, o, o, gold, bcg, bcg],
    
        [bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, gold, bcg, bcg, gold, bcg, bcg,
        bcg, gold, o, o, o, o, gold, bcg,
        bcg, bcg, gold, o, o, gold, bcg, bcg],
    
        [bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        gold, bcg, bcg, bcg, bcg, bcg, bcg, gold,
        bcg, o, o, gold, gold, o, o, bcg,
        bcg, gold, o, o, o, o, gold, bcg,
        bcg, bcg, gold, o, o, gold, bcg, bcg],
    
        [bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, gold, o, vypln, vypln, o, gold, bcg,
        bcg, o, o, gold, gold, o, o, bcg,
        bcg, gold, o, o, o, o, gold, bcg,
        bcg, bcg, gold, o, o, gold, bcg, bcg],

        [bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, vypln, limetka, limetka, vypln, bcg, bcg,
        bcg, gold, o, vypln, vypln, o, gold, bcg,
        bcg, o, o, gold, gold, o, o, bcg,
        bcg, gold, o, o, o, o, gold, bcg,
        bcg, bcg, gold, o, o, gold, bcg, bcg], 
    
        [bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, limetka, vypln, vypln, limetka, bcg, bcg,
        bcg, bcg, vypln, limetka, limetka, vypln, bcg, bcg,
        bcg, gold, o, vypln, vypln, o, gold, bcg,
        bcg, o, o, gold, gold, o, o, bcg,
        bcg, gold, o, o, o, o, gold, bcg,
        bcg, bcg, gold, o, o, gold, bcg, bcg],

        [bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
        bcg, bcg, limetka, vypln, vypln, limetka, bcg, bcg,
        bcg, bcg, vypln, limetka, limetka, vypln, bcg, bcg,
        bcg, gold, o, vypln, vypln, o, gold, bcg,
        bcg, o, o, gold, gold, o, o, bcg,
        bcg, gold, o, o, o, o, gold, bcg,
        bcg, bcg, gold, o, o, gold, bcg, bcg]
]
    
    sense.set_pixels(plant_states[plant_stage])
    time.sleep(1)    
    plant_stage+=1
    
    
sense.show_message("DeadCode", text_colour=(rgb.red, rgb.green, rgb.blue), back_colour=(255, 255, 255), scroll_speed=0.1)
plant_stage2 = 0
for i in range(7):
    get_background_color()
    time.sleep(1)
    if not get_pressure():
        plant_states2 = [
            [bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg],
        
            [bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, f, f, bcg, bcg, bcg,
            bcg, bcg, bcg, f, f, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg],
        
            [bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, gg, gg, bcg, bcg, bcg,
            bcg, bcg, gg, f, f, gg, bcg, bcg,
            bcg, bcg, gg, f, f, gg, bcg, bcg,
            bcg, bcg, bcg, gg, gg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg],
        
            [bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, p, p, bcg, bcg, bcg,
            bcg, bcg, p, gg, gg, p, bcg, bcg,
            bcg, p, gg, f, f, gg, p, bcg,
            bcg, p, gg, f, f, gg, p, bcg,
            bcg, bcg, p, gg, gg, p, bcg, bcg,
            bcg, bcg, bcg, p, p, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg],
        
            [bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, txc, p, p, txc, bcg, bcg,
            bcg, txc, p, gg, gg, p, txc, bcg,
            bcg, p, gg, f, f, gg, p, bcg,
            bcg, p, gg, f, f, gg, p, bcg,
            bcg, txc, p, gg, gg, p, txc, bcg,
            bcg, bcg, txc, p, p, txc, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg],
        
            [bcg, bcg, bcg, db, db, bcg, bcg, bcg,
            bcg, bcg, txc, p, p, txc, bcg, bcg,
            bcg, txc, p, gg, gg, p, txc, bcg,
            db, p, gg, f, f, gg, p, db,
            db, p, gg, f, f, gg, p, db,
            bcg, txc, p, gg, gg, p, txc, bcg,
            bcg, bcg, txc, p, p, txc, bcg, bcg,
            bcg, bcg, bcg, db, db, bcg, bcg, bcg],
        
            [bcg, b, b, db, db, b, b, bcg,
            b, b, txc, p, p, txc, b, b,
            b, txc, p, gg, gg, p, txc, b,
            db, p, gg, f, f, gg, p, db,
            db, p, gg, f, f, gg, p, db,
            b, txc, p, gg, gg, p, txc, b,
            b, b, txc, p, p, txc, b, b,
            bcg, b, b, db, db, b, b, bcg]
        ]
    else:
        plant_states2 = [
            [bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg],
        
            [bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg],
        
            [bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, gg, gg, bcg, bcg, bcg, 
            bcg, bcg, bcg, gg, gg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg],
        
            [bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg, 
            bcg, bcg, bcg, p, p, bcg, bcg, bcg, 
            bcg, bcg, p, gg, gg, p, bcg, bcg, 
            bcg, bcg, p, gg, gg, p, bcg, bcg, 
            bcg, bcg, bcg, p, p, bcg, bcg, bcg, 
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg, 
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg],
        
            [bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg,
            bcg, bcg, txc, p, p, txc, bcg, bcg,
            bcg, txc, p, gg, gg, p, txc, bcg,
            bcg, p, gg, f, f, gg, p, bcg,
            bcg, p, gg, f, f, gg, p, bcg,
            bcg, txc, p, gg, gg, p, txc, bcg,
            bcg, bcg, txc, p, p, txc, bcg, bcg,
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg],
        
            [bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg, 
            bcg, bcg, bcg, txc, txc, bcg, bcg, bcg, 
            bcg, bcg, txc, p, p, txc, bcg, bcg, 
            bcg, db, p, gg, gg, p, db, bcg, 
            bcg, db, p, gg, gg, p, db, bcg, 
            bcg, bcg, txc, p, p, txc, bcg, bcg, 
            bcg, bcg, bcg, txc, txc, bcg, bcg, bcg, 
            bcg, bcg, bcg, bcg, bcg, bcg, bcg, bcg],
        
            [bcg, bcg, b, b, b, b, bcg, bcg, 
            bcg, b, b, txc, txc, b, b, bcg, 
            bcg, b, txc, p, p, txc, b, bcg, 
            bcg, db, p, gg, gg, p, db, bcg, 
            bcg, db, p, gg, gg, p, db, bcg, 
            bcg, b, txc, p, p, txc, b, bcg, 
            bcg, b, b, txc, txc, b, b, bcg, 
            bcg, bcg, b, b, b, b, bcg, bcg]
        ]
    sense.set_pixels(plant_states2[plant_stage2])
    plant_stage2+=1
time.sleep(2)
sense.clear()