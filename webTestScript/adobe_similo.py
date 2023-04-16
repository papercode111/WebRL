import time
from selenium import webdriver
driver = webdriver.Chrome("/Users/wzz/Desktop/chromedriver")
driver.get("file:///Users/wzz/Desktop/Research/scriptRepair/WebRL/website/adobe/old/web.archive.org/web/20180702000525/https:/www.adobe.com/index.html")
el = driver.find_element_by_xpath("/html[1]/body[1]/main[1]/section[1]/figure[1]/article[1]/section[1]/ul[1]/li[1]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/main[1]/section[1]/figure[1]/article[1]/section[1]/ul[1]/li[2]/a[1]")
