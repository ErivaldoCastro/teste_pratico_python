import pandas as pd



def transformar_padrao_data(dataframe, nome_coluna):

    dataframe[nome_coluna] = pd.to_datetime(dataframe[nome_coluna], format='%d/%m/%Y')

    return dataframe


def tirar_mascara(dataframe, nome_coluna):

    dataframe[nome_coluna] = dataframe[nome_coluna].apply(lambda x: str(x).replace(".","").replace("/","").replace("-",""))

    return dataframe



