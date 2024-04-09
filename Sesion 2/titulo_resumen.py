import requests
from bs4 import BeautifulSoup
import re

# Realizar la solicitud HTTP
url = 'https://diariosinfronteras.com.pe/category/puno/'
response = requests.get(url)
html = response.text

# Analizar el HTML con BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Encontrar todos los elementos <li> con la clase "infinite-post"
posts = soup.find_all('li', class_='infinite-post')

# Expresión regular para extraer la fecha del enlace
date_pattern = r"/(\d{4})/(\d{2})/(\d{2})/"

# Iterar sobre los elementos y extraer la información deseada
for post in posts:
    title = post.find('h2').text.strip()
    description = post.find('p').text.strip()  # Extraer la descripción del artículo
    
    # Obtener el enlace de la noticia
    link = post.find('a')['href']
    
    # Buscar la fecha en el enlace utilizando la expresión regular
    match = re.search(date_pattern, link)
    if match:
        year = match.group(1)
        month = match.group(2)
        day = match.group(3)
        date = f"{year}-{month}-{day}"
    else:
        date = "No se pudo encontrar la fecha"
    
    print(f"Fecha: {date}\nTitulo: {title}\nDescription: {description}\n")
    print(f"------------------------------------------------------")
