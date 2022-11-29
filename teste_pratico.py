import pandas as pd
from funcoes import transformar_padrao_data,tirar_mascara




tabela = pd.read_csv(r'arquivo_exemplo.csv', encoding = "ISO-8859-1", sep=';')

print(tabela)
#Alterar formato da data para padrão EUA
transformar_padrao_data(tabela,'Data de Emissão')
transformar_padrao_data(tabela,'Data de Vencimento')
transformar_padrao_data(tabela,'Data de Compra CCB')


#Tirar as mascaras CPF/CNPJ
tirar_mascara(tabela,'CPF/CNPJ')


tabela_depara = pd.read_excel(r"C:\Users\eriva\Documents\GitHub\teste_csv\depara.xlsx")

tabela_csv = tabela_depara['Unnamed: 1'][3:22]

tabela_banco = tabela_depara['Unnamed: 2'][3:22]


print(tabela_banco)


#Savar no banco de dados
'''
for i in tabela.itertuples(index=False):
    
    x = Empresa(ORIGINADOR=i.Originador,DOC_ORIGINADOR=i._1,CEDENTE=i.Cedente,DOC_CEDENTE=i._3,
    CCB=i.CCB,ID_EXTERNO=i.Id,CLIENTE=i.Cliente,CPF_CNPJ=i._7,ENDERECO=i.Endereço,CEP=i.CEP,
    CIDADE=i.Cidade,UF=i.UF,VALOR_DO_EMPRESTIMO=i._12,VALOR_PARCELA=i._14,
    TOTAL_PARCELAS=i._19,PARCELA=i._20,DATA_DE_EMISSAO=i._23,DATA_DE_VENCIMENTO=i._24,PRECO_DE_AQUISICAO=i._26)
    session.add(x)
    session.commit()
        
'''


