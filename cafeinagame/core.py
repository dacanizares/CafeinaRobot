import pygame, sys, os
from pygame.locals import *

# Content Manager
class Content:
    # Builds a Content Manager to a relative path
    def __init__(self, path):
        self.path = path

    # Tries to load an image
    # colorkey: -1, (255,255,255), None
    def load_image(self, name, colorkey=None, scale=1):
        fullname = os.path.join(self.path, name)
        try:
            image = pygame.image.load(fullname)
        except pygame.error, message:
            print 'Cannot load image:', name
            raise SystemExit, message
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
        except pygame.error, message:
            print 'Cannot load sound:', wav
            raise SystemExit, message
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

# Game
class Game:
    # Inits game
    def __init__(self):
        print "Cafeinagame v0.2"
        print ""
        pygame.init()
        self.managed_entities = {}
        print "Game has been intialized"
           
    # Inits video
    def init_video(self, caption, width=800, height=640, fullscreen=False, fps=60):
        if fullscreen:
            pygame.display.set_mode((width, height), pygame.FULLSCREEN)
        else:
            pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        self.screen = pygame.display.get_surface()
        self.fullscreen = fullscreen
        self.active = True
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.time = 0
        self.width = width
        self.height = height
        self.valid_z_index = [10,9,8,7,6,5,4,3,2,1,0]

        background = pygame.Surface(self.screen.get_size())
        background = background.convert()
        background.fill((0, 0, 0))
        self.background = background      

        print "Video has been intialized"

    def get_events(self):
        return pygame.event.get()
    
    # Updates game
    def update(self):
        if not self.active:
            return      
        
        for z_index, entities in self.managed_entities.items():
            for entity in entities:
                entity.update(self.time)
    
    # Get keyboard events
    def get_keys(self):
        return [event for event in self.get_events() if event.type == KEYDOWN]

    # Clears all screen
    def clear(self):
        if not self.active:
            return
        self.screen.blit(self.background, (0, 0))

    # Draws all entities on a surface
    def draw_entities(self, surface):
        for z_index in self.valid_z_index:
            if z_index not in self.managed_entities:
                continue
            
            for entity in self.managed_entities[z_index]:                
                entity.draw(surface)
        
    # Draws all on a surface and scales it to current screen
    def draw(self, surface=None):
        if not self.active:
            return
        self.time = self.clock.tick(self.fps)
        
        if not surface:
            self.draw_entities(self.screen)
        else:
            self.draw_entities(surface)
            pygame.transform.scale(surface, (self.width, self.height), self.screen) 
        pygame.display.flip()

    # A complete gamecycle (update and draw)
    def gamecycle(self):
        self.update()
        self.draw()

    # Creates a finalize event
    def finalize_event(self):
        pygame.event.post(pygame.event.Event(QUIT))

    # Finalizes the game
    def finalize(self):
        pygame.quit()
        self.active = False
        self.events = []

    # Adds a new entity to the system
    def add_entity(self, entity, z_index):
        if z_index not in self.valid_z_index:
            print 'Invalid z_index'
            raise SystemExit
        
        entities = []
        if z_index in self.managed_entities:
            entities = self.managed_entities[z_index]

        entities.append(entity)
        self.managed_entities[z_index] = entities

    # Adds a list of entities
    def add_entities(self, entities, z_index):
        for entity in entities:
            self.add_entity(entity, z_index)
        
    
    _update = update
    _draw = draw
