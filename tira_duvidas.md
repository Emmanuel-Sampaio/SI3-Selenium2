# Operações com driver do selenium
## Importar o driver do firefox
from selenium import webdriver
driver = webdriver.Firefox()
## Criar um driver para navegar no browser
```
#Open web page online
driver.get('https://www.google.com')
print("Page opened Online")

```
##  Maximizar
```
driver = webdriver.Firefox()
driver.get('https://www.google.com')
#Maximise Window
driver.maximize_window()
print("Browser is maximised")
```
##  Fullscreen
```
driver = webdriver.Firefox()
driver.get('https://www.google.com')
#FullScreen
driver.fullscreen_window()
print("Browser is Fullscreen")
```
##  Redimencionado o browser
```
driver = webdriver.Firefox()
driver.get('https://www.google.com')
#Set Window Position
driver.set_window_position(x=500,y=400)
print("Sets Browser Position")
```
## Pegando as coordenadas de posição do browser
```
driver = webdriver.Firefox()
driver.get('https://www.google.com')
#Get Window Position
window_pos= driver.get_window_position()
print(window_pos)
```