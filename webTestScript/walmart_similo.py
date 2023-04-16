import time
from selenium import webdriver
driver = webdriver.Chrome("/Users/wzz/Desktop/chromedriver")
driver.get("file:///Users/wzz/Desktop/Research/scriptRepair/WebRL/website/walmart/old/index.html")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/header[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/form[1]/div[1]/div[2]/div[1]/label[1]/input[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/header[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[7]/div[1]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/header[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/header[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/form[1]/div[1]/div[3]/button[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/header[1]/div[1]/div[2]/div[1]/div[1]/nav[1]/div[1]/a[3]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/header[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/form[1]/div[1]/div[1]/div[1]/button[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/header[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[2]/button[1]")
