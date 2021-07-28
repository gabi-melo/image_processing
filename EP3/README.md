# image_processing

MAC0417/5768 - Visão e Processamento de Imagens (2021)
Exercício Programa 3 (EP3)
Gabriela Melo e Richard Block

O EP3 está dividido em duas partes. A primeira parte tem como objetivo a segmentação de imagens e a segunda parte tem como objetivo a classificação de imagens.

###

Na primeira parte do EP realizamos a segmentação das imagens em níveis de cinza do dataset gerado no EP2. Duas formas de segmentação foram aplicadas: manual e automática. Para a segmentação manual, utilizamos cerca de 15% das imagens em níveis de cinza de cada classe de objetos. Foi empregado o programa Label Studio para a segmentação semântica com máscaras. A segmentação manual gerou imagens binárias, em que o valor de 0 corresponde ao fundo e o valor de 1 corresponde ao objeto, compondo o "ground truth" do dataset. Essas imagens binárias foram processadas utilizando um Feret Box para delimitar a área de interesse, fazendo com que a região a ser analisada na etapa de classificação (EP3.2) esteja restrita ao objeto, auxiliando a localização do objeto pelo algoritmo classificador. Métricas para a avaliação do modelo de segmentação foram computadas.

Para a segmentação automática usamos um método chamado U square Net, baseado numa arquitetura de rede profunda (disponível em https://arxiv.org/pdf/2005.09007.pdf). Métricas para a avaliação do modelo de segmentação foram computadas.

O código da primeira parte do EP está no Jupyter Notebook EP3.1_segmentation.ipynb.

###

Na segunda parte do EP realizamos a etapa de classificação, baseada nas imagens binárias com Feret Box obtidas na primeira parte. As imagens foram redimensionaras para que todas as classes apresentem o mesmo tamanho. Os dados foram separados em conjuntos de treino e de teste. Então foi executada uma etapa de preparação para o aprendizado, com a extração do vetor de características. Para isso, foi utilizada a análise de componentes principais (PCA). A PCA descobre os eixos/vetores de maior variância dos dados, fazendo uma análise a partir da matriz de covariância. O vetor que indica a maior variabilidade dos dados é o primeiro autovetor. O vetor perpendicular é o segundo autovetor, indicando o segundo vetor de maior variabilidade. A transformada PCA muda a coordenada dos pontos definida pelos autovetores, realizando a redução da dimensionalidade.

O vetor de características resultante foi então submetido à classificação, utilizando um algoritmo de máquina de suporte vetorial (SVM). Um classificador define um modelo algébrico para qual é a superfície de decisão. O modelo mais simples é uma linha reta que divide o conjunto de dados para fazer a separação dos dados entre as diferentes classes. As máquinas de suporte vetorial procuram criar uma reta que define uma função critério, a qual é otimizada. O procedimento de otimização faz calcula qual é a linha reta que maximiza as distâncias dos pontos mais próximos da reta. O processo de treinamento de SVM descobre qual é essa linha reta que apresenta a maior distância possível de todas as classes. Esse treino foi realizado exclusivamente nos dados do conjunto de treino.
Foram calculadas métricas de avaliação da qualidade do modelo nos dados do conjunto de teste. Foi realizada a predição dos rótulos das classes do conjunto de teste, e foram computadas variáveis da performance do classificador.

O código da segunda parte do EP está no Jupyter Notebook EP3.2_classification.ipynb.

###

Projeto GitHub: https://github.com/gabi-melo/image_processing/tree/main/EP3
Base de imagens: https://www.kaggle.com/gabrielamelo/image-processing
