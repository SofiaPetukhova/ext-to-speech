import pyttsx3
engine = pyttsx3.init()

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QVBoxLayout,QPushButton
app = QApplication([])
win = QWidget()
win.setWindowTitle('text-to-speech')
win.move(300, 20)
win.resize(300,300)
win.show()

main_layout = QVBoxLayout()
win.setLayout(main_layout)

text = QTextEdit()
main_layout.addWidget(text)


button = QPushButton("СКАЗАТЬ")
main_layout.addWidget(button)

def say():
    text_to_say = text.toPlainText()
    engine.say("I will speak this text")
    engine.runAndWait()

button.clicked.connect(say)

app.exec_()

text = QTextEdit()
main_layout.addWidget(text)
def say():
    text_to_say = text.toPlainText()
    engine.say(text_to_say)
    engine.runAndWait()