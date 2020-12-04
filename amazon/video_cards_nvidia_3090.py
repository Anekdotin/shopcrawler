from .bs4_finder import find_data_amazon_url


def nvidia_3090_zotac(driver):
    url = 'https://www.amazon.com/ZOTAC-Graphics-IceStorm-Advanced-ZT-A30900D-10P/dp/B08HJQ182D?ref_=ast_sto_dp'
    title = "ZOTAC Gaming GeForce RTX 3090 Trinity 24GB"
    find_data_amazon_url(driver, url, title)


def nvidia_3090_pny(driver):
    url = 'https://www.amazon.com/PNY-GeForce-Gaming-Epic-X-Graphics/dp/B08HBQWBHH?ref_=ast_sto_dp'
    title = "PNY GeForce RTX 3090 24GB "
    find_data_amazon_url(driver, url, title)


def nvidia_3090_msi(driver):
    url = 'https://www.amazon.com/MSI-GeForce-RTX-3090-24G/dp/B08HRBW6VB?ref_=ast_sto_dp'
    title = "MSI Gaming GeForce RTX 3090 24GB "
    find_data_amazon_url(driver, url, title)


def nvidia_3090_gigabyte(driver):
    url = 'https://www.amazon.com/Gigabyte-Graphics-WINDFORCE-GV-N3090GAMING-OC-24GD/dp/B08HJRF2CN?ref_=ast_sto_dp'
    title = "Gigabyte GeForce RTX 3090 GAMING OC 24G"
    find_data_amazon_url(driver, url, title)


def nvidia_3090_asus(driver):
    url = 'https://www.amazon.com/Gigabyte-Graphics-WINDFORCE-GV-N3090GAMING-OC-24GD/dp/B08HJRF2CN?ref_=ast_sto_dp'
    title = "ASUS TUF Gaming NVIDIA GeForce RTX 3090 OC Edition Graphics Card 24GB"
    find_data_amazon_url(driver, url, title)
