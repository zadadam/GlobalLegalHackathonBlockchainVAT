from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("./chromedriver")
#driver.get("http://www.python.org")
#assert "Python" in driver.title
#elem = driver.find_element_by_name("q")
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()

driver = webdriver.Chrome("./chromedriver")
driver.get("https://ppuslugi.mf.gov.pl/")

time.sleep(15)
elem = driver.find_element_by_class_name("SidebarLinkChVAT")
elem.click()

time.sleep(10)
elem = driver.find_element_by_id("b-7")
elem.send_keys("5252128067"); # Witkacy
elem = driver.find_element_by_id("b-8")
elem.click()
elem = driver.find_element_by_id("caption2_b-3")
wynik = elem.text

print wynik
print driver.page_source