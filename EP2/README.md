# image_processing

# EP2

O EP2 tem como objetivo a criação de um dataset, baseado no conjunto de imagens coloridas originais, que apresente maior variação, por meio de Data Augmentation. Ele está dividido em duas partes.

Na primeira parte, primeiramente convertemos as imagens originais coloridas em imagens na escala de cinza, por meio da função RGB2Gray. Essas imagens formam o grayscaleDataset.
O grayscaleDataset passa outras transformações, para gerar novas variações. Estas transformações são: logaritmo, exponencial, soma da imagem com um gradiente, e a convolução com um filtro da média.
Essas transformações são salvas num novo dataset, o augmentedDataset.
O código da primeira parte do EP está no Jupyter Notebook EP2_augmentation.ipynb.

Na segunda parte do EP, as imagens do augmentedDataset passam por uma normalização, e formam um novo dataset, chamado normalizedDataset. A normalização é feita por meio de equalização de histogramas.
Nessa segunda parte, são feitas análises de todos os três datasets (grayscale, augmented e normalized), pela computação e apresentação do protótipo médio de cada classe de imagens, do histograma médio de cada classe, e a variância de cada classe.
O código da segunda parte do EP está no Jupyter Notebook EP2_normalization.ipynb.

Link para os dados: https://www.kaggle.com/gabrielamelo/image-processing
