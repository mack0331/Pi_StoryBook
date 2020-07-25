#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import os
import signal
import time
import pygame

pygame.mixer.init()

IsPaused = False

def playaudio(audiofile):
    global myprocess
    global directory

    status = pygame.mixer.music.get_busy()

    if status == False:
        print("No audio playing, start playing new audio")

    else:
        print("Audio alread playing, so quit current audio, then play")
        pygame.mixer.music.stop()


    pygame.mixer.music.load(directory + audiofile)
    pygame.mixer.music.play()

    time.sleep(3)

reader = SimpleMFRC522()

directory = '/home/pi/ellie_pi/'

print("Let's listen to some stories!")

try:

    while True:

        status = pygame.mixer.music.get_busy()

        if status == False:

            current_book_id = int(10)

        start_time = time.time()

        print("Ready to Read a Book")
        id, book = reader.read()
        if id == None:
            status = True
        print("Playing AudioBook: " + book)
        print("ID is: " + str(id))
        book = book.strip()

        if current_book_id !=  id:
            current_book_id = id
            playaudio(book)
#        else:
            end_time = time.time()
            elapsed_time = end_time - start_time

        if status == True:
            if elapsed_time > 0.6:
                if IsPaused == True:
                    pygame.mixer.music.unpause()
                    IsPaused = False
                else:
                    pygame.mixer.music.pause()
                    IsPaused = True

except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nAll Done")
