import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
from skimage.io import imread_collection

#caminho
ex_dir = '/Users/richardbarana/Downloads/exemplos/*.jpg'

#criando uma coleção com as imagens da pasta
col = imread_collection(ex_dir)

fig = plt.figure(figsize=(4., 4.))
grid = ImageGrid(fig, 111, nrows_ncols=(4,5), axes_pad=0.1)

for ax, im in zip(grid, col):
    ax.imshow(im)

plt.show()