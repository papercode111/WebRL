import time
from selenium import webdriver
driver = webdriver.Chrome("/Users/wzz/Desktop/chromedriver")
driver.get("file:///Users/wzz/Desktop/Research/scriptRepair/WebRL/website/indeed/old/index.html")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/span[2]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[1]/form[1]/table[1]/tbody[1]/tr[2]/td[1]/span[1]/input[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[2]/span[1]/div[2]/a[6]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[1]/p[1]/a[2]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/span[3]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[1]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/label[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[1]/form[1]/table[1]/tbody[1]/tr[2]/td[2]/span[1]/input[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[2]/span[1]/div[2]/a[3]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/span[1]/span[1]/a[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[2]/span[1]/div[2]/a[7]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[1]/form[1]/table[1]/tbody[1]/tr[1]/td[2]/label[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[1]/form[1]/table[1]/tbody[1]/tr[2]/td[3]/span[1]/span[1]/input[1]")
el = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[2]/span[1]/div[2]/a[1]")