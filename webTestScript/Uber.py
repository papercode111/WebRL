#coding=utf-8
#oldUrl="http://web.archive.org/web/20200521020213/https://www.uber.com/"
#newUrl="https://web.archive.org/web/20220217031516/https://www.uber.com/"
import time
from selenium import webdriver
driver=webdriver.Chrome("/Users//Desktop/chromedriver")
driver.get("http://web.archive.org/web/20200521020213/https://www.uber.com/")
el=driver.find_element_by_xpath("//*[@id=\"0\"]/div/div")
# eat button
el.click()