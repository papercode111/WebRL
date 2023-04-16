import time
from selenium import webdriver
driver = webdriver.Chrome("/Users/wzz/Desktop/chromedriver")
driver.get("file:///Users/wzz/Desktop/Research/scriptRepair/WebRL/website/microsoftonline/old/index.html")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/form[1]/div[2]/div[1]/div[1]/a[2]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/input[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/input[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/form[1]/div[2]/div[1]/div[1]/a[1]")
