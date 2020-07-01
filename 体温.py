# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import datetime

login_url = "http://ehall.ujn.edu.cn/fp"
driver = webdriver.Chrome()
driver.get(login_url)

stu_id = 'your ID'
stu_psw = 'your password'
morning = '36.5'
afternoon = '36.5'

driver.find_elements_by_xpath('/html/body/form/div/div[2]/div/div[3]/input[1]')[0].send_keys(stu_id)
driver.find_elements_by_xpath('/html/body/form/div/div[2]/div/div[3]/input[2]')[0].send_keys(stu_psw)
#点击按钮
driver.find_elements_by_xpath('/html/body/form/div/div[2]/div/div[3]/span/input')[0].click()
driver.implicitly_wait(5)
driver.find_elements_by_xpath('//*[@title="健康状况每日填报"]')[0].click()
driver.implicitly_wait(5)
driver.find_elements_by_xpath('//*[@id="layui-layer1"]/div[@class="layui-layer-content"]/div/div/div[@class="modal-footer"]/button[@class="btn btn-primary pull-right"]')[0].click()

driver.implicitly_wait(5)
driver.switch_to_frame("formIframe")
driver.find_elements_by_xpath('/html/body/div[1]/div[8]/div[2]/input')[0].send_keys(morning)
driver.find_elements_by_xpath('/html/body/div[1]/div[8]/div[4]/input')[0].send_keys(afternoon)
driver.switch_to.default_content()
driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div[8]/div/div[2]/div/div[2]/div/div/div[4]/div/div[2]/div[1]/div/div[3]/div[1]/button')[0].click()

