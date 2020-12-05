
import requests
import random

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.proxy import Proxy, ProxyType

from lxml.html.soupparser import fromstring
from secret import my_ip

from app.crawler_amazon.video_cards_nvidia_3080 import *
from app.crawler_amazon.video_cards_nvidia_3090 import *
from app.crawler_amazon.video_cards_nvidia_3070 import *
from app.crawler_amazon.video_cards_nvidia_3060 import *

from app.crawler_newegg.video_cards_nvidia_3080 import *
from app.crawler_newegg.video_cards_nvidia_3090 import *
from app.crawler_newegg.video_cards_nvidia_3070 import *
from app.crawler_newegg.video_cards_nvidia_3060 import *

bannedproxy = []
proxylist = []
use_proxy = 0


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

    if use_proxy == 1:
        randomproxy = getgoodproxy()
        myproxy = randomproxy

        proxy = Proxy({
            'proxyType': ProxyType.MANUAL,
            'httpProxy': myproxy,
            'ftpProxy': myproxy,
            'sslProxy': myproxy,
            'noProxy': ''
        })
        print(f"{TerminalColors.ENDC}using proxy {myproxy}")
        binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")

        capabilities = webdriver.DesiredCapabilities.FIREFOX
        proxy.add_to_capabilities(capabilities)

        options = Options()
        options.headless = True
        profile = webdriver.FirefoxProfile()
        profile.accept_untrusted_certs = True
        profile.set_preference("browser.privatebrowsing.autostart", True)

        driver = webdriver.Firefox(options=options,
                                   desired_capabilities=capabilities,
                                   firefox_profile=profile,
                                   firefox_binary=binary,
                                   executable_path="./geckodriver.exe")
        driver.implicitly_wait(5)
    else:
        binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")

        options = Options()
        options.headless = True
        profile = webdriver.FirefoxProfile()
        profile.accept_untrusted_certs = True
        profile.set_preference("browser.privatebrowsing.autostart", True)

        driver = webdriver.Firefox(options=options,
                                   firefox_profile=profile,
                                   firefox_binary=binary,
                                   executable_path="./geckodriver.exe")

    return driver


def check_proxy_ok(driver):
    url = 'https://whatismyipaddress.com/ip-lookup'

    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    for div in soup.findAll('span', {'id': 'ip'}):
        print(f"My IP:        {my_ip}")
        print(f"Appearing as: {div.text}")
        if str(my_ip == div.text):
            print("Proxy not working!")
        else:
            print("good to go my friend")
        return div.text


def main():
    driver = selenium_getter()

    # 3060
    nvidia_3060_asustuf(driver=driver)
    time.sleep(3)

    newegg_3060(driver=driver)

    # 3070

    nvidia_3070_pny(driver=driver)
    time.sleep(3)

    newegg_3070(driver=driver)

    # 3080

    print("")
    time.sleep(3)
    nvidia_3080_zotac(driver=driver)
    time.sleep(3)
    nvidia_3080_asustuf(driver=driver)
    time.sleep(3)
    nvidia_3080_pny(driver=driver)
    time.sleep(3)
    newegg_3080(driver=driver)
    nvidia_3080_msi(driver=driver)
    time.sleep(3)
    nvidia_3080_evga(driver=driver)
    time.sleep(3)
    nvidia_3080_gigabyte(driver=driver)
    time.sleep(3)

    # 3090

    nvidia_3090_zotac(driver=driver)
    time.sleep(3)
    nvidia_3090_asus(driver=driver)
    time.sleep(3)
    nvidia_3090_pny(driver=driver)
    time.sleep(3)
    newegg_3090(driver=driver)
    nvidia_3090_msi(driver=driver)
    time.sleep(3)
    nvidia_3090_gigabyte(driver=driver)

    driver.close()


while True:
    main()
