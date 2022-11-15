import pandas as pd
from bd import Empresa
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def RetornaSession():
    USUARIO = "root"
    SENHA = ""
    HOST = "localhost"
    BANCO = "testepython"
    PORT = "3306"

    CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base = declarative_base()
    return Session()


session = RetornaSession()


def transformar_padrao_data(dataframe, nome_coluna):

    dataframe[nome_coluna] = pd.to_datetime(dataframe[nome_coluna], format='%d/%m/%Y')

    return dataframe


def tirar_mascara(dataframe, nome_coluna):

    dataframe[nome_coluna] = dataframe[nome_coluna].apply(lambda x: str(x).replace(".","").replace("/","").replace("-",""))

    return dataframe



#lista de nome na planilha
titulos = ['Originador','_1','Cedente','_3','CCB','Id','Cliente','_7','Endereço','CEP','Cidade','UF','_12','_13',
                '_14','_15','_16','_17','_18','_19','_20','Multa','Mora','_23','_24','_25','_26']


#lista de nomes no banco de dados
titulos_bd= ['Originador','Doc_Originador','Cedente','Doc_Cedente','Ccb','Id_cliente','Cliente','Cpf_cnpj','Endereço','Cep',
    'Cidade','Uf','Valor_do_emprestimo','Taxa_de_juros','Parcela_em_reais','Principal','Juros','Iof','Comissao','Total_parcelas',
    'Parcelas','Multa','Mora','Data_de_emissao','Data_de_vencimento','Data_de_compra','preco_de_aquisicao']



def Insert_bd(datafram,nome_coluna_planilha,nome_coluna_bd):

    for i in datafram[nome_coluna_planilha]:
        x = Empresa(nome_coluna_bd=i)
    
    session.add(x)
    session.commit()
