from PIL import Image
import numpy as np

def rysuj_pasy_pionowe_szare(w, h, grub, zmiana_koloru):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w / grub)
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                tab[j, i] = (k + zmiana_koloru) % 256
    return Image.fromarray(tab)

r = rysuj_pasy_pionowe_szare(300,200,10,25)
r.show()
g = rysuj_pasy_pionowe_szare(300,200,18,25)
g.show()
b = rysuj_pasy_pionowe_szare(300,200,26,25)
b.show()

def rysuj_pasy_poziome_szare(w, h, grub, zmiana_koloru):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(h / grub)
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(w):
                tab[i, j] = (k + zmiana_koloru) % 256
    return Image.fromarray(tab)


im_paski = rysuj_pasy_poziome_szare(100, 246, 1, 10)
# im_paski.show()