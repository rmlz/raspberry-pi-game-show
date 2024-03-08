from Screens.Screen import Screen
import constants as c


class ScreenQuestions(Screen):
    def __init__(self, window, question, pygame):
        super().__init__("PERGUNTA", window, pygame)
        self.window = window
        self.font = pygame.font.Font(None, 36)
        self.timer_font = pygame.font.Font(None, 24)
        self.seconds_left = 10
        self.clock = pygame.time.Clock()
        self.question = question
        self.timer_event = pygame.USEREVENT+1
        self.timer_started = False
        self.timer_interval = 1000

    def on_event(self, event):
        if not self.timer_started:
            self.timer_started = True
            self.pygame.time.set_timer(self.timer_event , self.timer_interval)
        if event.type == self.timer_event and self.seconds_left > 0:
            self.seconds_left -= 1
        return self

    def on_loop(self):
        pass

    def draw_text(self, text, color, x, y):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.window.blit(text_surface, text_rect)

    def draw_question(self):
        # Desenha a pergunta
        text = self.font.render(self.question, True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.width / 2, 200))
        self.window.blit(text, text_rect)

    def draw_countdown(self):
        # Desenha o contador regressivo
        timer_text = self.timer_font.render(f"Tempo restante: {self.seconds_left}", True, (255, 0, 0))
        timer_rect = timer_text.get_rect(center=(self.width / 2, 300))
        self.window.blit(timer_text, timer_rect)

    def draw_continue_button(self):
        button_height = 50
        button_width = 200
        button_padding = 20
        y = 550
        rect = self.pygame.Rect(self.width // 2 - button_width // 2, y, button_width, button_height)
        if rect.collidepoint(self.pygame.mouse.get_pos()):
            self.pygame.draw.rect(self.window, c.BUTTON_COLOR_HOVER, rect)

        else:
            self.pygame.draw.rect(self.window, c.BUTTON_COLOR_NORMAL, rect)
        self.draw_text("CONTINUAR", c.BLACK, self.width // 2, y + button_height // 2)
        y += button_height + button_padding

    def on_render(self):
        # Limpa a tela
        self.window.fill(c.WHITE)

        # Desenha o texto da pergunta
        self.draw_question()

        # Desenha o contador regressivo
        self.draw_countdown()

        if self.seconds_left == 0:
            self.draw_continue_button()
