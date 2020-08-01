#!/usr/bin/env python
import pygame
from time import sleep
from threading import Timer
from mfrc522 import SimpleMFRC522
from models.book import Book

class StoryBook:
    # BOOK_DIRECTORY = '/home/pi/ellie_pi/book_files/'
    BOOK_DIRECTORY = '/home/pi/projects/Pi_StoryBook/book_files/'
    book_has_started_playing = False 

    def __init__(self):
        print('StoryBook Initialized!')
        self.rfid_reader = SimpleMFRC522()
        pygame.mixer.init()
        self.main()

    def main(self):
        """
        While true
            # Continuously watch RFID card reader
            
            if card is being read
                # If no audio is playing
                if not is_playing_audio()
                    get id and book name off of card

                    if valid id/card data
                        play audio book
                else
                    continue
            if card is not being read
                if is_playing_audio()
                    stop playing audio
                else
                    continue
        """
        # TODO: Create button to check when to start/stop program? Or maybe pause audio?
        # TODO: When card is removed store book and timestamp on the pi so user can start from when they left off?
        try:
            print('Watching for rfid card!')
            while True:
                pause_audio_timer = Timer(2.0, self.pause_audio)

                if self.is_playing_audio():
                    pause_audio_timer.start()

                # NOTE: Because this blocks the main thread the audio book will stop if no rfid card is present
                bookData = self.read_rfid_card()
                
                if not self.book_has_started_playing:
                    self.play_audio(bookData.name)
                else:
                    self.unpause_audio()

                pause_audio_timer.cancel()
                
        except KeyboardInterrupt:
            print("\nStopping due to keyboard interruption")
        finally:
            pass
            # TODO: Implement this if necessary
            # GPIO.cleanup()

    """
    Loads and plays audio at specified file path

    :param audio_file_name: Audio file name
    :return void: 
    """
    def play_audio(self, audio_file_name):
        try:
            print('play_audio called')
            # Load Music
            pygame.mixer.music.load(self.BOOK_DIRECTORY + audio_file_name)
            # Play Music
            pygame.mixer.music.play()
            self.book_has_started_playing = True
        except:
            raise Exception('Error while playing audio')
        finally:
            pass

    """
    Stops audio currently being played with pygame

    :return void: 
    """
    def stop_audio(self):
        try:
            print('stop_audio called')
            # Stop Music
            pygame.mixer.music.stop()
        except:
            raise Exception('Error while stopping audio')
        finally:
            pass

    """
    Pauses audio currently being played with pygame

    :return void: 
    """
    def pause_audio(self):
        try:
            print('pause_audio called')
            # Pause Music
            pygame.mixer.music.pause()
        except:
            raise Exception('Error while pausing audio')
        finally:
            pass

    """
    Unpauses audio currently being played with pygame

    :return void: 
    """
    def unpause_audio(self):
        try:
            print('unpause_audio called')
            # Unpause Music
            pygame.mixer.music.unpause()
        except:
            raise Exception('Error while unpausing audio')
        finally:
            pass

    """
    Returns true if pygame is playing audio, otherwise false
    NOTE: RETURNS TRUE EVEN IF AUDIO IS PAUSED

    :return boolean: 
    """
    def is_playing_audio(self):
        print('is_playing_audio called')
        return pygame.mixer.music.get_busy()

    """
    Returns dictionary with id and book name that exists on card
    NOTE: Calling read() on the rfid reader block main threads

    :return Book: 
    """
    def read_rfid_card(self):
        try:
            print('read_rfid_card called')
            id, book = self.rfid_reader.read()
            print("id: " + str(id))
            print ("book: " + book)
            return Book(id, book)
        except:
            raise Exception('Error reading id and book name')
        finally:
            pass
    
if __name__ == "__main__":
    StoryBook()
