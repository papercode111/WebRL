import time
from selenium import webdriver
driver = webdriver.Chrome("/Users/wzz/Desktop/chromedriver")
driver.get("file:///Users/wzz/Desktop/Research/scriptRepair/WebRL/website/bing/old/index.html")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[2]/form[1]/input[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/header[1]/div[1]/div[1]/a[1]/span[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/header[1]/div[1]/div[1]/a[4]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[2]/form[1]/label[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/header[1]/ul[1]/li[1]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/header[1]/div[1]/div[1]/a[1]/span[2]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/header[1]/div[1]/div[1]/a[2]/span[2]/span[1]/*[local-name()")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/header[1]/ul[1]/li[2]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/header[1]/div[1]/div[1]/a[2]/span[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/img[1]")
