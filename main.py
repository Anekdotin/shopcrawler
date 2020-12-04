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


bannedproxy = []
proxylist = []


def get_proxies():

    print("Getting new Proxies")

    url = 'https://free-proxy-list.net/'
    response = requests.get(url)

    parser = fromstring(response.text)
    for i in parser.xpath('//tbody/tr')[:30]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxyifound = ":".join([i.xpath('.//td[1]/text()')[0],
                                    i.xpath('.//td[2]/text()')[0]])
            proxylist.append(proxyifound)

    print("Found " + str(len(proxylist)) + " proxies")


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
    print(f"using proxy {myproxy}")
    binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")

    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, proxy=proxy, firefox_binary=binary, executable_path="./geckodriver.exe")

    return driver


def main():

    driver = selenium_getter()

    nvidia_3080_zotac(driver)

    print("Amazon 3080 finder Starting .. ")
    nvidia_3080_asustuf(driver=driver)
    nvidia_3080_pny(driver=driver)
    nvidia_3080_pny_2(driver=driver)
    nvidia_3080_msi_1(driver=driver)
    nvidia_3080_msi_2(driver=driver)
    nvidia_3080_evga_1(driver=driver)
    nvidia_3080_evga_2(driver=driver)
    nvidia_3080_evga_3(driver=driver)
    nvidia_3080_evga_4(driver=driver)
    nvidia_3080_evga_5(driver=driver)
    nvidia_3080_gigabyte_1(driver=driver)
    nvidia_3080_gigabyte_2(driver=driver)

    print("Newegg 3080 starting .. ")

main()
