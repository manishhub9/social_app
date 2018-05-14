import requests
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display

'''for starting virtual display'''
# display = Display(size=(1920, 1080))
# display.start()

'''for opening firefox'''
# profile = webdriver.FirefoxProfile()
# profile.set_preference('general.useragent.override', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
# driver = webdriver.Firefox(profile)


searchText = 'computer'
searchGoogle = 'https://www.google.com.np/#q=' + searchText

html_page = requests.get(searchGoogle)

print html_page.content


# html_content = driver.page_source

# bsObj = BeautifulSoup(html_content, 'lxml')

# elements = bsObj.findAll("h3", {"class": "r"})

# print elements

'''only close particular tab'''
# driver.close()
# driver.quit()
# display.stop()
