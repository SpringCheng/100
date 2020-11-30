# -*- coding: utf-8 -*-
# @Time    : 2020/11/30 0030 下午 11:28
# @Author  : CC1111
import time

from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://www.baidu.com')

# 1.先找到鼠标要操作的元素
ele=driver.find_element_by_xpath('//div[@id="u1"]//span[@name="tj_settingicon"]')

# 2.实例化ActionChains类
# ac=AC(driver)
# # 3.将鼠标操作添加到actions列表中
# ac.move_to_element(ele)
# # 4.调用perform()来执行鼠标操作
# ac.perform()

# 2 3 4步能够合成一步
AC(driver).move_to_element(ele).perform()

# 选择下拉列表中的高级搜索
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[text()="高级搜索"]')))
driver.find_element_by_xpath('//a[text()="高级搜索"]').click()


time.sleep(3)
driver.quit()