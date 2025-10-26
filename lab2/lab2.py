from PIL import Image
import numpy as np

#zad1
inicjaly = Image.open("inicjaly.bmp")
def rysuj_ramke_w_obrazie(obraz, grub):
    tab_obraz = np.asarray(obraz).astype(np.uint8)
    h, w = tab_obraz.shape
    for i in range(h):
        for j in range(grub):
            tab_obraz[i][j] = 0
        for j in range(w-grub,w):
            tab_obraz[i][j] = 0
    for i in range(w):
        for j in range(grub):
            tab_obraz[j][i] = 0
        for j in range(h-grub, h):
            tab_obraz[j][i] = 0
    tab = tab_obraz.astype(bool)
    return Image.fromarray(tab)

rysuj_ramke_w_obrazie(inicjaly, 5).show()

#zad2 1.1
def rysuj_ramki(w, h, grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = min(w, h) // grub
    for i in range(ile):
        tab[i*grub:h - i*grub, i*grub:w - i*grub] = i % 2
    tab1 = tab.astype(np.bool_)
    return Image.fromarray(tab1)

rysuj_ramki(300, 161, 10).show()

#zad2 1.2
def rysuj_pasy_pionowe(w, h, grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w/grub)
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                tab[j, i] = k % 2
    tab = tab * 255
    return Image.fromarray(tab)

rysuj_pasy_pionowe(100, 100, 10).show()

#zad2 1.3
# na srodku obrazu o wymiarach w,h tworzy krzyz o grubisci 2*grub
def rysuj_wlasne(w,h,grub):
    tab = np.ones((h,w),dtype=np.bool_)
    tab[(h//2)-grub:grub+(h//2), :] = 0
    tab[:, (w//2)-grub:grub+(w//2)] = 0
    return Image.fromarray(tab)

rysuj_wlasne(200,100,20).show()

#zad3
def wstaw_obraz_w_obraz(obraz_bazowy, obraz_wstawiany, m, n):
    tab_wstawiany = np.asarray(obraz_wstawiany).astype(np.uint8)
    tab_bazowy = np.asarray(obraz_bazowy).astype(np.uint8)
    h, w = tab_bazowy.shape
    h0, w0 = tab_wstawiany.shape
    n_k = min(h, n + h0)
    m_k = min(w, m + w0)
    n_p = max(0, n)
    m_p = max(0, m)
    for i in range(n_p, n_k):
        for j in range(m_p, m_k):
            tab_bazowy[i][j] = tab_wstawiany[i - n][j - m]
    tab_bazowy = tab_bazowy.astype(bool)
    return Image.fromarray(tab_bazowy)


inicjaly = Image.open("inicjaly.bmp")
obraz_bazowy = Image.open("obraz_bazowy.bmp")

wstaw_obraz_w_obraz(obraz_bazowy, inicjaly, 50, 10).show()