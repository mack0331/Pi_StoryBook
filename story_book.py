#!/usr/bin/env python
import pygame

class StoryBook:
    BOOK_DIRECTORY = '/home/pi/ellie_pi/'

    def __init__(self):
        print('StoryBook Initialized!')
        pygame.mixer.init()

    """
    Plays audio at specified file path

    :param path_to_audio_file: Path to audo file to play
    :return void: 
    """
    # TODO: Instead of path to file, just have file name?
    def play_audio(self, path_to_audio_file):
        print('play_audio called')
        raise Exception('Not Yet Implemented')

    def stop_audio(self):
        print('stop_audio called') 
        raise Exception('Not Yet Implemented')

    def is_playing_audio(self):
        return pygame.mixer.music.get_busy()