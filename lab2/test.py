from PIL import Image  # Python Imaging Library
import numpy as np

# def rysuj_pasy_pionowe(w, h, grub):
#     t = (h, w)
#     tab = np.ones(t, dtype=np.uint8)
#     ile = int(w/grub)
#     for k in range(ile):
#         for g in range(grub):
#             i = k * grub + g
#             for j in range(h):
#                 tab[j, i] = k % 2
#     tab = tab * 255
#     return Image.fromarray(tab)
#
# # rysuj_pasy_pionowe(200, 100, 10).save("wynik.bmp")
#
# obraz = Image.open('wynik256.bmp')
# tab = np.asarray(obraz)
#
# print("tryb:", obraz.mode)
# print("piksel:", tab[13][66])
# #66,13 13,66
# print("element tablicy:", tab[97][20])

# def rysuj_wlasne(w,h,grub):
#     tab = np.ones((h,w),dtype=np.bool_)
#     tab[(h//2)-grub:grub+(h//2), :] = 0
#     tab[:, (w//2)-grub:grub+(w//2)] = 0
#     return Image.fromarray(tab)
#
# wynik = rysuj_wlasne(200,100,20)
# wynik.show()
# wynik.save("wlasne.bmp")

# tab = np.loadtxt("tablica.txt", dtype=np.bool_)
# img = Image.fromarray(tab)
# print(img.mode)
#
# def rysuj_ramke_w_obrazie(obraz, grub):
#     tab_obraz = np.asarray(obraz).astype(np.uint8)
#     h, w = tab_obraz.shape
#     for i in range(h):
#         for j in range(grub):
#             tab_obraz[i][j] = 0
#         for j in range(w-grub,w):
#             tab_obraz[i][j] = 0
#     for i in range(w):
#         for j in range(grub):
#             tab_obraz[j][i] = 0
#         for j in range(h-grub, h):
#             tab_obraz[j][i] = 0
#     tab = tab_obraz.astype(bool)
#     return Image.fromarray(tab)
#
# ramka = rysuj_ramke_w_obrazie(img, 20)
# ramka.show()
# ramka.save("ramka.bmp")

# def rysuj_pasy_pionowe(w, h, grub):
#     t = (h, w)
#     tab = np.ones(t, dtype=np.uint8)
#     ile = int(w/grub)
#     for k in range(ile):
#         for g in range(grub):
#             i = k * grub + g
#             for j in range(h):
#                 tab[j, i] = k % 2
#     tab = tab * 255
#     return Image.fromarray(tab)
#
# def wstaw_obraz_w_obraz(obraz_bazowy, obraz_wstawiany, m, n):
#     tab_wstawiany = np.asarray(obraz_wstawiany).astype(np.uint8)
#     tab_bazowy = np.asarray(obraz_bazowy).astype(np.uint8)
#     h, w = tab_bazowy.shape
#     h0, w0 = tab_wstawiany.shape
#     n_k = min(h, n + h0)
#     m_k = min(w, m + w0)
#     n_p = max(0, n)
#     m_p = max(0, m)
#     for i in range(n_p, n_k):
#         for j in range(m_p, m_k):
#             tab_bazowy[i][j] = tab_wstawiany[i - n][j - m]
#     tab_bazowy = tab_bazowy.astype(bool)
#     return Image.fromarray(tab_bazowy)
#
#
# obraz_bazowy = rysuj_pasy_pionowe(300, 200, 15)
# obraz_wstawiany = Image.open("inicjaly.bmp")
#
# wstaw1 = wstaw_obraz_w_obraz(obraz_bazowy, obraz_wstawiany, 250, 100)
# wstaw1.show()
# wstaw1.save("wstaw1.bmp")
# wstaw2 = wstaw_obraz_w_obraz(obraz_bazowy, obraz_wstawiany, 0, 50)
# wstaw2.show()
# wstaw2.save("wstaw2.bmp")

def rysuj_ramki(w, h, grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = min(w, h) // grub
    for i in range(ile):
        tab[i*grub:h - i*grub, i*grub:w - i*grub] = i % 2
    tab1 = tab.astype(np.bool_)
    return Image.fromarray(tab1)

rysuj_ramki(80, 130, 5).save("ramki.bmp")

obraz = Image.open('ramki.png')
tab = np.asarray(obraz)

print("tryb:", obraz.mode)
print("rozmiar:", obraz.size)
print("wymiar tablicy:", tab.ndim)
print("liczba elementow:", tab.size)
