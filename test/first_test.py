from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display

'''for starting virtual display'''
display = Display(size=(1920, 1080))
display.start()

'''for opening firefox'''
profile = webdriver.FirefoxProfile()
profile.set_preference('general.useragent.override', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
driver = webdriver.Firefox(profile)




driver.get('https://www.wikipedia.org')
print driver.title

# print driver.page_source
elem =  driver.find_element_by_id('searchInput')
elem.send_keys('Simpy')
esc_elem = driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
esc_elem.click()
print 'clicked'
sleep(10)

heading1 = driver.find_element_by_tag_name('h1')

print heading1.text

pagal = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/p[1]')
print pagal.text
'''only close particular tab'''
driver.close()
# driver.quit()
display.stop()