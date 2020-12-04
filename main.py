from config import proxy_enabled
import requests
import random
from random import randrange

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.proxy import Proxy, ProxyType
from fake_useragent import UserAgent
from lxml.html.soupparser import fromstring

from amazon.video_cards_nvidia_3080 import *
from amazon.video_cards_nvidia_3090 import *
from newegg.video_cards_nvidia_3080 import *
from newegg.video_cards_nvidia_3090 import *


bannedproxy = []
proxylist = []


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


def get_proxies():

    print("Getting new Proxies")

    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    print(response)
    parser = fromstring(response.text)
    for i in parser.xpath('//tbody/tr')[:300]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxyifound = ":".join([i.xpath('.//td[1]/text()')[0],
                                    i.xpath('.//td[2]/text()')[0]])
            proxylist.append(proxyifound)

    print(TerminalColors.ENDC + "Found " + str(len(proxylist)) + " proxies")


def getgoodproxy():
    get_proxies()
    randomproxy = (random.choice(proxylist))
    return randomproxy


def selenium_getter():
    randomproxy = getgoodproxy()
    myproxy = randomproxy

    proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': myproxy,
        'ftpProxy': myproxy,
        'sslProxy': myproxy,
        'noProxy': ''
    })
    print(f"{TerminalColors.ENDC}  using proxy {myproxy}")
    binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")

    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, proxy=proxy, firefox_binary=binary, executable_path="./geckodriver.exe")

    return driver


def main():

    driver = selenium_getter()

    print(TerminalColors.ENDC + "Amazon 3080 starting .. ")
    nvidia_3080_zotac(driver=driver)
    nvidia_3080_asustuf(driver=driver)
    nvidia_3080_pny(driver=driver)
    nvidia_3080_msi(driver=driver)
    nvidia_3080_evga(driver=driver)
    nvidia_3080_gigabyte(driver=driver)

    print(TerminalColors.ENDC + "Amazon 3090 starting .. ")
    nvidia_3090_zotac(driver=driver)
    nvidia_3090_asus(driver=driver)
    nvidia_3090_pny(driver=driver)
    nvidia_3090_msi(driver=driver)
    nvidia_3090_gigabyte(driver=driver)

    print(TerminalColors.ENDC + "Newegg 3080 starting .. ")
    newegg_3080(driver=driver)

    print(TerminalColors.ENDC + "Newegg 3090 starting .. ")
    newegg_3090(driver=driver)


while True:
    main()
