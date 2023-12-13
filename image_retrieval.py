'''
Elijah Hart
cst205
Description: this module handles the retrieval of images from the URLs input by the user.
'''

from PIL import Image
import requests
from bs4 import BeautifulSoup
import os

def save_image(img_data, filename):
    with open(filename, 'wb') as f:
        f.write(img_data)

def get_image_url(self, url, is_background=True):
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            img_tags = soup.find_all('img')

            images_list = []
            for img_tag in img_tags:
                img_url = img_tag.get('src')
                if img_url:
                    img_data = requests.get(img_url).content
                    img = Image.open(io.BytesIO(img_data))
                    images_list.append(img)

            if is_background:
                self.bg_images = images_list
            else:
                self.subject_images = images_list

            if images_list:
                return images_list
            else:
                print(f"No images found on the page.")
                return None

        except requests.RequestException as e:
            print(f"Error retrieving images from URL: {e}")
            return None