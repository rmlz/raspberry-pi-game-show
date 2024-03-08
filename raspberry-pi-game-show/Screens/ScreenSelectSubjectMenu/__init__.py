from Screens.Screen import Screen
from Screens.ScreenQuestions import ScreenQuestions
import constants as c


class SelectSubjectMenu(Screen):
    def __init__(self, window, pygame):
        super().__init__("Seleção de Matérias", window, pygame)
        self.window = window
        self.subjects = ["Biologia"]
        self.font = self.pygame.font.Font(None, 36)
        self.next_screen = None

    def on_event(self, event):
        if self.next_screen:
            return self.next_screen
        return self

    def on_loop(self):
        pass

    def draw_text(self, text, color, x, y):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.window.blit(text_surface, text_rect)

    def draw_buttons(self):
        button_height = 50
        button_width = 200
        button_padding = 20
        y = 200
        for idx, subject in enumerate(self.subjects):
            rect = self.pygame.Rect(self.width // 2 - button_width // 2, y, button_width, button_height)
            if rect.collidepoint(self.pygame.mouse.get_pos()):
                self.pygame.draw.rect(self.window, c.BUTTON_COLOR_HOVER, rect)
                if self.pygame.mouse.get_pressed()[0]:
                    self.next_screen = ScreenQuestions(self.window, "Quantas pessoas verão isso?", self.pygame)

            else:
                self.pygame.draw.rect(self.window, c.BUTTON_COLOR_NORMAL, rect)
            self.draw_text(subject, c.BLACK, self.width // 2, y + button_height // 2)
            y += button_height + button_padding

    def on_render(self):
        # Limpa a tela
        self.window.fill(c.WHITE)

        # Desenha o texto de seleção de matérias
        self.draw_text("Selecione a matéria:", c.BLACK, self.width // 2, 100)

        # Desenha os botões das matérias
        self.draw_buttons()
