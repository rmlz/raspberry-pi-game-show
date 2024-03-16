import constants as c


class Screen:
    def __init__(self, window_title, window, pygame, previous_screen=None, width=c.WINDOW_WIDTH, height=c.WINDOW_HEIGHT):
        self.size = self.width, self.height = width, height
        self.window_title = window_title
        self.window = window
        self.pygame = pygame
        self.next_screen = None
        self.previous_screen = previous_screen

    def on_init(self):
        pass

    # if event.type == pygame.QUIT:
    # self._running = False
    def on_event(self, event):
        pass

    def on_render(self):
        pass

    def return_previous_screen(self):
        if self.previous_screen:
            self.next_screen = self.previous_screen
