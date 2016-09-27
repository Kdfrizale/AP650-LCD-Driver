##Program to parse text and display it on LCD

import os
import sys

text = sys.argv[2]
place = sys.argv[1]
position = 0

if not text:
        sys.exit()

if place == "0":
        ##Change the Display of the Clock, large segment displays
        if len(text) == 4:
                address1 = "80"
                data1 = "00"
                number = text[1]
                if number == "1":
                        data1 = "16"
                elif number == "2":
                        data1 = "7d"
                elif number == "3":
                        data1 = "5f"
                elif number == "4":
                        data1 = "d6"
                elif number == "5":
                        data1 = "db"
                elif number == "6":
                        data1 = "fb"
                elif number == "7":
                        data1 = "1e"
                elif number == "8":
                        data1 = "ff"
                elif number == "9":
                        data1 = "de"
                elif number == "0":
                        data1 = "bf"

                os.system("i2cset -y 1 0x20 0x" + address1 + " 0x" + data1)
                position = position + 1
                text = text[2:]
                
        for number in text:
                if position == 0:
                        address1 = "80"
                elif position == 1:
                        address1 = "82"
                elif position == 2:
                        address1 = "84"
                else:
                        break
                
                data1 = "00"
                if number == "1":
                        data1 = "06"
                elif number == "2":
                        data1 = "6d"
                elif number == "3":
                        data1 = "4f"
                elif number == "4":
                        data1 = "c6"
                elif number == "5":
                        data1 = "cb"
                elif number == "6":
                        data1 = "eb"
                elif number == "7":
                        data1 = "0e"
                elif number == "8":
                        data1 = "ef"
                elif number == "9":
                        data1 = "ce"
                elif number == "0":
                        data1 = "af"

                os.system("i2cset -y 1 0x20 0x" + address1 + " 0x" + data1)
                position = position + 1


        
if place == "1":
        ##Change the Display of the small segment display
        for character in text:

                if position == 0:
                        address1 = "87"
                        address2 = "89"
                elif position == 1:
                        address1 = "8b"
                        address2 = "8d"
                elif position == 2:
                        address1 = "90"
                        address2 = "92"
                elif position == 3:
                        address1 = "94"
                        address2 = "96"
                elif position == 4:
                        address1 = "99"
                        address2 = "9b"
                elif position == 5:
                        address1 = "9d"
                        address2 = "9f"
                else:
                        break
                
                data1 = "00"
                data2 = "00"
                if character == "a":
                        data1 = "d4"
                        data2 = "aa"
                        
                elif character == "b":
                        data1 = "f4"
                        data2 = "22"
                        
                elif character == "c":
                        data1 = "e0"
                        data2 = "80"
                        
                elif character == "d":
                        data1 = "74"
                        data2 = "2a"
                        
                elif character == "e":
                        data1 = "e4"
                        data2 = "a0"
                        
                elif character == "f":
                        data1 = "c4"
                        data2 = "a0"
                        
                elif character == "g":
                        data1 = "f0"
                        data2 = "a2"
                        
                elif character == "h":
                        data1 = "d4"
                        data2 = "28"
                        
                elif character == "i":
                        data1 = "20"
                        data2 = "f0"
                        
                elif character == "j":
                        data1 = "70"
                        data2 = "88"
                        
                elif character == "k":
                        data1 = "00"
                        data2 = "75"
                        
                elif character == "l":
                        data1 = "e0"
                        data2 = "00"
                        
                elif character == "m":
                        data1 = "d9"
                        data2 = "2c"
                        
                elif character == "n":
                        data1 = "d8"
                        data2 = "29"
                        
                elif character == "o":
                        data1 = "f0"
                        data2 = "88"
                        
                elif character == "p":
                        data1 = "c4"
                        data2 = "aa"
                        
                elif character == "q":
                        data1 = "f0"
                        data2 = "89"
                        
                elif character == "r":
                        data1 = "c4"
                        data2 = "ab"
                        
                elif character == "s":
                        data1 = "b0"
                        data2 = "a2"
                        
                elif character == "t":
                        data1 = "00"
                        data2 = "f0"
                        
                elif character == "u":
                        data1 = "f0"
                        data2 = "08"
                        
                elif character == "v":
                        data1 = "08"
                        data2 = "24"
                        
                elif character == "w":
                        data1 = "d2"
                        data2 = "39"
                        
                elif character == "x":
                        data1 = "0a"
                        data2 = "25"
                        
                elif character == "y":
                        data1 = "08"
                        data2 = "34"
                        
                elif character == "z":
                        data1 = "22"
                        data2 = "a4"
                

                os.system("i2cset -y 1 0x20 0x" + address1 + " 0x" + data1)
                os.system("i2cset -y 1 0x20 0x" + address2 + " 0x" + data2)

                position = position + 1
                
