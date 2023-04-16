import time
from selenium import webdriver
driver = webdriver.Chrome("/Users/wzz/Desktop/chromedriver")
driver.get("file:///Users/wzz/Desktop/Research/scriptRepair/WebRL/website/zoom/old/index.html")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[4]/div[2]/form[1]/div[7]/div[1]/button[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[2]/ul[2]/li[3]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[5]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[1]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[4]/div[2]/form[1]/div[7]/div[1]/input[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[2]/ul[2]/li[2]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[2]")
