#coding=utf-8
#oldUrl="http://web.archive.org/web/20180525002632/https://www.amazon.com/"
#newUrl="http://web.archive.org/web/20200721002358/https://www.amazon.com/"
import time
from selenium import webdriver
driver=webdriver.Chrome("/Users//Desktop/chromedriver")
driver.get("file:///Users//Desktop/webProject/amazon2018/index.html")
#driver.get("https://web.archive.org/web/20191101060559/https://www.w3schools.com/")
#home
el=driver.find_element_by_xpath("//*[@id=\"nav-logo\"]/a[1]")
el.click()















