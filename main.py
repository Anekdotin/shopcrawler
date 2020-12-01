from config import proxy_enabled

import time
import random
import sys

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from lxml.html.soupparser import fromstring
from lxml.html import fromstring
from lxml import html

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.proxy import Proxy, ProxyType


proxylist = []

amazonid = 'B08HJNKT3P'


def get_proxies():

    print("Getting new Proxies")
    sys.stdout.flush()

    url = 'https://free-proxy-list.net/'
    response = requests.get(url)

    parser = fromstring(response.text)
    for i in parser.xpath('//tbody/tr')[:50]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxyifound = ":".join([i.xpath('.//td[1]/text()')[0],
                                    i.xpath('.//td[2]/text()')[0]])
            proxylist.append(proxyifound)
    print("Found " + str(len(proxylist)) + " proxies")
    sys.stdout.flush()


def getgoodproxy():
    if len(proxylist) < 20:
        get_proxies()
    randomproxy = (random.choice(proxylist))
    return randomproxy


def proxy_enabled_page():
    randomproxy = getgoodproxy()

    # get all items
    urltogetforitems = "http://www.amazon.com/dp/" + amazonid
    print("Using proxy:", randomproxy)

    # Pick a random user agent
    ua = UserAgent()
    user_agent = ua.random
    # Set the headers
    headers = {'User-Agent': user_agent}
    # Make the request

    proxy1 = str("http://") + str(randomproxy)
    proxy2 = str("https://") + str(randomproxy)
    proxies = {proxy1:
                   proxy2}

    # Attemp to contact amazon
    response = requests.get(urltogetforitems,
                        proxies=proxies,
                        headers=headers,
                        timeout=10)
    return response


def non_proxy_page():

    # get all items
    urltogetforitems = "http://www.amazon.com/dp/" + amazonid

    ua = UserAgent()
    user_agent = ua.random
    # Set the headers
    headers = {'User-Agent': user_agent}
    # Make the request

    # Attemp to contact amazon
    response = requests.get(urltogetforitems,
                        headers=headers,
                        timeout=10)

    return response


def selenium_getter():
    binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    driver = webdriver.Firefox(firefox_binary=binary, executable_path="./geckodriver.exe")
    driver.get("http://www.amazon.com")

    if "Amazon" in driver.title:
        print("success")

    return driver

def my_proxy(PROXY_HOST, PROXY_PORT):
    fp = webdriver.FirefoxProfile()
    # Direct = 0, Manual = 1, PAC = 2, AUTODETECT = 4, SYSTEM = 5
    print
    PROXY_PORT
    print
    PROXY_HOST
    fp.set_preference("network.proxy.type", 1)
    fp.set_preference("network.proxy.http", PROXY_HOST)
    fp.set_preference("network.proxy.http_port", int(PROXY_PORT))
    fp.set_preference("general.useragent.override", "whater_useragent")
    fp.update_preferences()
    return webdriver.Firefox(firefox_profile=fp)


def main():
    if proxy_enabled is True:
        response = proxy_enabled_page()
    else:
        response = non_proxy_page()

    print(response.status_code)

    if response.status_code == 504:
        print("504 error: Timeout")

    elif response.status_code == 503:
        print("503 error: Unavailable")

    elif response.status_code == 200:
        c = response.content
        soup = BeautifulSoup(c, 'html.parser')
        # get soup information
        doc = html.fromstring(response.content)

        print(soup.prettify())


selenium_getter()
