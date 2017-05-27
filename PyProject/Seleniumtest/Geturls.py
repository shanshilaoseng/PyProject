#!/usr/bin/python
# coding:utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def Geturls(url, username='', password=''):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)

    # print driver.current_window_handle

    # driver.find_element_by_class_name('u_login').click()
    # time.sleep(3)


    # print driver.current_window_handle
    try:
        # element = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.ID, "passport-login-pop"))
        # )
        # driver.find_element_by_id('passport-login-pop').find_element_by_name('userName').send_keys(username)
        # driver.find_element_by_id('passport-login-pop').find_element_by_name('password').send_keys(password)
        # driver.find_element_by_id('passport-login-pop').find_element_by_class_name('pass-form-item-submit').click()
        #
        # time.sleep(3)
        #
        link_list = []
        # print link_list
        links = driver.find_elements_by_css_selector('.content a')
        # print links
        for i in links:
            print i.get_attribute('href')

            link_list.append(i.get_attribute('href'))

        print link_list

        time.sleep(2)

    finally:
        driver.quit()


        # print driver.page_source


url_var = 'http://www.lovecaobi.com/'
# user = u'方丈20'
# passwd = '1991a1112.zaq'
Geturls(url_var)
