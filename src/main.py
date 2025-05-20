import cv2
import numpy as np
import pandas as pd


caminhos_num = [f'{x}' for x in range(10)]
caminhos_lower = [x + "_L" for x in list('abcdefghijklmnopqrstuvwxyz')]
caminhos_upper = [x + "_U" for x in list('abcdefghijklmnopqrstuvwxyz'.upper())]

caminhos = caminhos_num + caminhos_upper + caminhos_lower

imagens = []
rotulos = []


for ind, caminho in enumerate(caminhos):
    count = 0
    for i in range(1, 3476):
        try:
            if ind < 10:
                path = f'dataset/{caminho}/{i}.png'
                print(path)
            else:
                path = f'dataset/{caminho}/{caminho.upper() + "_" + str(i)}.png'
                print(path)
            imagem = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            imagem_flatten = 255 - imagem.flatten()
        except:
            pass
        else:
            imagens.append(imagem_flatten)
            count += 1
            rotulos.append(caminho)

imagens = np.array(imagens)
rotulos = np.array(rotulos)

OCR_X = pd.DataFrame(data=imagens)
OCR_y = pd.DataFrame(data=rotulos)

OCR_X.to_csv("OCR_X.csv", ",")
OCR_y.to_csv("OCR_y.csv", ",")

print(OCR_y.to_numpy().shape)
print(OCR_X.to_numpy().shape)

