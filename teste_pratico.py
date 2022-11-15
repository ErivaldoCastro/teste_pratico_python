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

#Savar no banco de dados
for i in tabela.itertuples(index=False):

    x = Empresa(Originador=i.Originador,Doc_Originador=i._1,Cedente=i.Cedente,Doc_Cedente=i._3,
    Ccb=i.CCB,Id_cliente=i.Id,Cliente=i.Cliente,Cpf_cnpj=i._7,Endereço=i.Endereço,Cep=i.CEP,
    Cidade=i.Cidade,Uf=i.UF,Valor_do_emprestimo=i._12,Taxa_de_juros=i._13,Parcela_em_reais=i._14,
    Principal=i._15,Juros=i._16,Iof=i._17,Comissao=i._18,Total_parcelas=i._19,Parcelas=i._20,Multa=i.Multa,
    Mora=i.Mora,Data_de_emissao=i._23,Data_de_vencimento=i._24,Data_de_compra=i._25,preco_de_aquisicao=i._26)
    session.add(x)
    session.commit()



