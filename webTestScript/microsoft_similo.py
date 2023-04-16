import time
from selenium import webdriver
driver = webdriver.Chrome("/Users/wzz/Desktop/chromedriver")
driver.get("file:///Users/wzz/Desktop/Research/scriptRepair/WebRL/website/microsoft/old/web.archive.org/web/20160602024415/https:/www.microsoft.com/en-us/index.html")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/span[2]/div[1]/div[1]/div[1]/div[5]/form[1]/div[1]/button[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/span[2]/div[1]/div[1]/div[1]/div[1]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/span[2]/div[1]/div[1]/div[1]/div[5]/div[1]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/span[2]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[4]/a[1]")
