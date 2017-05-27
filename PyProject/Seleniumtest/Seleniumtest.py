#!/usr/bin/python
#coding:utf-8

from selenium import webdriver

driver = webdriver.PhantomJS()

driver.get('http://i.firefoxchina.cn/')
cookie_r = driver.get_cookies()
print cookie_r

#cookies
cookie_list = []
for i in cookie_r:
    cookie = i['name'] + '=' + i['value']
    cookie_list.append(cookie)
    cookie_str = ';'.join(cookie_list)
print cookie_str

#js
js_code = 'return document.cookie'
cookies = driver.execute_script(js_code)
print cookies