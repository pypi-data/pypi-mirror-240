import matplotlib.pyplot as plt
from matplotlib.image import imread
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import quos

def piqo(aiqo):
    """
    Output: Matplotlib plot
    aiqo: Comma-concatenated string of space-concatenated strings of
          image-name str, qubit-number int, operation-number int
    """
    b = aiqo.split(',')
    d = b[0].split(" ")
    ex, ey = int(d[2]), -int(d[1])
    x0, x1, y0, y1 = ex, ex, ey, ey
    for c in b[1:]:
        d = c.split(" ")
        ex, ey = int(d[2]), -int(d[1])
        if (ex < x0): x0 = ex
        if (ex > x1): x1 = ex
        if (ey < y0): y0 = ey
        if (ey > y1): y1 = ey
    fig = plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.set_xlim(x0-1, x1+1)
    ax.set_ylim(y0-1, y1+1)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    for y in range(y0, y1+1):
        ax.axhline(y, color='red', lw=1)
    for c in b:
        d = c.split(" ")
        ex, ey = int(d[2]), -int(d[1])
        img = imread((quos.__file__).replace('__init__.py','icons/' + d[0]+'.jpg'))
        # img = imread('icons/' + d[0]+'.jpg')
        ax.add_artist(AnnotationBbox(OffsetImage(img), (ex, ey), frameon=False))
    plt.show()

# piqo('Hadamard 1 1,PauliX 2 2,PauliY 3 3,PauliZ 4 4')