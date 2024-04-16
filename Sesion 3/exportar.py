import os
import requests
from bs4 import BeautifulSoup
import csv
import re

# Ruta del directorio actual del script
script_dir = os.path.dirname(os.path.realpath(__file__))
csv_file_path = os.path.join(script_dir, 'noticias.csv')

# Realizar la solicitud HTTP
url = 'https://diariosinfronteras.com.pe/category/puno/'
response = requests.get(url)
html = response.text

# Analizar el HTML con BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Encontrar todos los elementos <li> con la clase "infinite-post"
posts = soup.find_all('li', class_='infinite-post')

if posts:
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Description', 'Date']
        # Cambiar el delimitador a "|"
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='|')
        writer.writeheader()

        for post in posts:
            title = post.find('h2').text.strip()
            description = post.find('p').text.strip()  # Extraer la descripción del artículo
            link = post.find('a')['href']

            # Utilizar expresión regular para extraer la fecha del enlace
            date_pattern = r"/(\d{4})/(\d{2})/(\d{2})/"
            match = re.search(date_pattern, link)
            if match:
                year = match.group(1)
                month = match.group(2)
                day = match.group(3)
                date_published = f"{day}-{month}-{year}"
            else:
                date_published = "No se pudo encontrar la fecha"

            writer.writerow({'Title': title, 'Description': description, 'Date': date_published})

    print(f"Los datos han sido exportados correctamente a '{csv_file_path}'.")
else:
    print("No se encontraron noticias en la página principal.")
