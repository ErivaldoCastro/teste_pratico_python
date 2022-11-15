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

    ID_CESSAO = Column(Integer, primary_key=True)
    ORIGINADOR = Column(String(250))
    DOC_ORIGINADOR = Column(Integer)
    CEDENTE = Column(String(250))
    DOC_CEDENTE =  Column(Integer)
    CCB = Column(Integer)
    ID_EXTERNO = Column(Integer)
    CLIENTE = Column(String(250))
    CPF_CNPJ = Column(String(50))
    ENDERECO = Column(String(250))
    CEP = Column(String(50))
    CIDADE = Column(String(250))
    UF = Column(String(50))
    VALOR_DO_EMPRESTIMO = Column(Integer)
    VALOR_PARCELA = Column(Integer)
    TOTAL_PARCELAS = Column(Integer)
    PARCELA = Column(Integer)
    DATA_DE_EMISSAO = Column(Integer)
    DATA_DE_VENCIMENTO = Column(Integer)
    PRECO_DE_AQUISICAO = Column(Integer)


Base.metadata.create_all(engine)
