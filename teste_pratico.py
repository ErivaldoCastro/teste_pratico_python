import pandas as pd
from funcoes import transformar_padrao_data,tirar_mascara
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from bd import Empresa

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



tabela = pd.read_csv(r'arquivo_exemplo.csv', encoding = "ISO-8859-1", sep=';')


#Alterar formato da data para padrão EUA
transformar_padrao_data(tabela,'Data de Emissão')
transformar_padrao_data(tabela,'Data de Vencimento')
transformar_padrao_data(tabela,'Data de Compra CCB')


#Tirar as mascaras CPF/CNPJ
tirar_mascara(tabela,'CPF/CNPJ')


#Salvar Banco de dados


