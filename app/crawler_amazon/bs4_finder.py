from bs4 import BeautifulSoup
import time
from datetime import datetime
from app import db

from app.models import Nvidia3060, Nvidia3080, Nvidia3090, Nvidia3070
from app.addtodb import outta_stock, add_data

class TerminalColors:

    HEADER = '\033[95m'
    BLACK = '\033[40m'
    WHITE = '\033[47m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def find_data_amazon_url(driver, url, title, typeofcard):
    now = datetime.now()
    try:
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        current_time = now.strftime("%H:%M:%S")

        print(f"{TerminalColors.HEADER}[{current_time}] {TerminalColors.OKCYAN}Amazon {TerminalColors.ENDC}  {title}")

        if soup.findAll(text="In Stock."):
            print(f"{TerminalColors.ENDC}Status:  {TerminalColors.OKGREEN}In Stock!!!!!")
            add_data(typeofitem=typeofcard,
                     seller=1,
                     url=url)
        else:
            print(f"{TerminalColors.ENDC}Status:  {TerminalColors.FAIL}OUT OF STOCK")
            outta_stock(typeofitem=typeofcard, seller=1)
        print("")

    except:
        pass