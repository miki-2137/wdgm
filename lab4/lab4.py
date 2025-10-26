from PIL import Image
import numpy as np


#zad5
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

obraz_r = rysuj_pasy_pionowe_szare(300, 200, 10, 55)
obraz_g = rysuj_pasy_pionowe_szare(300, 200, 18, 55)
obraz_b = rysuj_pasy_pionowe_szare(300, 200, 26, 55)

r_ext = np.expand_dims(obraz_r, axis=-1)
g_ext = np.expand_dims(obraz_g, axis=-1)
b_ext = np.expand_dims(obraz_b, axis=-1)

tab_rgb = np.concatenate((r_ext, g_ext, b_ext), axis=-1)
obraz_rgb = Image.fromarray(tab_rgb, mode="RGB")
obraz_rgb.save("obraz6.png")


#zad6
def rysuj_po_skosie_szare(h, w, a, b):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab[i, j] = (a*i + b*j) % 256
    return Image.fromarray(tab)

obraz_a = rysuj_po_skosie_szare(200,300, 7, 7)

a_ext = np.expand_dims(obraz_a, axis=-1)

tab_rgba = np.concatenate((obraz_rgb, a_ext), axis=-1)
obraz_rgba = Image.fromarray(tab_rgba)
obraz_rgba.save('obraz7.png')


#zad7
def rgb_to_cmyk(rgb_array):
    rgb = rgb_array.astype(float) / 255
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    k = 1 - np.max(rgb, axis=2)
    c = (1 - r - k) / (1 - k + 1e-8)
    m = (1 - g - k) / (1 - k + 1e-8)
    y = (1 - b - k) / (1 - k + 1e-8)
    c[np.isnan(c)] = 0
    m[np.isnan(m)] = 0
    y[np.isnan(y)] = 0
    cmyk = np.stack((c, m, y, k), axis=2) * 255
    return cmyk.astype(np.uint8)

tab_cmyk = rgb_to_cmyk(tab_rgb)
obraz_cmyk = Image.fromarray(tab_cmyk, mode="CMYK")
obraz_cmyk.save('obraz8.tiff')


t_r = tab_rgb[:, :, 0]
im_r = Image.fromarray(t_r)
im_r.save('r.png')

t_c = tab_cmyk[:, :, 0]
im_c = Image.fromarray(t_c)
im_c.save('c.png')
