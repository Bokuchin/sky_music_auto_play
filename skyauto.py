#!/usr/bin/env python3
#jidou ensou program.
#mode:a ha midi ensou mode.
#mode:b ha procon sousa mode.
#terminal ni a ka b wo uchikonde mode wo kaeru.
import os
import threading
import time
import pygame.midi as m
import csv

m.init()
i = m.Input(3)#midi device number

# Re-connect USB Gadget device
os.system('echo > /sys/kernel/config/usb_gadget/procon/UDC')
os.system('ls /sys/class/udc > /sys/kernel/config/usb_gadget/procon/UDC')

time.sleep(0.5)

gadget = os.open('/dev/hidg0', os.O_RDWR | os.O_NONBLOCK)
procon = os.open('/dev/hidraw3', os.O_RDWR | os.O_NONBLOCK)

mode = "a"
def key_wari():
    global mode
    while True:
        mode = input()




ri_btn = 0b00000000
le_btn = 0b00000000
l_stk6 = 0b00000000
l_stk7 = 0b00000000
l_stk8 = 0b00000000

r_stk9 = 0b00000000
r_stk10 = 0b00000000
r_stk11 = 0b00000000
zr_btn = 0b10000000
r_btn  = 0b01000000
x_btn  = 0b00000010
a_btn  = 0b00001000
b_btn  = 0b00000100
y_btn  = 0b00000001
zl_btn = 0b10000000
dwn_btn= 0b00000001
lft_btn= 0b00001000
up_btn = 0b00000010
rit_btn= 0b00000100
l_btn  = 0b01000000
keyflg = [0 for i in range(73)]

