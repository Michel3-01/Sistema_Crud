from qt_core import *

FILE_UI ="view/cadProdutoPage.ui"

class cadProduto(QWidget):
    def __init__(self,produtos,janela_produto):
        super().__init__()
        uic.loadUi(FILE_UI,self)

        self.produtos = produtos
        self.janela_produto = janela_produto