import numpy
import pandas as pd

def main():
    #importar_dados_movimentacao()
    #importar_dados_saldo()
    aprendendo_sqlalchemy()

def importar_dados_movimentacao():
    caminho_arquivo_movimentacao = "/workspaces/dom-rock-desafio/ambiente-desenvolvimento/projeto/projeto/dados/MovtoITEM.xlsx"
    dataframe_movimentacao = pd.read_excel(caminho_arquivo_movimentacao)
    print(dataframe_movimentacao)
    
def importar_dados_saldo():
    caminho_arquivo_saldo = "/workspaces/dom-rock-desafio/ambiente-desenvolvimento/projeto/projeto/dados/SaldoITEM.xlsx"
    dataframe_saldo = pd.read_excel(caminho_arquivo_saldo)
    print(dataframe_saldo)

def aprendendo_sqlalchemy():
    class Empresa(cnpj)
