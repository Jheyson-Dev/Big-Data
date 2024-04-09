import requests
from bs4 import BeautifulSoup

# Realizar la solicitud HTTP
url = 'https://diariosinfronteras.com.pe/category/puno/'
response = requests.get(url)
html = response.text

# Analizar el HTML con BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Encontrar todos los elementos <li> con la clase "infinite-post"
posts = soup.find_all('li', class_='infinite-post')

# Iterar sobre los elementos y extraer la información deseada
for post in posts:
    title = post.find('h2').text.strip()
    link = post.find('a')['href']
    image = post.find('img')['src']
    views = post.find('span', class_='feat-info-text').text.strip()
    description = post.find('p').text.strip()  # Extraer la descripción del artículo
    print(f"Title: {title}\nLink: {link}\nImage URL: {image}\nViews: {views}\nDescription: {description}\n")
    print(f"---------------------------------------------------------------------------------------------------------------------------------------------")
