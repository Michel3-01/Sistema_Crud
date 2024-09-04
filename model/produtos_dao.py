#Funções dao
from model import database_prod
from model.produto import Produto 
lista = []
def adicionar_prod(novo_produto):
    try:
        conn = database_prod.connect_produto()
        cursor = conn.cursor()
        sql = """ INSERT INTO Produtos (nome,tipo,preco,estoque,excluir) VALUES (?,?,?,?,0);"""
        cursor.execute(sql,novo_produto.getProd())
        conn.commit()
    except Exception as e:
        print("Deu erro :",e)
    finally:
        conn.close()
def listar_prod():
    lista = []
    try:
        conn = database_prod.connect_produto()
        cursor = conn.cursor()
        sql = """SELECT * FROM Produtos WHERE excluir = 0;"""
        cursor.execute(sql)
        linhas = cursor.fetchall()
        for produto in linhas:
            id = produto[0]
            nome = produto[1]
            tipo = produto[2]
            preco = produto[3]
            estoque = produto[4]
            excluir = produto[5]

            novo_produto = Produto(id,nome,tipo,preco,estoque,excluir)
            lista.append(novo_produto)
    except Exception as e:
        print("deu erro: ",e)
    finally:
        conn.close()
    return lista

def excluir_prod(id):
    pass
def editar_prod(id):
    pass