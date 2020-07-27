#!/usr/bin/env python
import pygame
from mfrc522 import SimpleMFRC522
from models.book import Book

class StoryBook:
    BOOK_DIRECTORY = '/home/pi/ellie_pi/'

    def __init__(self):
        print('StoryBook Initialized!')
        pygame.mixer.init()
        self.rfid_reader = SimpleMFRC522()

    # TODO
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

    """
    Plays audio at specified file path

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
        except:
            raise Exception('Error while playing audio')
        finally:
            pass

    """
    Stops audio current being played with pygame

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
    Returns true if pygame is playing audio, otherwise false

    :return boolean: 
    """
    def is_playing_audio(self):
        return pygame.mixer.music.get_busy()

    """
    Returns dictionary with id and book name that exists on card

    :return dictionary: 
    """
    def read_rfid_card(self):
        try:
            print('read_rfid_card called')
            # NOTE: Is id a string or int
            id, book = self.rfid_reader.read()
            return Book(id, book)
        except:
            raise Exception('Error reading id and book name')
        finally:
            pass
    