
from .bs4_finder import find_data_amazon_url


def nvidia_3070_pny(driver):
    url = 'https://www.amazon.com/PNY-GeForce-Gaming-Epic-X-Graphics/dp/B08HBJB7YD?ref_=ast_sto_dp'
    title = "PNY GeForce RTX 3070 8GB"
    find_data_amazon_url(driver, url, title, typeofcard=3070)


