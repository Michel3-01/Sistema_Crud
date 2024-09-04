from qt_core import *
from controller.nova_venda_page import NovaVendaPage

FILE_UI = "view/vendas_tela_principal.ui"

class VendasMain(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI,self)

        self.novaVenda_btn.clicked.connect(self.nova_venda)
    
    def nova_venda(self):
        self.painel_vendas.setCurrentIndex(0)
        self.painel_vendas.insertWidget(0,NovaVendaPage())