#!/usr/bin/env python

# I'm sleepy gonna write some comments
# Your code should be able to read as if someone who doesn't 
# code can understand wtf is going on.

# Also, maybe make a project w a kanban board in github.  Or I can make issues on the repository or smoething

# Is the purpose of this file to provide functionality for the card reader so it keeps reading forever and ever and ever and ever?
# I was a lil sleepy during your explanation.  What specific functionality are you trying to achieve?
# - Start audio when rfid card is read
# - Stop audio when rfid card is removed
# - What was the purpose of the times again?  The only reason I think you want to keep track of the time is if you want your kid to
#       start off where she left off for a particular story.  You can implement taht later if she wants, but I think it should just restart from the beginning for now.

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import os
import signal
import time
import pygame

# Directory to ellie's audiobooks
# BOOK_DIRECTORY = '/home/pi/ellie_pi/'
test_path = os.getcwd()
BOOK_DIRECTORY = test_path +  '/book_files/'
rfid_reader = SimpleMFRC522()

IsPaused = False

pygame.mixer.init()


# This function should probably be in a separate file and imported into the read file
"""
Plays audio

:param audiofile: Path to audo file to play
:return void: 
"""
def play_audio(audiofile):
    global myprocess # Remove this if not needed

    playing_audio = pygame.mixer.music.get_busy()

    if not playing_audio:
      print("No audio playing, start playing new audio")

    else:
        print("Audio alread playing, so quit current audio, then play")
        pygame.mixer.music.stop()

    # Load Music
    pygame.mixer.music.load(BOOK_DIRECTORY + audiofile)

    # Play Music
    pygame.mixer.music.play()

    # Is this time.sleep necessary?
    time.sleep(3)

print("Let's listen to some stories!")

try:

    # Not good to have an infinite loop -> have a way for your kid to turn it on off or have a global variable that can be set to true or false
    # while readyToReadRfidCard -> maybe more pythonic like this -> while ready_to_read_rfid_card
    while True:

        playing_audio = pygame.mixer.music.get_busy()

        if not playing_audio:

            # What does this do?  Generates a new int in base 10?
            current_book_id = int(10)

        start_time = time.time()

        print("Ready to Read a Book")
        id, book = rfid_reader.read()
        if id == None:
            # You probably shouldn't be overwriting playing_audio here with your own boolean
            # you should call pygame.mixer.music.get_busy() and get that value
            playing_audio = True
        print("Playing AudioBook: " + book)
        print("ID is: " + str(id))
        book = book.strip() # no im not strippin for u, wth is this? removes empty space at the end of a string?

        if current_book_id !=  id:
            current_book_id = id
            play_audio(book)
        else:
            end_time = time.time()
            elapsed_time = end_time - start_time

        if playing_audio == True:
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
