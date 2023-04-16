import time
from selenium import webdriver
driver = webdriver.Chrome("/Users/wzz/Desktop/chromedriver")
driver.get("file:///Users/wzz/Desktop/Research/scriptRepair/WebRL/website/okta/old/web.archive.org/web/20171102031615/https:/www.okta.com/index.html")
el = driver.find_element_by_xpath("/html[1]/body[1]/header[1]/div[1]/div[2]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/header[1]/div[1]/nav[1]/ul[1]/li[3]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/header[1]/div[1]/nav[1]/ul[1]/li[6]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/header[1]/div[1]/div[3]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/header[1]/div[1]/h1[1]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/header[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/header[1]/div[1]/nav[1]/ul[1]/li[7]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/header[1]/div[1]/nav[1]/ul[1]/li[2]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/header[1]/div[1]/nav[1]/ul[1]/li[5]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/header[1]/div[1]/a[1]")
