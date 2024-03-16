import sys

import pygame.event
import constants as c
from Screens.ScreenSelectSubjectMenu import SelectSubjectMenu


class App:
    def __init__(self):
        self.current_screen = None
        self.size = self.width, self.height = c.WINDOW_WIDTH, c.WINDOW_HEIGHT
        self.window_title = ""
        self.window = None
        self.font = None
        self._running = False


    def on_init(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.window_title)
        self.font = pygame.font.Font(None, 36)
        self.current_screen = SelectSubjectMenu(self.window, pygame)
        self._running = True

    # if event.type == pygame.QUIT:
    # self._running = False
    def on_event(self, event):
        self.current_screen = self.current_screen.on_event(event)

    def on_loop(self):
        pass

    def on_render(self):
        self.current_screen.on_render()

    def on_cleanup(self):
        pass

    def on_execute(self):
        if not self._running:
            self.on_init()

        clock = pygame.time.Clock()

        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.on_event(event)

            self.on_render()

            pygame.display.flip()
            clock.tick(60)


if __name__ == "__main__":
    app = App()
    app.on_execute()
