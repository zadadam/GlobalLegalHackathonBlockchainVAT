from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.common.by as By
import time

driver = webdriver.Chrome("./chromedriver")

driver = webdriver.Chrome("./chromedriver")
driver.get("https://ppuslugi.mf.gov.pl/")

time.sleep(10)
elem = driver.find_element_by_class_name("SidebarLinkChVAT")
elem.click()

time.sleep(5)
elem = driver.find_element_by_id("b-7")
elem.send_keys("5252128067") # Witkacy
#elem.send_keys("5261032852") # Oninnen
elem = driver.find_element_by_id("b-8")
elem.click()
time.sleep(3)
elem = driver.find_element_by_id("caption2_b-3")
wynik = elem.text

print wynik
#print driver.page_source

#driver.close()