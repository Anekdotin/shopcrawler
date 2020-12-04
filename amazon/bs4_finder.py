from bs4 import BeautifulSoup


def find_data_amazon_url(driver,url):

    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    if soup.findAll(text="In Stock."):
        print("Status: IN STOCK!!!!!")
    else:
        print("Status: out of stock")
