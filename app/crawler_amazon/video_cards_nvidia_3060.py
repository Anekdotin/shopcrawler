
from .bs4_finder import find_data_amazon_url


def nvidia_3060_asustuf(driver):
    url = 'https://www.amazon.com/ASUS-Premium-GeForce-Keyboard-Included/dp/B083Z5P6TX'
    title = "ASUS TUF Gaming NVIDIA GeForce RTX 3060 Ti 8gb"
    find_data_amazon_url(driver, url, title)


