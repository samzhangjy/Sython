import pygame
from pygame.locals import *
import threading
from .events.events_base import BaseEvents
import os

# The current sprites list
SPRITE_LIST = []

# Events happening at this frame
events = []

class Sprite(BaseEvents):
    def __init__(self, name: str, img: pygame.Surface, screen: pygame.Surface, background: pygame.Surface) -> None:
        """Generates a Sython sprite.

        Args:
            name (str): The name of the sprite.
            img (pygame.Surface): The image to display.
            screen (pygame.Surface): The screen object of `sython.Window.screen`.
            background (pygame.Surface): The background object of `sython.Window.background`.
        """
        super().__init__()
        self.img = img
        self.pos = img.get_rect()
        self.screen = screen
        self.background = background
        self.visible = True
        self.name = name
        SPRITE_LIST.append(self)
    
    def show(self) -> None:
        """Show the current sprite.

        This method simply changes the `sython.Sprite.visible` property to True for the 
        ease of use.
        """
        self.visible = True
    
    def hide(self) -> None:
        """Hide the current sprite.

        This method simply changes the `sython.Sprite.visible` property to False for the 
        ease of use.
        """
        self.visible = False
    
    def move_to(self, x: int, y: int) -> None:
        """Move the current sprite to (x, y), without animation.

        Args:
            x (int): The horizontal ordinate of the target position.
            y (int): The ordinate of the target position.
        """
        self.screen.blit(self.background, (0, 0))
        self.pos = self.pos.move((x, y))
        self.screen.blit(self.img, self.pos)
        pygame.display.update()
    
    def _glide_to(self, x: int, y: int, time: int = 1000, frames: int = 40) -> None:
        """Glide the current sprite to (x, y), with animation.

        Note that this function is not async, so the main process will not execute after
        the animation ends. Use `sython.Sprite.glide_to` to do async gliding.

        Args:
            x (int): The horizontal ordinate of the target position.
            y (int): The ordinate of the target position.
            time (int, optional): The period of time to do the gliding animation. Defaults to 1000.
            frames (int, optional): The animation frame num. Defaults to 40.
        """
        if x < frames:
            frames = x
        if y < frames:
            frames = y
        for i in range(frames):
            self.screen.blit(self.background, (0, 0))
            for sprite in SPRITE_LIST:
                if sprite != self:
                    self.screen.blit(sprite.img, sprite.pos)
            self.pos = self.pos.move((float(x) / float(frames), float(y) / float(frames)))
            if self.visible:
                self.screen.blit(self.img, self.pos)
            pygame.display.update()
            pygame.time.delay(int(time / frames))
    
    def glide_to(self, x: int, y: int, time: int = 1000, frames: int = 40) -> None:
        """Glide the current sprite to (x, y), with animation.

        This method creates a new thread using `threading.Thread` to do async animations.
        The rest of the main process can be executed while doing the gliding animation.
        If you want to use unasync gliding, please use `sython.Sprite._glide_to`. However,
        it is not recommended to use unasync gliding.

        Args:
            x (int): The horizontal ordinate of the target position.
            y (int): The ordinate of the target position.
            time (int, optional): The period of time to do the gliding animation. Defaults to 1000.
            frames (int, optional): The animation frame num. Defaults to 40.
        """
        threading.Thread(target=self._glide_to, args=(x, y, time, frames)).start()
    
    def __repr__(self) -> str:
        return '<Sprite %s>' % self.name


class Window(object):
    def __init__(self, title: str = '') -> None:
        """Creates a new Sython Window object.

        Every program built with Sython must have at least one Window object.
        For example:

            >>> win = Window('Foo Program')
            >>> # Write your code here...
            >>> win.start()  # Starts the app

        Args:
            title (str, optional): The title of the created window. Defaults to ''.
        """
        super().__init__()
        pygame.init()
        self.SIZE = self.WINDOWWIDTH, self.WINDOWHEIGHT = 500, 250
        self.screen = pygame.display.set_mode(self.SIZE, RESIZABLE)
        pygame.display.set_caption(title)

        # Fill background
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((250, 250, 250))

        # Blit everything to the screen
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()
    
    def __update_background(self) -> None:
        """Updates the current window's background.

        This method will run when the background need to be re-blited.
        """
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((250, 250, 250))
        for sprite in SPRITE_LIST:
            sprite.background = self.background

    def start(self) -> None:
        """Starts the program's main loop.

        This function runs a loop to detect every event and do movements of the sprites.
        """
        # Event loop
        global events
        while True:
            clock = pygame.time.Clock()
            clock.tick(60)
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    return
                elif event.type == WINDOWRESIZED:
                    threading.Thread(target=self.__update_background).start()
            self.screen.blit(self.background, (0, 0))
            for sprite in SPRITE_LIST:
                sprite.handle_events()
                if sprite.visible:
                    self.screen.blit(sprite.img, sprite.pos)
            pygame.display.update()
    
    def add_sprite(self, name: str, img_path: str, size: tuple = (0, 0)) -> Sprite:
        """Adds a sprite to the window.

        This method adds a sprite to the current `sython.Window` object using
        `sython.Sprite`.

        Args:
            name (str): The name of the generated sprite.
            img_path (str): The image path of the generated sprite.
            size (tuple, optional): The display size of the image.
                Keeps the original size when equals to (0, 0). Defaults to (0, 0).

        Returns:
            Sprite: The generated `sython.Sprite` object.
        """
        img = pygame.image.load(img_path).convert_alpha()
        if not (size[0] == 0 and size[1] == 0):
            pygame.transform.scale(img, size)
        self.screen.blit(img, (0, 0))
        pygame.display.update()
        sprite = Sprite(name, img, self.screen, self.background)
        return sprite