def replace_mouse(md_ev):
    
    global ri_btn, le_btn, l_stk6, l_stk7, l_stk8, r_stk9, r_stk10, r_stk11, zr_btn, r_btn, x_btn, a_btn, b_btn, y_btn, zl_btn, dwn_btn, lft_btn, up_btn, rit_btn, l_btn

    for i in range(len(md_ev)):

        key = md_ev[i][0][1]
        push = md_ev[i][0][0]
       
        if type(ri_btn) is bytes:
            ri_btn = int.from_bytes(ri_btn, byteorder='little')
        if type(le_btn) is bytes:
            le_btn = int.from_bytes(le_btn, byteorder='little')    

        if (push == 144 and key == 48):#do
            keyflg[48] = 1
        if (push == 144 and key == 50):#re
            keyflg[50] = 1
        if (push == 144 and key == 52):#mi
            keyflg[52] = 1
        if (push == 144 and key == 53):#fa
            keyflg[53] = 1
        if (push == 144 and key == 55):#so
            keyflg[55] = 1
        if (push == 144 and key == 57):#ra
            keyflg[57] = 1
        if (push == 144 and key == 59):#shi
            keyflg[59] = 1
        if (push == 144 and key == 60):#do
            keyflg[60] = 1
        if (push == 144 and key == 62):#re
            keyflg[62] = 1
        if (push == 144 and key == 64):#mi
            keyflg[64] = 1
        if (push == 144 and key == 65):#fa
            keyflg[65] = 1
        if (push == 144 and key == 67):#so
            keyflg[67] = 1
        if (push == 144 and key == 69):#ra
            keyflg[69] = 1
        if (push == 144 and key == 72):#do
            keyflg[72] = 1    
        if (push == 144 and key == 71):#shi
            keyflg[71] = 1 
    
        ####
        if (push == 128 and key == 48):#do
            keyflg[48] = 0
        if (push == 128 and key == 50):#re
            keyflg[50] = 0
        if (push == 128 and key == 52):#mi
            keyflg[52] = 0
        if (push == 128 and key == 53):#fa
            keyflg[53] = 0
        if (push == 128 and key == 55):#so
            keyflg[55] = 0
        if (push == 128 and key == 57):#ra
            keyflg[57] = 0
        if (push == 128 and key == 59):#shi
            keyflg[59] = 0
        if (push == 128 and key == 60):#do
            keyflg[60] = 0
        if (push == 128 and key == 62):#re
            keyflg[62] = 0
        if (push == 128 and key == 64):#mi
            keyflg[64] = 0
        if (push == 128 and key == 65):#fa
            keyflg[65] = 0
        if (push == 128 and key == 67):#so
            keyflg[67] = 0
        if (push == 128 and key == 69):#ra
            keyflg[69] = 0
        if (push == 128 and key == 72):#do
            keyflg[72] = 0
        if (push == 128 and key == 71):#shi
            keyflg[71] = 0     
        ####

        ################
        if keyflg[48] == 1:
            le_btn = zl_btn | le_btn
        else:
            le_btn = 0b01111111 & le_btn
        if keyflg[50] == 1:
            ri_btn = zr_btn | ri_btn
        else:
            ri_btn = 0b01111111 & ri_btn
        if keyflg[52] == 1:
            le_btn = dwn_btn | le_btn
        else:
            le_btn = 0b11111110 & le_btn
        if keyflg[53] == 1:
            ri_btn = b_btn | ri_btn
        else:
            ri_btn = 0b11111011 & ri_btn
        if keyflg[55] == 1:
            le_btn = lft_btn | le_btn
        else:
            le_btn = 0b11110111 & le_btn
        if keyflg[57] == 1:
            ri_btn = y_btn | ri_btn
        else:
            ri_btn = 0b11111110 & ri_btn
        if keyflg[59] == 1:
            le_btn = up_btn | le_btn
        else:
            le_btn = 0b11111101 & le_btn
        if keyflg[60] == 1:
            ri_btn = x_btn | ri_btn
        else:
            ri_btn = 0b11111101 & ri_btn
        if keyflg[62] == 1:
            le_btn = rit_btn | le_btn
        else:
            le_btn = 0b11111011 & le_btn
        if keyflg[64] == 1:
            ri_btn = a_btn | ri_btn
        else:
            ri_btn = 0b11110111 & ri_btn
        if keyflg[65] == 1:
            le_btn = l_btn | le_btn
        else:
            le_btn = 0b10111111 & le_btn
        if keyflg[67] == 1:
            ri_btn = r_btn | ri_btn
        else:
            ri_btn = 0b10111111 & ri_btn
        if keyflg[69] == 1:
            l_stk6 = 0b00000000
            l_stk7 = 0b00000000
            l_stk8 = 0b01110000

            #l_stk6 = l_stk6.to_bytes(1, byteorder="little")
            #l_stk7 = l_stk7.to_bytes(1, byteorder="little")
            #l_stk8 = l_stk8.to_bytes(1, byteorder="little")
    
        elif keyflg[72] == 1:
            l_stk6 = 0b00000000
            l_stk7 = 0b00001111
            l_stk8 = 0b01110000

            #l_stk6 = l_stk6.to_bytes(1, byteorder="little")
            #l_stk7 = l_stk7.to_bytes(1, byteorder="little")
            #l_stk8 = l_stk8.to_bytes(1, byteorder="little")
        else:
            #l_stk6 = (0b00000000).to_bytes(1, byteorder="little")#output_data[6:7]
            #l_stk7 = (0b00000111).to_bytes(1, byteorder="little")#output_data[7:8]
            #l_stk8 = (0b01110000).to_bytes(1, byteorder="little")#output_data[8:9]        
            l_stk6 = 0b00000000
            l_stk7 = 0b00000111#0b00000111
            l_stk8 = 0b01110000#0b01110000
        if keyflg[71] == 1:
            r_stk9 = 0b00000000
            r_stk10 = 0b00000000
            r_stk11 = 0b01110000

            #r_stk9 = r_stk9.to_bytes(1, byteorder="little")
            #r_stk10 = r_stk10.to_bytes(1, byteorder="little")
            #r_stk11 = r_stk11.to_bytes(1, byteorder="little")
        else:
            #r_stk9 = (0b00000000).to_bytes(1, byteorder="little")#output_data[9:10]
            #r_stk10 = (0b00000111).to_bytes(1, byteorder="little")#output_data[10:11]
            #r_stk11 = (0b01110000).to_bytes(1, byteorder="little")#output_data[11:12]
            r_stk9 = 0b00000000
            r_stk10 = 0b00000111#0b00000111
            r_stk11 = 0b01110000#0b01110000

    ################
    #print(format(ri_btn, '08b') + " " + format(le_btn, '08b'))
    ri_btn = ri_btn#ri_btn.to_bytes(1, byteorder='little')
    le_btn = le_btn#le_btn.to_bytes(1, byteorder='little')

    
    
    return ri_btn, le_btn, l_stk6, l_stk7, l_stk8, r_stk9, r_stk10, r_stk11
