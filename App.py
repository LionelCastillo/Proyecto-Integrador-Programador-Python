'''
Ejercicio Integrador Programador Python
Autor: Victor Lionel Castillo
Version: 1.0
Descripcion: programa que funciona que consulta datos meteorologicos de, 
una ciudad, en la API  de OpenWaether los guardara en variables y las 
mostrara en una interfaz creada con TKinter.

'''

from tkinter import *
import requests

#clave para acceder y poder conectarte con la API,
#se la pasa como parametro para realizar la conexion 
#14e0e7ab132c6e5a66d2e23b53cd99cf
#URL de la API para extraer los datos
#https://api.openweathermap.org/data/2.5/weather


#Funcion para guardar los datos meteorologicos en sus variables
def mostrar_clima(clima):
    ciudad["text"] = clima["name"]
    descripcion["text"] =clima["weather"][0]["description"] 
    temperatura["text"] = 'Temperatura', 'actual', clima["main"]["temp"],'°C'
    humedad["text"] = 'Humedad', clima["main"]["humidity"],'%'
    vientos["text"] = 'vientos', int(clima["wind"]["speed"]*18/5), 'Km/H'
    

#Funcion para conectarse con la API y obtener los datos   
def pronostico(ciudad):
    API_key = "14e0e7ab132c6e5a66d2e23b53cd99cf"
    URL = "https://api.openweathermap.org/data/2.5/weather"
    parametros = {"APPID": API_key, "q": ciudad, "units": "metric", "lang": "es"}
    response = requests.get(URL, params = parametros)
    clima = response.json()
    print(response.json())
    
    mostrar_clima(clima)

#Creacion de la interfaz, con su dimension y color
ventana = Tk()
ventana.geometry("900x700")
ventana.config(bg="light sky blue")

#Barra donde se ingresa la ciudad
texto_ciudad = Entry(ventana, font = ("Courier", 20, "normal"), justify = "center")
texto_ciudad.pack (padx = 30, pady = 30 )

#Boton para realizar la busqueda de la ciudad
obtener_clima = Button(ventana, text ="Obtener Clima", font = ("Courier", 20, "normal"), command = lambda : pronostico (texto_ciudad.get()))
obtener_clima.pack()

#Muestra los datos Obtenidos
ciudad = Label(font = ("Courier", 25, "normal"))
ciudad.pack(padx=25, pady=25)

descripcion = Label(font = ("Courier", 25, "normal"))
descripcion.pack(padx=15, pady=15)

temperatura = Label(font = ("Courier", 25, "normal"))
temperatura.pack(padx=15, pady=15)

humedad = Label(font = ("Courier", 25, "normal"))
humedad.pack(padx=15, pady=15)

vientos = Label(font = ("Courier", 25, "normal"))
vientos.pack(padx=15, pady=15)

ventana.mainloop ()