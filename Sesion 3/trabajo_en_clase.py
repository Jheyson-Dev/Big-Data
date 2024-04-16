import csv
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

# Ruta del archivo CSV
csv_file_path = 'noticias.csv'

# Abrir el archivo CSV en modo escritura
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    # Definir los nombres de las columnas
    fieldnames = ['Title', 'Date', 'Resumen', 'Noticia completa']

    # Crear el escritor de CSV con el separador "|" y escapar el contenido
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='|', quoting=csv.QUOTE_MINIMAL)

    # Escribir los encabezados al archivo CSV
    writer.writeheader()

    # Iterar sobre las noticias
    for post in posts:
        title = post.find('h2').text.strip()
        link = post.find('a')['href']

        # Obtener el resumen de la noticia
        resumen_container = post.find('div', class_='archive-list-text')
        resumen = resumen_container.find('p').text.strip()

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

        # Realizar la solicitud HTTP para la noticia completa
        response_article = requests.get(link)
        html_article = response_article.text
        soup_article = BeautifulSoup(html_article, 'html.parser')

        # Encontrar todos los párrafos dentro de la noticia
        paragraphs = soup_article.find('div', id='content-main').find_all('p')

        # Concatenar el texto de los párrafos y el texto después de las etiquetas <br>
        full_article = ''
        for paragraph in paragraphs:
            paragraph_text = paragraph.get_text(separator=' ')
            br_text = ''
            for sibling in paragraph.next_siblings:
                if sibling.name == 'br':
                    br_text += sibling.get_text(separator=' ')
            full_article += paragraph_text + ' ' + br_text + ' '

        # Escribir los datos al archivo CSV
        writer.writerow({'Title': title, 'Date': date_published, 'Resumen': resumen, 'Noticia completa': full_article.strip()})

print(f"Los datos han sido exportados correctamente a '{csv_file_path}'.")
