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

    engine = create_engine(CONN, echo=False)
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


for i in tabela.itertuples(index=False):
    print(i._26)


'''
x = Empresa(Originador=i.Originador,Doc_Originador=i._2,Cedente=i.Cedente,Doc_Cedente=i._4,
Ccb=i.CCB,Id=i.ID,Cliente=i.Cliente,Cpf_cnpj=i._8,Endereço=i.Endereço,Cep=i.CEP,
Cidade=i.Cidade,Uf=i.UF,Valor_do_Emprestimo=i._13,Taxa_de_juros=i._14,Parcela_em_reais=i._15,Principal=i._15,
Principal=i._16,Juros=i._17,Iof=i._18,Comissao=i._19,Total_parcelas=i._20,Parcelas=i._21,Multa=i.Multa,
Mora=i.Mora,Data_de_emissao=i._24,Data_de_vencimento=i._25,Data_de_compra=i._26,Preco_de_aquisicao=i._27)
session.add(x)
session.commit()
'''
