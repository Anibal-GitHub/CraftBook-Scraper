import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# URL base
base_url = "https://www.herronbooks.com"
start_url = "https://www.herronbooks.com/shop/shop/23/cat/7/page/"

# Función para extraer datos de una página
def scrape_page(page_url):
    response = requests.get(page_url)
    if response.status_code != 200:
        print(f"Error al acceder a {page_url}: {response.status_code}")
        return None

    soup = BeautifulSoup(response.content, "html.parser")

    # Contenedor principal de cada artículo
    items = soup.find_all("div", class_="shopItem")

    # Datos recopilados
    data = {
        "Name": [],
        "Author": [],
        "Description": [],
        "ISBN": [],
        "Price": [],
        "Image URL": [],
        "Page URL": [],
    }

    # Extraer datos
    for item in items:
        # Nombre del producto
        name = item.find("h4", class_="itemTitle")
        data["Name"].append(name.text.strip() if name else "N/A")

        # Autor
        author = item.find("p", class_="itemAuth")
        data["Author"].append(author.text.replace("by", "").strip() if author else "N/A")
    
        # Descripción corta
        description = item.find("p", class_="itemSdesc")
        data["Description"].append(description.text.strip() if description else "N/A")
    
        # ISBN
        isbn = item.find("p", class_="itemISBN")
        data["ISBN"].append(isbn.text.replace("ISBN:", "").strip() if isbn else "N/A")
    
        # Precio
        price = item.find("p", class_="itemAmt")
        data["Price"].append(price.text.replace("Price:", "").strip() if price else "N/A")
    
        # URL de la imagen
        image_tag = item.find("img")
        image_url = base_url + image_tag["src"] if image_tag else "N/A"
        data["Image URL"].append(image_url)
    
        # URL de detalles
        details_link = item.find("p", class_="itemViewLink").find("a")
        page_url = base_url + details_link["href"] if details_link else "N/A"
        data["Page URL"].append(page_url)

    return data


# Acumular datos de todas las páginas
all_data = {
    "Name": [],
    "Author": [],
    "Description": [],
    "ISBN": [],
    "Price": [],
    "Image URL": [],
    "Page URL": [],
}

# Iterar por las páginas
for page in range(0, 5):  # Cambiar según el número de páginas
    print(f"Scraping página {page}...")
    page_data = scrape_page(f"{start_url}{page}/")
    if page_data:
        for key in all_data.keys():
            all_data[key].extend(page_data[key])
    time.sleep(2)  # Espera para evitar bloqueos

# Exportar a Excel
df = pd.DataFrame(all_data)
df.to_excel("craft_books.xlsx", index=False)
print("Datos exportados exitosamente.")

