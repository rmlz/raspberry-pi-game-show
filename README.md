# Raspberry Game Show

[//]: # (![Project Image]&#40;project-image-url&#41;)

### Table of Contents

- [Description](#description)
- [How To Use](#how-to-use)
- [References](#references)
- [License](#license)
- [Author Info](#author-info)

---

## Description

This project is a answers and questions gameshow made with Pygame and Raspberry Pi. It is a fun way to learn and test your knowledge on a variety of topics.
The game is based on a popular brazilian show name Passa Ou Repassa.
#### Technologies
- Python 3.11
- Pygame

[Back To The Top](#read-me-template)

---

## How To Use

#### Installation
If you are not regular with Python projects, you can follow the steps below to install the project on your Raspberry Pi.

1. Clone the project
```html
    git clone git@github.com:rmlz/raspberry-pi-game-show.git
```

2. Install the dependencies
```html
    pip install -r requirements.txt
```

3. Run the game
```html
    python3 app.py
```

This simple steps will install the project on your Raspberry Pi and you will be able to play the game.

#### Adding Questions
The game has only a few questions as examples. You can add more questions to the game by adding them to the questions.py file.
```python
# before adding the questions, you need to add the subject to the subjects list.
subjects = [
    "Biologia"
]

# the questions array is where you will add the questions
questions = [
    Question("Biologia", "Qual a principal característica dos poríferos?", "Presença de poros"),
    Question("Biologia", "O que é dimorfismo sexual?", "Diferenças entre macho e fêmea")
]

# the Question class has the following parameters: subject, question and answer.
# add as many questions as you would like. Remember to separete them with a comma.
```

#### Game rules
The game has a few simple rules:
1. One player must be the game show presenter. The presenter will be responsible for reading the questions and answers 
and must be the only player to interact with the monitor. No other player should be able to see the questions and answers.
2. Divide the other players into the red team and the blue team.
3. Every round the presenter will ask a question. The players must press the button to answer it.
4. If a player press the button before the presenter read the question, the presenter must ask the player to give an 
answer even though the question was not fully read.
5. If the answer is correct, the player's team will score a point. If the answer is wrong, the other team will have the
   1. A fun way to play the game is by crafting chantily pies in styrofoam plates. If the answer is correct, the player
   rub one of them in the other player's face. If the answer is wrong, the player will have the pie rubbed in their face.

#### Game controls
The game has only two buttons. One for the red team and one for the blue team. 
For this project, I have crafted a simple controller using a zero delay usb controller board and two buttons.

>Once I have the schematics done, I will add it to the project.

## License

MIT License

Copyright (c) [2017] [James Q Quick]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Back To The Top](#read-me-template)

---

## Author Info

- Linkedin - [Ramon Barros](https://www.linkedin.com/in/ramon-pinto-de-barros-a4527a72/)

[Back To The Top](#read-me-template)
