import constants as c


class Screen:
    def __init__(self, window_title, window, width=c.WINDOW_WIDTH, height=c.WINDOW_HEIGHT):
        self.size = self.width, self.height = width, height
        self.window_title = window_title
        self.window = window

    def on_init(self):
        pass

    # if event.type == pygame.QUIT:
    # self._running = False
    def on_event(self, event):
        pass

    def on_render(self, window):
        pass
