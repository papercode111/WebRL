import time
from selenium import webdriver
driver = webdriver.Chrome("/Users/wzz/Desktop/chromedriver")
driver.get("file:///Users/wzz/Desktop/Research/scriptRepair/WebRL/website/twitch/old/index.html")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/a[2]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/form[1]/input[2]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/a[1]/*[local-name() = "svg"][1]")
