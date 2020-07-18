#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import pygame

reader = SimpleMFRC522()

try:
        id, text = reader.read()
       # print(id)
        print("Read File: " + text)
finally:
        GPIO.cleanup()

        
        pygame.mixer.init()
        pygame.mixer.music.load(text.strip())
        pygame.mixer.music.play()
        print("Playing AudioBook: " + text)
        while pygame.mixer.music.get_busy() == True:
                continue
