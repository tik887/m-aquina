1 from selenium import webdriver 
2 import time
3 from random import randrange
4
5 tiempo_vista = 10
6 list_navegador =[]
7
8 navegador_1 = webdriver.chorome(executable_path='./chromedriver')
9 navegador_2 = webdriver.chorome(executable_path='./chromedriver')
10 navegador_3 = webdriver.chorome(executable_path='./chromedriver')
11
12 lista_navegador .append(navegador_1)
13 lista_navegador .append(navegador_2)
14 lista_navegador .append(navegador_3)
15
16 for navegador in lista navegador:
17     navegador.('tiktok.com/@luz43542'
18 while(true):
19     numero_random = randrange(0,len(lista_navegador)
20     lista_navegador[numero_random].refresh()
21     print("Navegador Numero: ",numero_random,"se a Actualizado")
22     time.sleep(tiempo_vista)
22
