from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()

browser.get('https:/www.instagram.com/')

sleep(5)

browser.close()
