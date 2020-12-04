
from bs4 import BeautifulSoup
import time
from datetime import datetime


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


def newegg_3080(driver):
    url = 'https://www.newegg.com/p/pl?N=100007709%20601357247'
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    for div in soup.findAll('div', {'class': 'item-info'}):
        time.sleep(1)

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        tdtags = div.find_all("a", {"class": "item-title"})
        for tag in tdtags:

            promotag = div.find_all("p", {"class": "item-promo"})
            for promo in promotag:
                print(f"{TerminalColors.HEADER}[{current_time}] {TerminalColors.ENDC}  {tag.text[0:40]}..")
                print(f"{TerminalColors.OKBLUE}Newegg")
                if promo.text == 'OUT OF STOCK':
                    print(f"{TerminalColors.ENDC}Status:  {TerminalColors.FAIL}{promo.text}")
                else:
                    print(f"{TerminalColors.ENDC}Status:  {TerminalColors.OKGREEN}{promo.text}")
                print("")

