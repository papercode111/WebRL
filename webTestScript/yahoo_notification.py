#coding=utf-8
#oldUrl="http://web.archive.org/web/20200107001908/https://www.yahoo.com/"
#newUrl="http://web.archive.org/web/20220221000940/https://www.yahoo.com/"
#file:///Users//Desktop/webProject/yahoo2020/Yahoo.html
#file:///Users//Desktop/webProject/yahoo2022/Yahoo%20_%20Mail,%20Weather,%20Search,%20Politics,%20News,%20Finance,%20Sports%20&%20Videos.html
import time
from selenium import webdriver
driver=webdriver.Chrome("/Users//Desktop/chromedriver")
driver.get("file:///Users//Desktop/webProject/yahoo2020/Yahoo.html")
# driver.get("file:///Users//Desktop/webProject/yahoo2022/Yahoo%20_%20Mail,%20Weather,%20Search,%20Politics,%20News,%20Finance,%20Sports%20&%20Videos.html")
# notification
el=driver.find_element_by_id("header-notification-button")
el.click()
driver.quit()