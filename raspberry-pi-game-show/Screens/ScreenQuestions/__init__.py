from Screens.Screen import Screen
import constants as c


class ScreenQuestions(Screen):
    def __init__(self, screen_lottery):
        super().__init__("PERGUNTA", screen_lottery.window, screen_lottery.pygame, screen_lottery)
        # screen data
        self.next_screen = None
        self.screen_lottery = screen_lottery
        self.font = self.pygame.font.Font(None, 36)
        self.timer_font = self.pygame.font.Font(None, 24)

        # chronometer data
        self.seconds_left = c.TIME_LEFT_IN_SECONDS
        self.clock = self.pygame.time.Clock()
        self.question = self.screen_lottery.lottery.get_question()
        self.timer_event = self.pygame.USEREVENT + 1
        self.timer_started = False
        self.timer_interval = 1000

        # joystick data
        self.joystick = self.pygame.joystick.Joystick(0)
        self.joystick.init()
        self.red_pressed = False
        self.blue_pressed = False

        # sound data
        self.pressed_sound = self.pygame.mixer.Sound('assets/sound/correct_sound_effect.mp3')

    def on_event(self, event):
        if event.type == self.pygame.JOYHATMOTION:
            x, y = event.value
            if x == -1:
                print('left')
                self.red_pressed = True
                self.seconds_left = 0
                self.pressed_sound.play()
            elif x == 1:
                print('right')
                self.blue_pressed = True
                self.seconds_left = 0
                self.pressed_sound.play()
        if not self.timer_started:
            self.timer_started = True
            self.pygame.time.set_timer(self.timer_event, self.timer_interval)
        if event.type == self.timer_event and self.seconds_left > 0:
            self.seconds_left -= 1
        if not self.next_screen:
            return self
        return self.next_screen

    def on_loop(self):
        pass

    def draw_text(self, text, color, x, y):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.window.blit(text_surface, text_rect)

    def draw_question(self):
        # Desenha a pergunta
        text = self.font.render(self.question.question, True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.width / 2, 200))
        self.window.blit(text, text_rect)

    def draw_answer(self):
        text = self.font.render(self.question.answer, True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.width / 2, 400))
        self.window.blit(text, text_rect)

    def draw_countdown(self):
        # Desenha o contador regressivo
        timer_text = self.timer_font.render(f"Tempo restante: {self.seconds_left}", True, (150, 150, 0))
        timer_rect = timer_text.get_rect(center=(self.width / 2, 300))
        self.window.blit(timer_text, timer_rect)

    def draw_buttons(self):
        self.draw_continue_button()
        self.draw_retry_button()
        self.draw_close_button()

    def draw_continue_button(self):
        button_height = 50
        button_width = 200
        button_padding = 20
        y = 450
        y += button_height + button_padding

        button_continue = self.pygame.Rect(self.width // 4 - button_width // 2, y, button_width, button_height)
        if button_continue.collidepoint(self.pygame.mouse.get_pos()):
            self.pygame.draw.rect(self.window, c.BUTTON_COLOR_HOVER, button_continue)
            if self.pygame.mouse.get_pressed()[0]:
                self.return_previous_screen()
        else:
            self.pygame.draw.rect(self.window, c.BUTTON_COLOR_NORMAL, button_continue)

        self.draw_text("CONTINUAR", c.BLACK, self.width // 4, y + button_height // 2)

    def draw_retry_button(self):
        button_height = 50
        button_width = 200
        button_padding = 20
        y = 450
        y += button_height + button_padding

        button_retry = self.pygame.Rect(self.width // 1.5 - button_width // 2, y, button_width, button_height)
        if button_retry.collidepoint(self.pygame.mouse.get_pos()):
            self.pygame.draw.rect(self.window, c.BUTTON_COLOR_HOVER, button_retry)
            if self.pygame.mouse.get_pressed()[0]:
                self.seconds_left = c.TIME_LEFT_IN_SECONDS
                self.restart_parameters()
        else:
            self.pygame.draw.rect(self.window, c.BUTTON_COLOR_NORMAL, button_retry)

        self.draw_text("REPETIR", c.BLACK, self.width // 1.5, y + button_height // 2)

    def restart_parameters(self):
        self.timer_started = False
        self.joystick.init()
        self.red_pressed = False
        self.blue_pressed = False
    def draw_close_button(self):
        # Posição e tamanho do botão
        button_size = 30
        button_margin = 10
        button_x = self.width - button_size - button_margin
        button_y = button_margin

        # Desenha o retângulo do botão
        button_close = self.pygame.Rect(button_x, button_y, button_size, button_size)
        self.pygame.draw.rect(self.window, c.BLACK, (button_x, button_y, button_size, button_size))
        self.pygame.draw.line(self.window, c.WHITE, (button_x + 5, button_y + 5), (button_x + button_size - 5, button_y
                                                                                   + button_size - 5), 2)
        self.pygame.draw.line(self.window, c.WHITE, (button_x + button_size - 5, button_y + 5), (button_x + 5, button_y
                                                                                                 + button_size - 5), 2)

        if button_close.collidepoint(self.pygame.mouse.get_pos()):
            if self.pygame.mouse.get_pressed()[0]:
                self.next_screen = self.previous_screen.previous_screen

    def on_render(self):
        # Limpa a tela
        self.window.fill(c.WHITE)
        if self.seconds_left == 0:
            if self.blue_pressed:
                self.window.fill(c.BLUE)
                self.joystick.quit()
            elif self.red_pressed:
                self.window.fill(c.RED)
                self.joystick.quit()
            self.draw_answer()

        # Desenha o texto da pergunta
        self.draw_question()


        # Desenha o contador regressivo
        self.draw_countdown()

        if self.seconds_left == 0:
            self.draw_buttons()
