import Question
from Screens.Screen import Screen
from Screens.ScreenQuestionLottery import ScreenQuestionLottery
import constants as c
from Question import QuestionLottery
import questions as q


class SelectSubjectMenu(Screen):
    def __init__(self, window, pygame):
        super().__init__("Seleção de Matérias", window, pygame)
        self.window = window
        self.subjects = q.subjects
        self.font = self.pygame.font.Font(None, 36)
        self.next_screen = None

    def on_event(self, event):
        if self.next_screen:
            new_screen = self.next_screen
            self.next_screen = None
            return new_screen
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
                    lottery = QuestionLottery(q.get_questions(subject))
                    self.next_screen = ScreenQuestionLottery(self.window, self.pygame, lottery, self)

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
