from PIL import Image
import numpy as np

inicjaly = Image.open("inicjaly.bmp")

print("tryb: ", inicjaly.mode)
print("format: ", inicjaly.format)
print("rozmiar: ", inicjaly.size)

tablica = np.asarray(inicjaly)
print(tablica)

tablica1 = tablica.astype(np.uint8)
print(tablica1)

inicjalytxt = open("inicjaly.txt", "w")
for rows in tablica1:
    for item in rows:
        inicjalytxt.write(str(item) + ' ')
    inicjalytxt.write('\n')

inicjalytxt.close()


print(tablica[30][50])
print(tablica[40][90])
print(tablica[0][99])

t1 = np.loadtxt("inicjaly.txt", dtype=np.bool_)
# print(t1)

t2 = np.loadtxt("inicjaly.txt", dtype=np.uint8)
