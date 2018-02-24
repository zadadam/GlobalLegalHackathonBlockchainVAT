from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.common.by as By
import time


def getVATstatus(nip):
    """

    :param nip: string!!! nie liczba
    :return: status ze strony ministerstwa
    """

    driver = webdriver.Chrome("./chromedriver")

    driver = webdriver.Chrome("./chromedriver")
    driver.get("https://ppuslugi.mf.gov.pl/")

    time.sleep(7)
    elem = driver.find_element_by_class_name("SidebarLinkChVAT")
    elem.click()

    time.sleep(3)
    elem = driver.find_element_by_id("b-7")
    elem.send_keys(nip)
    #elem.send_keys("5252128067") # Witkacy
    #elem.send_keys("5261032852") # Oninnen
    elem = driver.find_element_by_id("b-8")
    elem.click()
    time.sleep(3)
    elem = driver.find_element_by_id("caption2_b-3")
    wynik = None
    wynik = elem.text

    print wynik

    driver.close()

    return {'nip':nip, 'result':wynik}

if __name__ == "__main__":
    for nip in ["5252128067", "5261032852"]:
        print getVATstatus(nip)