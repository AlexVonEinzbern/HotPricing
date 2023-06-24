from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
import pandas as pd
import requests

from django.http import HttpResponse

hotel_precio=[]
hotel_nombre=[]
hotel_direccion=[]
hotel_imagenes=[]
ciudad = []
def scraping_view(request):
    hotel_precio.clear()
    hotel_nombre.clear()
    hotel_direccion.clear()
    hotel_imagenes.clear()
    ciudad.clear()
    # Opciones de navegación
    options =  webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')

    driver_path = 'c:\\Users\\kmilo\\Downloads\\chromedriver_win32\\chromedriver.exe'

    driver = webdriver.Chrome(driver_path, chrome_options=options)

    # Iniciarla en la pantalla 2
    driver.set_window_position(2000, 0)
    driver.maximize_window()

    # Inicializamos el navegador
    #driver.get('https://ayenda.com/co/hoteles/cali')
    #driver.get('https://ayenda.com/co/hoteles/medellin')
    #driver.get('https://ayenda.com/co/hoteles/santa-marta')
    #driver.get('https://ayenda.com/co/hoteles/pereira')
    driver.get('https://ayenda.com/co/hoteles/popayan')
    #Obtén la altura total de la página
    page_height = driver.execute_script("return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")
    final = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #
    
    # Define la altura del desplazamiento (por ejemplo, 500 píxeles)
    scroll_height = 200
    new_height_ = driver.execute_script("return document.body.scrollHeight")
    cantidad_hoteles_int=0
    ho=True
    lista=True
    b_=1
    b__=b_+1
    # Recorre la página en incrementos de scroll_height
    for scroll in range(0, page_height*6, scroll_height):
    # Ejecuta el script para desplazarte al siguiente punto en la página
        driver.execute_script(f"window.scrollTo(0, {scroll});")
    # Realiza aquí las operaciones que deseas realizar en cada parte de la página
        b_=b_+2
        if ho:
            time.sleep(10)
            cantidad_hoteles= driver.find_element(By.XPATH, '/html/body/div[1]/main/div/nav/div/h1/span[1]')
            cantidad_hoteles_texto = cantidad_hoteles.text
            cantidad_hoteles_int = int(cantidad_hoteles_texto)
            print("cantidad de hoteles p: ", cantidad_hoteles_int)
            xpath_ciudad = "/html/body/div[1]/main/div/nav/div/h1/text()[last()]"
            #/html/body/div[1]/main/div/nav/div/h1/text()[2]
            #/html/body/div[1]/main/div/nav/div/h1/text()[1]
            texto_ciudad = driver.execute_script(f'return document.evaluate("{xpath_ciudad}", document, null, XPathResult.STRING_TYPE, null).stringValue;')
            ciudad_=texto_ciudad.split()[1]
            ciudad.append(ciudad_)
            print("ciudad: ", ciudad[0])
            b_=1
            ho=False
        if lista:
            #print("cantidad de hoteles : ", cantidad_hoteles_int)
            
            b__=b_+1
            time.sleep(2)
            print("b_: ",b_)
            xpath__ = f'/html/body/div[1]/main/div/section/a[{b_}]/div/div[1]/div'
            
            elemento_padre = driver.find_element(By.XPATH, xpath__)
            elemento_div = elemento_padre.find_element(By.XPATH, './/div[contains(@class, "slick-slider css-uwwqev slick-initialized")]')
            if (cantidad_hoteles_int % 2 != 0 and b__ != cantidad_hoteles_int + 1) or cantidad_hoteles_int % 2 == 0:
                xpath__d = f'/html/body/div[1]/main/div/section/a[{b__}]/div/div[1]/div'
                elemento_padre_d = driver.find_element(By.XPATH, xpath__d)
                elemento_div_d = elemento_padre_d.find_element(By.XPATH, './/div[contains(@class, "slick-slider css-uwwqev slick-initialized")]')
            try:
                #print("b_: ",b_)
                #print("b__: ",b__)
                boton = elemento_div.find_element(By.XPATH, f'.//button[2]/span')
                boton_d = elemento_div_d.find_element(By.XPATH, f'.//button[2]/span')
               # b_=b_+2
                try:     
                    boton.click()
                    boton_d.click()
                    #b_=b_+1
                except ElementClickInterceptedException:
                    print("El elemento está siendo bloqueado y no se puede hacer clic")
            except NoSuchElementException:
                print("no se encontro")
            if cantidad_hoteles_int % 2 == 0:
                if b__ == cantidad_hoteles_int:
                    lista=False 
            else:
                if b_ == cantidad_hoteles_int:
                    lista=False 
            
            print("lista: ", lista)        
        new_height = driver.execute_script("return document.body.scrollHeight")
        scroll_position = driver.execute_script("return window.pageYOffset;")
        window_height = driver.execute_script("return window.innerHeight;")
        #corregir el if
        
        if scroll_position >= (new_height-window_height):
            print("va hacer el break")
            break
        new_height_=new_height
    # Agrega una espera explícita si es necesario esperar a que se cargue el contenido
        time.sleep(5) 
    

    elemento_div_a = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/section')
    elemento_a = elemento_div_a.find_elements(By.XPATH, './a')
    a_ =  1
    j=1
    
    for y in elemento_a:
        lista_texto = []
        lista_imagenes = []
        #Nombre de los hoteles
        ruta_nombre = f"/html/body/div[1]/main/div/section/a[{a_}]/div/div[2]/div/div[1]"
        elemento_div_nombres = driver.find_element(By.XPATH, ruta_nombre)
        h3 = elemento_div_nombres.find_elements(By.XPATH, './h3')
        for nombre_ in h3:
            nombre_hotel = nombre_.text
            hotel_nombre.append(nombre_hotel)
            j = j+1   
        
        #Precio de los hoteles    
        elemento_div_precio = driver.find_element(By.XPATH,f"/html/body/div[1]/main/div/section/a[{a_}]/div/div[2]/div/div[2]/div")                                       
        spans = elemento_div_precio.find_elements(By.XPATH, './/span')
        spans_deseados = [span for span in spans if span.find_element(By.XPATH, './..') == elemento_div_precio]

        for span in spans_deseados:
            texto_span = span.text
            lista_texto.append(texto_span)
        hotel_precio.append(lista_texto)

        #Direccion hoteles
        elemento_div_direccion = driver.find_element(By.XPATH,f"/html/body/div[1]/main/div/section/a[{a_}]/div/div[2]/div")
        spans_d = elemento_div_direccion.find_elements(By.XPATH, './/span')
        spans_deseados_d = [span for span in spans_d if span.find_element(By.XPATH, './..') == elemento_div_direccion]
        for span_d in spans_deseados_d:
            texto_span_d = span_d.text
            hotel_direccion.append(texto_span_d)
        
        #Imagenes
        xpath_imagen = f'/html/body/div[1]/main/div/section/a[{a_}]/div/div[1]/div'
        elemento_padre_imagen = driver.find_element(By.XPATH, xpath_imagen)
        elemento_div_imagen = elemento_padre_imagen.find_element(By.XPATH, './/div[contains(@class, "slick-slider css-uwwqev slick-initialized")]')
        imagen = elemento_div_imagen.find_element(By.XPATH, './/div/div/div[2]/div/img')
        ruta_imagen = imagen.get_attribute('src')
        contenido_imagen = requests.get(ruta_imagen).content
        lista_imagenes.append(contenido_imagen)
        imagen_dos = elemento_div_imagen.find_element(By.XPATH, './/div/div/div[3]/div/img')
        ruta_imagen_dos = imagen_dos.get_attribute('src')
        contenido_imagen_dos = requests.get(ruta_imagen_dos).content
        lista_imagenes.append(contenido_imagen_dos)
        hotel_imagenes.append(lista_imagenes)

        a_=a_+1 

    for c in range(len(hotel_nombre)):
        if len(hotel_precio[c]) == 3:
            print("Nombre del hotel:", hotel_nombre[c])
            print("Direccion:", hotel_direccion[c])
            print("Precio antes:", hotel_precio[c][0].split()[1].replace("COP", ""))
            print("Precio ahora:", hotel_precio[c][2].replace("COP", ""))
            print("")    
        elif len(hotel_precio[c])==1:
            print("Nombre del hotel:", hotel_nombre[c])
            print("Direccion:", hotel_direccion[c])
            print("Sin habitaciones disponibles")
            print("")
        else:
            print("Nombre del hotel:", hotel_nombre[c])
            print("Direccion:", hotel_direccion[c])
            print("Precio:", hotel_precio[c][1])
            print("")

    print("tipo de ruta_imagen: ", type(ruta_imagen))
    print("len hotel imagenes: ", len(hotel_imagenes))
    print("len hotel imagenes d: ", len(hotel_imagenes[0]))
    print("len hotel imagenes d: ", len(hotel_imagenes[1]))
    print("len hotel imagenes d: ", len(hotel_imagenes[2]))
    print("len hotel imagenes d: ", len(hotel_imagenes[3]))
    print("len hotel imagenes d: ", len(hotel_imagenes[4]))
    precio__=float(hotel_precio[0][2].replace("COP", "").replace(".","").replace(",", "."))
    print("precio antes: ", precio__)
    print("tipo precio antes: ", type(precio__))
    print("ciudad: ", ciudad[0])

    response = HttpResponse(content_type='image/jpeg')

    # Retorna la imagen en la respuesta HTTP
    response.write(hotel_imagenes[0][0])
    return response
    #return HttpResponse(imagen)