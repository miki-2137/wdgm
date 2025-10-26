from PIL import Image
import numpy as np

def rysuj_ramki_szare(w, h, grub, zmiana_koloru):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = min(w, h) // grub

    for i in range(ile):
        shade = min(0 + i * zmiana_koloru, 255)
        tab[i*grub:h - i*grub, i*grub:w - i*grub] = shade
    return Image.fromarray(tab)

# rysuj_ramki_szare(270, 165, 3, 8).show()

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

# rysuj_pasy_pionowe_szare(300, 200, 5, 10).show()

