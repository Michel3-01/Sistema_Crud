from qt_core import *

FILE_UI = "view/novaVenda_page.ui"

class NovaVendaPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI,self)

        data = self.dateEdit.text()
        time = self.timeEdit.text()
        print(type(data))
        print(type(time))