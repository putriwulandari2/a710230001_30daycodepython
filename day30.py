import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        self.button1 = QPushButton('Klik')
        self.button1.setStyleSheet('background-color: navy; color: white;')
        self.button1.clicked.connect(self.button1Clicked)

        self.button2 = QPushButton('Klik')
        self.button2.setStyleSheet('background-color: grey; color: white;')
        self.button2.clicked.connect(self.button2Clicked)

        vbox.addWidget(self.button1)
        vbox.addWidget(self.button2)

        self.setLayout(vbox)
        self.setWindowTitle('Style Button')

    def button1Clicked(self):
        self.button1.setText('Haiii😊!')

    def button2Clicked(self):
        self.button2.setText('Happy Birthday🎉!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
