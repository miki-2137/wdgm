from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt

#zad6  takie samo bedzie na kolokwium almost sure

beks = Image.open('beksinski.png')
beks1 = Image.open('beksinski1.png')
beks2 = Image.open('beksinski2.png')
beks3 = Image.open('beksinski3.png')

def ocen_czy_identyczne(obraz1, obraz2):
    if obraz1.mode != obraz2.mode:
        print('obrazy maja rozne tryby')
        return 0
    if obraz1.size != obraz2.size:
        print('obrazy maja rozne rozmiary')
        return 0
    t1 = np.asarray(obraz1)
    t2 = np.asarray(obraz2)
    h, w, d = t1.shape
    for i in range(h):
        for j in range(w):
            for k in range(d):
                if t1[i, j, k] != t2[i, j, k]:
                    print(f'piksele obrazow o wspolrzednych {i},{j},{k} roznia sie')
                    return 0
    print('obrazy sa identyczne')
    return 1

ocen_czy_identyczne(beks, beks1)
ocen_czy_identyczne(beks, beks2)
ocen_czy_identyczne(beks, beks3)

#zad7

def pokaz_roznice(obraz_wejsciowy):
    t = np.asarray(obraz_wejsciowy)
    h, w, d = t.shape
    for i in range(h):
        for j in range(w):
            for k in range(d):
                # t[i, j, k] =