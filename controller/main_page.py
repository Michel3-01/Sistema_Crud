from qt_core import*
from controller.produdos_main_window import ProdutosMain
from controller.vendas_main_window import VendasMain
#Arquivo .ui
FILE = "view/main_page.ui"
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE,self)


        #Evento dos botões
        self.produtos_btn.clicked.connect(self.show_produtos)
        self.vendas_btn.clicked.connect(self.show_vendas)
    def show_produtos(self):
        self.painel_principal.setCurrentIndex(0)
        self.painel_principal.insertWidget(0,ProdutosMain())
    def show_vendas(self):
        self.painel_principal.setCurrentIndex(1)
        self.painel_principal.insertWidget(1,VendasMain())
        