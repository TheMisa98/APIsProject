import requests
from typing import Optional, Dict

def obtener_direccion() -> Optional[Dict[str, str]]:
    """
    Fetches fake address data from the Faker API.

    Returns:
        dict: A dictionary containing the address data obtained from the API. 
                If an error occurs during the request, None is returned.
    """
    # Define the API URL
    url = "https://fakerapi.it/api/v1/addresses?_quantity=1"

    try:
        # Make a GET request to the API
        response = requests.get(url)
        response.raise_for_status()  # Raises an exception if there is an error in the request

        # Convert the response to JSON format
        data = response.json()
        
        # Extract address data from the response
        address_data = data['data'][0]
        address = {
            "street": address_data['street'],
            "city": address_data['city'],
            "zipcode": address_data['zipcode'],
            "country": address_data['country']
        }
        return address
    except requests.exceptions.RequestException as e:
        print("Error making the request:", e)
        return None
    
def obtener_libro() -> Optional[Dict[str, str]]:
    """
    Fetches fake book data from the Faker API.

    Returns:
        dict: A dictionary containing the book data obtained from the API. 
                If an error occurs during the request, None is returned.
    """
    # Define the API URL
    url = "https://fakerapi.it/api/v1/books?_quantity=1"

    try:
        # Make a GET request to the API
        response = requests.get(url)
        response.raise_for_status()  # Raises an exception if there is an error in the request

        # Convert the response to JSON format
        data = response.json()
        
        # Extract book data from the response
        book_data = data['data'][0]
        book = {
            "title": book_data['title'],
            "author": book_data['author'],
            "genre": book_data['genre'],
            "description": book_data['description'],
            "isbn": book_data['isbn'],
            "image": book_data['image'],
            "published": book_data['published'],
            "publisher": book_data['publisher']
        }
        return book
    except requests.exceptions.RequestException as e:
        print("Error making the request:", e)
        return None

def obtener_imagen_gatitos() -> Optional[Dict[str, str]]:
    """
    Fetches fake kitten image data from the Faker API.

    Returns:
        dict: A dictionary containing the kitten image data obtained from the API. 
                If an error occurs during the request, None is returned.
    """
    # Define the API URL
    url = "https://fakerapi.it/api/v1/images?_quantity=1&_type=kittens&_height=300"

    try:
        # Make a GET request to the API
        response = requests.get(url)
        response.raise_for_status()  # Raises an exception if there is an error in the request

        # Convert the response to JSON format
        data = response.json()
        
        # Extract kitten image data from the response
        kitten_data = data['data'][0]
        kitten_image = {
            "title": kitten_data['title'],
            "description": kitten_data['description'],
            "url": kitten_data['url']
        }
        return kitten_image
    except requests.exceptions.RequestException as e:
        print("Error making the request:", e)
        return None
    

# Example usage of the function
address = obtener_direccion()
if address is not None:
    print("Address data obtained:")
    print("-----------------------------")
    print("Street:", address['street'])
    print("City:", address['city'])
    print("Zipcode:", address['zipcode'])
    print("Country:", address['country'])
    print("-----------------------------")
    
book = obtener_libro()
if book is not None:
    print("Book data obtained:")
    print("-----------------------------")
    print("Title:", book['title'])
    print("Author:", book['author'])
    print("Genre:", book['genre'])
    print("Description:", book['description'])
    print("ISBN:", book['isbn'])
    print("Image:", book['image'])
    print("Published:", book['published'])
    print("Publisher:", book['publisher'])
    print("-----------------------------")

kitten_image = obtener_imagen_gatitos()
if kitten_image is not None:
    print("Kitten image data obtained:")
    print("-----------------------------")
    print("Title:", kitten_image['title'])
    print("Description:", kitten_image['description'])
    print("URL:", kitten_image['url'])
    print("-----------------------------")