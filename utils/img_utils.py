import requests
import cv2
import matplotlib.pyplot as plt
import numpy as np


def descargar_img(url: str):
    resp = requests.get(url)
    image = np.asarray(bytearray(resp.content), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    
    return image
    
def mostrar_img(img: np.ndarray):
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()
    
def mostrar_mascara(img: np.ndarray):
    plt.imshow(img, cmap='gray')
    plt.show()
    
def crear_mascara(img, limite=1):
    _, bin_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), limite, 255, cv2.THRESH_BINARY)
    return bin_img
    
def crear_imagen_con_transparencia(img: np.ndarray):
    no_background_image = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    return no_background_image
    
def es_pixel_negro(img: np.ndarray, i:int, j: int):
    if img[i, j] == 0:
        return True
    else:
        return False

def volver_pixel_transparente(img: np.ndarray, i: int, j: int):
    img[i, j, 3] = 0

def dimensiones_de_la_imagen(img: np.ndarray):
    return img.shape[:2]
    
def guardar_imagen(nombre:str, img: np.ndarray):
    cv2.imwrite(nombre, img)
