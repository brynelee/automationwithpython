#! /usr/bin/python3

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Cracking Codes with Python')
print(type(linkElem))
linkElem.click()
