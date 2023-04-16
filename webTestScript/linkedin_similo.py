import time
from selenium import webdriver
driver = webdriver.Chrome("/Users/wzz/Desktop/chromedriver")
driver.get("file:///Users/wzz/Desktop/Research/scriptRepair/WebRL/website/linkedin/old/web.archive.org/web/20170802004444/https:/www.linkedin.com/index.html")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/form[1]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/form[1]/input[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/form[1]/input[3]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/form[1]/input[2]")
