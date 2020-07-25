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

pygame.mixer.init()

IsPaused = False


# This function should probably be in a separate file and imported into the read file
def playaudio(audiofile):
    global myprocess
    global directory

    # Wth does status mean
    # A better variable name might be...
    # playingAudio = pygame.mixer.music.get_busy()
    status = pygame.mixer.music.get_busy()

    # Pretty sure python has the not keyword which gets the inverse of a boolean
    # if not playingAudio
    #   print("No audio playing, start playing new audio")
    if status == False:
        print("No audio playing, start playing new audio")

    else:
        print("Audio alread playing, so quit current audio, then play")
        pygame.mixer.music.stop()

    # Load Music
    pygame.mixer.music.load(directory + audiofile)

    # Play Music
    pygame.mixer.music.play()

    # Is this time.sleep necessary?
    time.sleep(3)

# Think of a better clearer name, reader is a bit vague imo
# rfidReader = SimpleMFRC522()
reader = SimpleMFRC522()

# The global directory variable is made in the playAudio function.  Why?
# If this will not/should not be changed yuo can make it a constant
# ie: DIRECTORY = '/home/pi/ellie_pi/'
# probably at the top of this page next to IsPause
directory = '/home/pi/ellie_pi/'

print("Let's listen to some stories!")

try:

    # Not good to have an infinite loop -> have a way for your kid to turn it on off or have a global variable that can be set to true or false
    # while readyToReadRfidCard -> maybe more pythonic like this -> while ready_to_read_rfid_card
    while True:

        # See status comment above
        status = pygame.mixer.music.get_busy()

        # See if status comment above
        if status == False:

            # What does this do?  Generates a new int in base 10?
            current_book_id = int(10)

        start_time = time.time()

        print("Ready to Read a Book")
        id, book = reader.read()
        if id == None:
            # You probably shouldn't be overwriting status here with your own boolean
            # you should call pygame.mixer.music.get_busy() and get that value
            status = True
        print("Playing AudioBook: " + book)
        print("ID is: " + str(id))
        book = book.strip() # no im not strippin for u, wth is this? removes empty space at the end of a string?

        if current_book_id !=  id:
            current_book_id = id
            playaudio(book)
        else:
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
