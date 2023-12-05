'''
Elijah Hart
cst205
Description: this module handles the retrieval of images from the URLs input by the user.
'''

import requests
from bs4 import BeautifulSoup

def get_image_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        img_tag = soup.find('img')
        if img_tag:
            img_url = img_tag.get('src')
            if img_url:
                img_data = requests.get(img_url).content
                return img_data
            else:
                print("Image source ('src') attribute not found")
        else:
            print("No 'img' tag found in the HTML content.")
    except requests.RequestException as e: 
        print(f"Error retrieving image from URL: {e}")
        return None

