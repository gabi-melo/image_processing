import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

##Queremos criar uma Tabela Global com
##1- número de classes; 2- total de imagens; 3- tamanho da base; e 4- resolução das imagens

#Não sei criar uma tabela ainda, mas consigo obter 1- e 2- assim

#Ler metadados
metadata = pd.read_excel('./image_processing/EP1/metadata.xlsx')

#Dados pra tabela
metadata.groupby('classe').count().shape[0] #1- número de classes
metadata.groupby('classe')['exemplo'].count() #número de imagens por classe
metadata.groupby('classe').count()['exemplo'].sum() #2- total de imagens
#3-
#Padronizamos as resoluções aí só pegamos uma imagem como exemplo pra dar a resolução
#4-

##Tabela Detalhada

#Consigo produzir cada número de exemplos, fundos, repetições e locais
#mas não em tabela

metadata.groupby('classe')['exemplo'].unique() #quantos exemplos
metadata.groupby('classe')['periodo'].unique() #períodos
metadata.groupby('classe')['local'].unique() #locais
metadata.groupby('classe')['fundo'].unique() #fundos
metadata.groupby('classe')['repeticao'].unique() #número de repetições