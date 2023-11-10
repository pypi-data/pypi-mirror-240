import os
import matplotlib.pyplot as plt
from matplotlib.image import imread
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from quos import icons

def qplt(ssgtq):
    """
    Output: Matplotlib plot
    sgtq: String of strings of gates times qubits:
        Comma-concatenated string of space-concatenated strings of
        gate-name str, time-number int, qubit-number int,
        affected gate-name str, affected time-number int, affected qubit-number int
    """
    asgtq = ssgtq.split(',')
    agtq = asgtq[0].split(" ")
    t, q = int(agtq[1]), int(agtq[2])
    tlo, tup, qlo, qup = t, t, q, q
    for sgtq in asgtq:
        agtq = sgtq.split(" ")
        t, q = int(agtq[1]), int(agtq[2])
        if (t < tlo): tlo = t
        if (t > tup): tup = t
        if (q < qlo): qlo = q
        if (q > qup): qup = q
        if len(agtq) > 3:
            t, q = int(agtq[4]), int(agtq[5])
            if (t < tlo): tlo = t
            if (t > tup): tup = t
            if (q < qlo): qlo = q
            if (q > qup): qup = q
    fig = plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.set_xlim(tlo-1, tup+1)
    ax.set_ylim(-qup-1, -qlo+1)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    for q in range(-qup,-qlo+1):
        ax.axhline(q, color='red', lw=1)
    if os.path.isfile('icons/H.jpg'):
        idir = 'icons/'
    else:
        idir = (icons.__file__).replace('__init__.py','')
    for sgtq in asgtq:
        agtq = sgtq.split(" ")
        ax.add_artist(AnnotationBbox(
            OffsetImage(imread(idir + agtq[0]+'.jpg')),
            (int(agtq[1]), -int(agtq[2])),
            frameon=False))
        if len(agtq) > 3:
            ax.add_artist(AnnotationBbox(
                OffsetImage(imread(idir + agtq[3]+'.jpg')),
                (int(agtq[4]), -int(agtq[5])),
                frameon=False))
            plt.plot([float(agtq[1]),float(agtq[4])],
                [-float(agtq[2]),-float(agtq[5])], 'b')
    plt.show()

# qplt('H 1 1,X 1 2,Z 2 3,Y 2 4,C 3 1 X 3 3,H 4 2')
