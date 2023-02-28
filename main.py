import sys
from PyQt5.QtWidgets import QApplication, QWidget




app = QApplication(sys.argv)

w = QWidget()
w.resize(1080, 720)
w.move(120, 120)
w.setWindowTitle('Tesla charger map')
w.show()

sys.exit(app.exec_())