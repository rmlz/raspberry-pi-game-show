import random

from Screens.Screen import Screen
from Screens.ScreenQuestions import ScreenQuestions
import constants as c


class ScreenQuestionLottery(Screen):
    def __init__(self, window, pygame, lottery, previous_screen):
        super().__init__("CARREGANDO", window, pygame, previous_screen)
        self.rotation_angle = 0
        self.font = pygame.font.Font(None, 48)
        self.lottery = lottery
        self.next_screen = None

        # start fake loading timer
        self.seconds_left = random.randint(2, 3)
        self.clock = pygame.time.Clock()
        self.timer_event = pygame.USEREVENT + 1
        self.timer_started = False
        self.timer_interval = 1000

    def on_init(self):
        pass

    def draw(self):
        self.draw_loading()

    def draw_loading(self):
        self.window.fill((255, 255, 255))

        # Desenha a mensagem "Carregando..."
        text = self.font.render("Sorteando pergunta...", True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
        self.window.blit(text, text_rect)

        # Desenha o círculo de progresso indeterminado
        self.pygame.draw.arc(self.window, c.BLACK, (self.width // 2 - 100, self.height // 3, 200, 100),
                             self.rotation_angle, self.rotation_angle +
                             3.14, 3)
        self.rotation_angle += 0.1
        if self.rotation_angle >= 6.28:
            self.rotation_angle = 0

    def on_event(self, event):
        if not self.timer_started:
            self.timer_started = True
            self.pygame.time.set_timer(self.timer_event, self.timer_interval)
        if self.seconds_left == 0:
            self.next_screen = ScreenQuestions(self)
        if event.type == self.timer_event and self.seconds_left > 0:
            self.seconds_left -= 1
        if not self.next_screen:
            return self
        return self.next_screen

    def on_render(self):
        self.draw()
