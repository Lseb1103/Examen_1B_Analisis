import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import pandas as pd


def scrape_quotes():
    more_links = True
    # valor para paginacion
    page = 1
    #variable para almacenar las citas que se vayan encontrando
    quotes = []
    while(more_links):
        # hace la solicitud al sitio con las citas
        markup = requests.get(f'http://quotes.toscrape.com/page/{page}').text
        # obtiene el contenido html del sitio
        soup = BeautifulSoup(markup, 'html.parser')
        #itera através de los elementos .quote, para obtener la información de los mismos
        for item in soup.select('.quote'):
            #creamos un diccionario quote para guardar la info de cada quote
            quote = {}
            #obtenemos los valores de texto y autor según su etiqueta html
            quote['text'] = item.select_one('.text').get_text()
            quote['author'] = item.select_one('.author').get_text()
            tags = item.select_one('.tags')
            #al objeto tags del diccionario quotes, le asignamos el listado de los tags
            #por eso iteramos a través de dicho listado
            quote['tags'] = [tag.get_text() for tag in tags.select('.tag')]
            #la informacion de quote obtenida la ingresamos hacia nuestro diccionario
            quotes.append(quote)
        #con next_link apuntamos hacia el elemento que indica que existe otra página
        next_link = soup.select_one('.next > a')
        print(f'scraped page {page}')
        #si es que beautiful soup detecta que existe otra página, aumenta el valor de page
        if(next_link):
            page += 1
        else:
        #sino lo encuentra cambiamos la bandera more links de true a false 
            more_links = False
    return quotes

#Llmamamos a la función quotes que retorna todas las quotes encontradas 
quotes = scrape_quotes()

#Creamos nuestra conexión a mongo e intentamos la inserción de las quotes encontradas.  
mongo_client = pymongo.MongoClient('localhost',27017)
mongo_client_db = mongo_client.db.quotes
try:
    mongo_client_db.insert_many(quotes)
    print(f'inserted {len(quotes)} articles')
except:
    print('an error occurred quotes were not stored to db')