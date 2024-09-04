from qt_core import*
from controller.cadastro_produtos_page import CadastroProdPage
from controller.produtos_listar_page import ListarProdPage
#Arquivo tipo ui
FILE_UI = "view/produtos_tela_principal.ui"

class ProdutosMain(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI,self)


        self.cadastrar_btn.clicked.connect(self.show_cadastrar)
        self.listar_btn.clicked.connect(self.show_listar)

    def show_cadastrar(self):
        self.painel_produtos.setCurrentIndex(0)
        self.painel_produtos.insertWidget(0,CadastroProdPage())
    def show_listar(self):
        self.painel_produtos.setCurrentIndex(1)
        self.painel_produtos.insertWidget(1,ListarProdPage(self))