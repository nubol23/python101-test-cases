import os
import urllib
import time

def getUrlMonth(site_url, sub_url):
    links = []
    ruta_i = urllib.request.urlopen( site_url+sub_url)
    ruta_i = bs(ruta_i, "html.parser")
    for line in ruta_i.find("div", class_ = "list-archive").findAll("li"):
        links.append(line.find("a").get("href"))
    return links

def getDatos(receta_i):
    print("Obteniendo datos para: \n" + receta_i)
    Page_i = bs(urllib.request.urlopen(site+ receta_i), "html.parser")
    try:
        ingredientes = []
        for ingrediente in Page_i.find("ul", class_ = "asset-recipe-list").findAll("li"):
            ingredientes.append(ingrediente.text)
        preparacion = Page_i.find("div", class_ = "asset-recipe-steps").text
        dificultad = Page_i.find("div", class_="asset-recipe-difficulty").text
        pic_url = Page_i.find("div", class_ = "article-asset-big").find("img").get("src")
        urllib.request.urlretrieve(pic_url, receta_i.split("/")[-1]+".png")
        print("%%%%%%%% DATOS OBTENIDOS CON ÉXITO %%%%%%%%%%")
        return [receta_i, dificultad, ingredientes, preparacion]
    except:
        print("%%%%%%%% ERROR %%%%%%%%%%")
        pass