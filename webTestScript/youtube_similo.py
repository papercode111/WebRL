import time
from selenium import webdriver
driver = webdriver.Chrome("/Users/wzz/Desktop/chromedriver")
driver.get("file:///Users/wzz/Desktop/Research/scriptRepair/WebRL/website/youtube/old/index.html")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[4]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/ul[1]/li[3]/a[1]/span[1]/span[2]/span[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[4]/div[2]/div[2]/div[1]/div[3]/form[1]/div[1]/input[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[4]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/ul[1]/li[1]/a[1]/span[1]/span[2]/span[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[4]/div[2]/div[2]/div[1]/div[1]/button[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[4]/div[2]/div[2]/div[1]/div[3]/form[1]/button[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[4]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/ul[1]/li[2]/a[1]/span[1]/span[2]/span[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[4]/div[2]/div[2]/div[1]/div[1]/span[1]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[4]/div[2]/div[2]/div[1]/div[2]/div[1]/button[1]")
