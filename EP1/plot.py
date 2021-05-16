import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

##Queremos criar a visualização da base

#ler a base
metadata = pd.read_excel('./image_processing/EP1/metadata.xlsx')

#todos dados dos metadados
classe = metadata['classe'].unique()
exemplos = metadata['exemplo'].unique()
periodo = metadata['periodo'].unique()
fundos = metadata['fundo'].unique()

classe_x = np.array([classe[0], classe[1]]) #vamos usar apenas duas classes pro plot
exemplo_x = exemplos[0] #um exemplo
#antes de selecionar os fundos, checar se eles existem pra classe escolhida. Como?
#Tentei, não deu certo
fundo_x = np.array([fundos[0], fundos[1]]) #usar somente dois fundos

xx, yy, zz = np.meshgrid(classe_x, periodo, fundo_x)
xyz = np.dstack([xx, yy, zz]).reshape(-1, 2)

#to tentando criar uma forma de fazer todas combinações possíveis
#pra quando for selecionar as imagens pro plot, sair mais automático.
#faz sentido? Queria deixar num array [chinelo, dia, bege], no outro
#[chinelo, dia, azul] e assim por diante. Depois pra selecionar as imagens
#do arquivo, seria só criar um loop pra criar os nomes e ele pegar pra gente só essas que queremos.
#mas ainda não arrumei esse xyz como gostaria.