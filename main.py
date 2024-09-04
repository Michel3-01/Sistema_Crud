from qt_core import*
from controller.main_page import MainWindow


app = QApplication(sys.argv)
win = MainWindow()

win.show()
app.exec()