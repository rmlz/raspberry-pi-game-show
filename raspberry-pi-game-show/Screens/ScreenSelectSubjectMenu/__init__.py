import pygame

from Screens.Screen import Screen
import constants as c


class SelectSubjectMenu(Screen):
    def __init__(self, window):
        super().__init__("Seleção de Matérias", window)
        self.window = window
        self.subjects = ["Biologia"]
        self.font = pygame.font.Font(None, 36)

    def open_subject_screen(self, subject):
        # Aqui você pode adicionar lógica para abrir uma nova tela para a disciplina selecionada
        # Por enquanto, vamos apenas imprimir uma mensagem para demonstrar a funcionalidade
        print(f"Abrindo tela da disciplina de {subject}")

    def on_event(self, event):
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
            rect = pygame.Rect(self.width // 2 - button_width // 2, y, button_width, button_height)
            if rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.window, c.BUTTON_COLOR_HOVER, rect)
                if pygame.mouse.get_pressed()[0]:
                    # Aqui você pode definir a ação correspondente a cada disciplina
                    print(f"Você clicou em {subject}")
                    # Por exemplo, abrir uma nova tela para a disciplina selecionada
                    self.open_subject_screen(subject)
            else:
                pygame.draw.rect(self.window, c.BUTTON_COLOR_NORMAL, rect)
            self.draw_text(subject, c.BLACK, self.width // 2, y + button_height // 2)
            y += button_height + button_padding

    def on_render(self):
        # Limpa a tela
        self.window.fill(c.WHITE)

        # Desenha o texto de seleção de matérias
        self.draw_text("Selecione a matéria:", c.BLACK, self.width // 2, 100)

        # Desenha os botões das matérias
        self.draw_buttons()
