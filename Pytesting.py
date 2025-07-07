from time import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

a = webdriver.Chrome()
a.implicitly_wait(5)
a.get("https://rahulshettyacademy.com/seleniumPractise/#/")
print(a.find_element(By.CSS_SELECTOR,".cart-header-navlink.blinkingText").text)
a.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
sleep(2)
b = a.find_elements(By.XPATH,"//div[@class='products']/div")
for i in b:
    i.find_element(By.XPATH,"div/button").click()
d = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
b =a.find_elements(By.CSS_SELECTOR,"h4[class='product-name']")
c=[]
for i in b:
    c.append(i.text)
print(c)
assert c==d
a.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
sleep(1)
a.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
sleep(2)
z = a.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
x = 0
for i in z:
    x+=int(i.text)
print(x)

a.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
a.find_element(By.CSS_SELECTOR,".promoBtn").click()
W = WebDriverWait(a,10)
W.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR,".promoInfo")))
t = a.find_element(By.CSS_SELECTOR,".discountAmt").text
assert eval(t)<x
print(a.find_element(By.CSS_SELECTOR,".promoInfo").text)
