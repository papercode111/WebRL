import time
from selenium import webdriver
driver = webdriver.Chrome("/Users/wzz/Desktop/chromedriver")
driver.get("file:///Users/wzz/Desktop/Research/scriptRepair/WebRL/website/zillow/old/web.archive.org/web/20170801174330/https:/www.zillow.com/index.html")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[2]/main[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/button[1]/span[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/header[1]/nav[1]/div[1]/div[2]/section[3]/header[1]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/header[1]/nav[1]/div[1]/div[1]/div[1]/section[1]/div[2]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/header[1]/nav[1]/div[1]/div[1]/section[1]/div[1]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/header[1]/nav[1]/div[1]/div[2]/section[1]/header[1]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/header[1]/nav[1]/div[1]/div[2]/section[5]/header[1]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[2]/main[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/header[1]/nav[1]/div[1]/div[2]/section[2]/header[1]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/header[1]/nav[1]/div[1]/div[1]/div[1]/section[2]/div[1]/a[1]")
