import time
from selenium import webdriver
driver = webdriver.Chrome("/Users/wzz/Desktop/chromedriver")
driver.get("file:///Users/wzz/Desktop/Research/scriptRepair/WebRL/website/instructure/old/index.html")
el = driver.find_element_by_xpath("/html[1]/body[1]/header[1]/nav[1]/div[1]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/header[1]/nav[1]/div[1]/span[1]/a[6]")
