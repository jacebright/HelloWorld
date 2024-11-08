from time import sleep
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

def display_message(message, sound1, sound2):
    new_message = ''
    for character in message:
        new_message += character
        sound1.play()
        print(new_message, end='\r')
        sleep(.2)
    sound2.play()
    sleep(1)
    print(end='\n')

def main():
    pygame.mixer.init()
    key_sound = pygame.mixer.Sound("typewriter_key.wav")
    bell_sound = pygame.mixer.Sound("typewriter_bell.wav")
    display_message('Hello World!', key_sound, bell_sound)

if __name__ == "__main__":
    main()