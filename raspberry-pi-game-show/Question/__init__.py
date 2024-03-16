import random


class Question:
    def __init__(self, subject, question, answer):
        self.subject = subject
        self.question = question
        self.answer = answer

    def __str__(self):
        return f"{self.subject}: {self.question}\nResposta: {self.answer}"

    def __repr__(self):
        return f"{self.subject}: {self.question}\nResposta: {self.answer}"


class QuestionLottery:
    def __init__(self, questions):
        self.questions = questions
        random.shuffle(self.questions)

    def get_question(self):
        if not self.questions:
            return Question("Fim", "Fim", "Obrigado por jogar!")
        question = self.questions[0]
        self.remove_question()
        return question

    def remove_question(self):
        self.questions.pop(0)
