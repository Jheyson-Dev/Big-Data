import requests
from bs4 import BeautifulSoup
import csv

# Realizar la solicitud HTTP
url = 'https://diariosinfronteras.com.pe/category/puno/'
response = requests.get(url)
html = response.text

# Analizar el HTML con BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Encontrar todos los elementos <li> con la clase "infinite-post"
posts = soup.find_all('li', class_='infinite-post')

if posts:
    with open('noticias.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Link', 'Image URL', 'Views', 'Description', 'Category', 'Date Published']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for post in posts:
            title = post.find('h2').text.strip()
            link = post.find('a')['href']
            image = post.find('img')['src']
            views = post.find('span', class_='feat-info-text').text.strip()
            description = post.find('p').text.strip()  # Extraer la descripción del artículo

            # Obtener el contenido completo del artículo
            article_response = requests.get(link)
            article_html = article_response.text
            article_soup = BeautifulSoup(article_html, 'html.parser')

            # Buscar y extraer la categoría del artículo
            category = article_soup.find('a', class_='post-cat-link').text.strip()

            # Buscar y extraer la fecha de publicación del artículo
            date_published = article_soup.find('time', class_='post-date updated').text.strip()

            writer.writerow({'Title': title, 'Link': link, 'Image URL': image, 'Views': views,
                             'Description': description, 'Category': category, 'Date Published': date_published})

    print("Los datos han sido exportados correctamente a 'noticias.csv'.")
else:
    print("No se encontraron noticias en la página principal.")
