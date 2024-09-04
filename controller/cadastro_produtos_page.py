from qt_core import*
from model.produto import Produto
from model.produtos_dao import adicionar_prod, listar_prod

FILE_UI = "view/cadastro_prod_page.ui"

class CadastroProdPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI,self)

        #Evento dos botões
        self.salvar_btn.clicked.connect(self.salvar_produto)

    def limpar_campos(self):
        self.nome.setText("")
        self.tipo.setText("")
        self.preco.setText("")
        self.estoque.setText("")
    def salvar_produto(self):
        nome = self.nome.text()
        tipo = self.tipo.text()
        preco = self.preco.text()
        estoque = self.estoque.text()
        novo_produto = Produto(None,nome,tipo,preco,estoque)
        adicionar_prod(novo_produto)

        self.limpar_campos()