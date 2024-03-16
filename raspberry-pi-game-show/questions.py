from Question import Question

subjects = [
    "Biologia"
]

questions = [
    Question("Biologia", "Qual a principal característica dos poríferos?", "Presença de poros"),
    Question("Biologia", "O que é dimorfismo sexual?", "Diferenças entre macho e fêmea"),
    Question("Biologia", "Cite uma novidade evolutiva dos Nematoides.", "Sistema digestório completo"),
    Question("Biologia", "O que é um Pseudoceloma?", "Inicio da formação do celoma"),
    Question("Biologia", "Para que órgão a larva da esquistossomose migra depois de infectar o ser humano?", "Fígado"),
    Question("Biologia", "Que nome recebe a larva que entra na pele humana na esquistossomose?", "Cercaria"),
    Question("Biologia", "Como se chama o hospedeiro intermediário da esquistossomose?", "Caramujo"),
    Question("Biologia", "Como se chama a reprodução sexuada dos platelmintos?", "Fecundação cruzada"),
    Question("Biologia", "Como se chama a reprodução assexuada dos platelmintos?", "Fissão"),
    Question("Biologia", "O que são ocelos?", "Olhos primitivos"),
    Question("Biologia", "Qual o nome da célula responsável pela excreção nos Platelmintos?", "Células flama"),
    Question("Biologia", "Qual a principal diferença entre Platelmintos e Nematoides?",
             "Corpo achatado e corpo cilíndrico"),
    Question("Biologia", "O que significa ser acelomado?", "Sem cavidade no corpo"),
    Question("Biologia", "Como se chama a larva dos Cnidários?", "Plânula"),
    Question("Biologia", "Como se chama a forma séssil dos cnidários?", "Pólipo"),
    Question("Biologia", "Que nome recebe a reprodução assexuada dos cnidários?", "Brotamento"),
    Question("Biologia", "Qual o nome da principal célula dos cnidários?", "Cnidócitos"),
    Question("Biologia", "Como é feita a digestão dos Cnidários?", "Intra e extracelular"),
    Question("Biologia", "Qual o tipo de simetria dos Cnidários?", "Radial"),
    Question("Biologia", "Como são feitas as trocas gasosas, excreção e distribuição nos poríferos?", "Difusão"),
    Question("Biologia", "Qual o nome da principal célula dos poríferos?", "Conócitos"),
    Question("Biologia", "Qual o caminho que a água faz pelos poríferos?",
             "Entra pelos poros, sai no átrio e sai pelo ósculo"),
    Question("Biologia", "Verdadeiro ou falso. Os poríferos não apresentam tecidos verdadeiros.", "Verdadeiro"),
    Question("Biologia", "O que são indivíduos sesseis?", "Não se locomove, são fixos no substrato."),
]


def get_questions(selected_subject):
    return [q for q in questions if q.subject == selected_subject]


for subject in subjects:
    is_there_any_question_for_subject = False
    for question in questions:
        if question.subject == subject:
            is_there_any_question_for_subject = True
            break
    if not is_there_any_question_for_subject:
        raise Exception(
            f"Não há nenhuma questão para a matéria {subject}.\n Favor inserir ao menos uma questão no arquivo question.py")
