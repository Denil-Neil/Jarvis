import requests
from plugin import plugin, require
from PIL import Image
from io import BytesIO


image_url = ""
@require(network=True)
@plugin("cat")
def get_random_cat_image(jarvis, s):
    url = "https://api.thecatapi.com/v1/images/search"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()  # Parse the JSON response
        
        if data:
            image_url = data[0]['url']
            jarvis.say(f"Cat image URL: {image_url}")  # Print the URL using jarvis
            display_image(image_url)
        else:
            jarvis.say("No cat images found.")
    
    except requests.exceptions.RequestException as e:
        jarvis.say(f"An error occurred: {e}")

@plugin("cat image")
def display_image(jarvis,image_url ):
    try:
        response = requests.get(image_url)
        response.raise_for_status()  # Check if the request was successful
        img_data = response.content
        image = Image.open(BytesIO(img_data))
        image.show()  # This will open the image in the default image viewer
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
