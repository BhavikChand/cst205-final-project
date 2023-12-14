'''
Elijah Hart
cst205
Description: this module handles the retrieval of images from the URLs input by the user.
'''

from PIL import Image
import requests
from bs4 import BeautifulSoup

def save_image(img_data, filename):
    with open(filename, 'wb') as f:
        f.write(img_data)

def get_image_url(index):
        try:
            response = requests.get("https://www.nasa.gov")
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            img_tags = soup.find_all('img')
            return Image.open(requests.get(img_tags[index]['src'], stream = True).raw)
            

        except requests.RequestException as e:
            print(f"Error retrieving images from URL: {e}")
            return None