print(1)
fh = open("guresenbon.csv", "r")
reader = csv.reader(fh)
score = []
print(2)
for j in reader:
    score.append(j)
print(3)

ti = time.time()
k = 1000#tempo
count = 0
md_ev = [[[0,1]]]
def autoplay():
    global ti, score, count
    prgrs = time.time() - ti
    sound = score[count]
    if int(sound[0]) > prgrs * k:
        m_e = [[[0,1]]]
    else:
        m_e = [[[int(sound[1]), int(sound[2])]]]
        count += 1
    return m_e

modeflg = "a"
threading.Thread(target=key_wari).start()
ti2 = time.time()
while True:
    #print(4)
    if i.poll(): # MIDIが受信されると１
        md_ev = i.read(4) # 読み取る入力イベントの数
        #print ("midi_events:" + str(md_ev))
    if count <= len(score)-1:
        if time.time() > ti2 + 0.02:
            md_ev = autoplay()
            ti2 = time.time()
    ri_btnb, le_btnb, l_stk6b,l_stk7b, l_stk8b, r_stk9b, r_stk10b, r_stk11b  = replace_mouse(md_ev)
    #print(5)
    try:
        input_data = os.read(gadget, 128)
        os.write(procon, input_data)
    except BlockingIOError:
        pass
    except:
        os._exit(1)
    #print(6)

    
    try:
        output_data = os.read(procon, 128)
        if mode == "a":#midi mode
            if modeflg == "a":
                print("mode:a")
                modeflg = "b"
            ri_btnb = ri_btnb | output_data[3]
            le_btnb = le_btnb | output_data[5]
        
            ri_btnb = ri_btnb.to_bytes(1, byteorder='little')
            le_btnb = le_btnb.to_bytes(1, byteorder='little')
            l_stk6b = l_stk6b.to_bytes(1, byteorder='little')
            l_stk7b = l_stk7b.to_bytes(1, byteorder='little')
            l_stk8b = l_stk8b.to_bytes(1, byteorder='little')
            r_stk9b = r_stk9b.to_bytes(1, byteorder='little')
            r_stk10b= r_stk10b.to_bytes(1, byteorder='little')
            r_stk11b= r_stk11b.to_bytes(1, byteorder='little')
            e = output_data[0:3] + ri_btnb + output_data[4:5] + le_btnb + l_stk6b + l_stk7b + l_stk8b + r_stk9b + r_stk10b + r_stk11b + output_data[12:63]
        elif mode == "b":#procon sousa mode
            if modeflg == "b":
                print("mode:b")
                modeflg = "a"
            e = output_data
        elif mode == "r":#music repeat
            ti = time.time()
            count = 0
            md_ev = [[[0,1]]]
            mode = "a"
            modeflg = "a"
        
        os.write(gadget, e)#output_data
    except BlockingIOError:
        pass
    except Exception as g:
        print(type(g))
        print(g)
        os._exit(1)

