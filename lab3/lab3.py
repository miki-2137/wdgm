from PIL import Image
import numpy as np


#zad1
def rysuj_ramki_szare(w, h, grub, zmiana_koloru):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    ile = min(h, w) // grub
    for i in range(ile):
        tab[i*grub:h - i*grub, i*grub:w - i*grub] = (i*zmiana_koloru) % 256
    return Image.fromarray(tab)

rysuj_ramki_szare(270,165,10,30).show()


def rysuj_pasy_pionowe_szare(w, h, grub, zmiana_koloru):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w/grub)
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                tab[j, i] = (k*zmiana_koloru) % 256
    return Image.fromarray(tab)

rysuj_pasy_pionowe_szare(252, 200, 30, 10).show()


#zad2
def negatyw(obraz):
    tab = np.asarray(obraz)
    if len(tab.shape) == 2:
        h, w = tab.shape
    elif len(tab.shape) == 3:
        h, w, c = tab.shape
    if obraz.mode == 'L' or obraz.mode == 'RGB':
        tab_neg = tab.copy()
        for i in range(h):
            for j in range(w):
                tab_neg[i, j] = 255 - tab[i, j]
        return Image.fromarray(tab_neg.astype(np.uint8))
    elif obraz.mode == '1':
        tab_bool = np.asarray(obraz, dtype=bool)
        tab_neg = np.logical_not(tab_bool)
        return Image.fromarray(tab_neg)
    else:
        print('Neobsługwany typ obrazu')
        return obraz

def rysuj_ramki_kolorowe(w, kolor, zmiana_koloru_r, zmiana_koloru_g, zmiana_koloru_b):
    t = (w, w, 3)
    tab = np.zeros(t, dtype=np.uint8)
    kolor_r = kolor[0]
    kolor_g = kolor[1]
    kolor_b = kolor[2]
    z = w
    for k in range(int(w / 2)):
        for i in range(k, z - k):
            for j in range(k, z - k):
                tab[i, j] = [kolor_r, kolor_g, kolor_b]
        kolor_r = (kolor_r - zmiana_koloru_r) % 256
        kolor_g = (kolor_g - zmiana_koloru_g) % 256
        kolor_b = (kolor_b - zmiana_koloru_b) % 256
    return Image.fromarray(tab)

def rysuj_po_skosie_szare(h, w, a, b):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab[i, j] = (a*i + b*j) % 256
    return Image.fromarray(tab)

gwiazdka = Image.open('gwiazdka.bmp')
negatyw(gwiazdka).save('gwiazdka_negatyw.bmp')

ramki = rysuj_ramki_kolorowe(200, [20, 120, 220], 7, 7, -7)
ramki.save('ramki_kolorowe.png')
ramki_neg = negatyw(ramki)
ramki_neg.save('ramki_kolorowe_negatyw.png')

skos = rysuj_po_skosie_szare(100, 300, 7, 7)
skos.save('skos_szare.png')
skos_neg = negatyw(skos)
skos_neg.save('skos_szare_negatyw.png')


#zad3
def koloruj_w_paski(obraz, grub, kolor, zmiana_koloru):
    t_obraz = np.asarray(obraz)
    h, w = t_obraz.shape
    tab = np.ones((h, w, 3), dtype=np.uint8) * 255
    ile = int(h / grub)
    for k in range(ile):
        r = (kolor[0] + k * zmiana_koloru) % 256
        g = (kolor[1] + k * zmiana_koloru) % 256
        b = (kolor[2] + k * zmiana_koloru) % 256
        kolory = [r, g, b]
        for m in range(grub):
            i = k * grub + m
            if i < h:
                for j in range(w):
                    if t_obraz[i, j] == 0:
                        tab[i, j] = kolory
    return Image.fromarray(tab)

inicjal = Image.open('inicjaly.bmp')
inicjaly_kolor = koloruj_w_paski(inicjal, 5, [20, 120, 220], 20)
inicjaly_kolor.save('inicjaly_kolor.png')
inicjaly_kolor.save('inicjaly_kolor.jpg')

