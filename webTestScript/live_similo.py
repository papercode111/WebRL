import time
from selenium import webdriver
driver = webdriver.Chrome("/Users/wzz/Desktop/chromedriver")
driver.get("file:///Users/wzz/Desktop/Research/scriptRepair/WebRL/website/live/old/web.archive.org/web/20170801034526/https:/outlook.live.com/owa/index.html")
el = driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[1]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[2]/div[2]/div[1]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]")
