from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


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


class Empresa(Base):
    __tablename__ = "Empirica"
    id = Column(Integer, primary_key=True)
    Originador = Column(String(50))
    Doc_Originador = Column(String(50))
    Cedente = Column(String(50))
    Doc_Cedente = Column(String(50))
    Ccb = Column(String(50))
    Id_cliente = Column(String(50))
    Cliente = Column(String(50))
    Cpf_cnpj = Column(String(50))
    Endereço = Column(String(50))
    Cep = Column(String(50))
    Cidade = Column(String(50))
    Uf = Column(String(50))
    Valor_do_emprestimo = Column(Integer)
    Taxa_de_juros = Column(Integer)
    Parcela_em_reais = Column(Integer)
    Principal = Column(Integer)
    Juros = Column(Integer)
    Iof = Column(Integer)
    Comissao = Column(Integer)
    Total_parcelas = Column(Integer)
    Parcelas = Column(Integer)
    Multa = Column(Integer)
    Mora = Column(Integer)
    Data_de_emissao = Column(String(10))
    Data_de_vencimento = Column(String(10))
    Data_de_compra = Column(String(10))
    preco_de_aquisicao = Column(Integer)
    



Base.metadata.create_all(engine)
