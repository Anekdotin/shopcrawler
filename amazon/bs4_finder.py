from bs4 import BeautifulSoup
import time
from datetime import datetime

now = datetime.now()


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


def find_data_amazon_url(driver, url, title):

    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    current_time = now.strftime("%H:%M:%S")

    print(f"{TerminalColors.HEADER}[{current_time}] {TerminalColors.ENDC}  {title[0:40]}..")
    print(f"{TerminalColors.OKBLUE}Amazon")

    if soup.findAll(text="In Stock."):
        print(f"{TerminalColors.ENDC}Status:  {TerminalColors.OKGREEN}In Stock!!!!!")
    else:
        print(f"{TerminalColors.ENDC}Status:  {TerminalColors.FAIL}out of stock")
    print("")