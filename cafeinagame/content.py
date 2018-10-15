import pygame, sys, os
from pygame.locals import *

# Content Manager
class Content:
    # Builds a Content Manager to a relative path
    def __init__(self, path):
        self.path = path

    # Tries to load an image
    # colorkey: -1, (255,255,255), None
    def load_image(self, name, colorkey=None, scale=1,):
        fullname = os.path.join(self.path, name)
        try:
            image = pygame.image.load(fullname)
        except pygame.error(message):
            print("Cannot load image:", name)
            raise SystemExit(message)
        # Apply color key
        image = image.convert()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, RLEACCEL)
            
        # Scale image
        if scale == 2:
            image = pygame.transform.scale2x(image)
        elif scale > 2:
            width = image.get_width()* scale
            height = image.get_height() * scale
            image = pygame.transform.smoothscale(image, (width, height))                         
        
        return image

    # Tries to load a sound
    def load_sound(self, name):
        class NoneSound:
            def play(self): pass
        if not pygame.mixer:
            return NoneSound()
        fullname = os.path.join(self.path, name)
        try:
            sound = pygame.mixer.Sound(fullname)
        except pygame.error(message):
            print("Cannot load sound:", wav)
            raise SystemExit(message)
        return sound

    # Loads a set of images
    def load_images(self, array):
        images = []
        for item in array:
            if len(item) == 1:
                images.append(self.load_image(item[0]))
            else:
                images.append(self.load_image(item[0], item[1]))
        return images
