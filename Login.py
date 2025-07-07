import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
class Loginpage:
    def __init__(self,a):
        self.username = (By.CSS_SELECTOR, "#username")
        self.password = (By.CSS_SELECTOR, "#password")
        self.signin= (By.ID,"signInBtn")
        self.items = (By.XPATH, "//div[@class='card h-100']")
        self.item = (By.XPATH, "div/h4/a")
        self.addtocart = (By.XPATH, "div/button")
        self.cartitem= (By.CSS_SELECTOR, ".nav-link.btn.btn-primary")
        self.button = (By.CSS_SELECTOR, "button[class='btn btn-success']")
        self.name = (By.ID, "country")
        self.drop = (By.LINK_TEXT, "India")
        self.chkbox = (By.CSS_SELECTOR, "label[for='checkbox2']")
        self.cnf = (By.CSS_SELECTOR, "input[value='Purchase']")
        self.alert = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
        self.a = a

    def login(self,id,password):
        self.a.find_element(*self.username).send_keys(id)
        self.a.find_element(*self.password).send_keys(password)
        self.a.find_element(*self.signin).click()

    def cart(self,name):
        b = self.a.find_elements(*self.items)
        for i in b:
            if i.find_element(*self.item).text == name:
                i.find_element(*self.addtocart).click()
        self.a.find_element(*self.cartitem).click()
    def checkout(self,country_name):
        self.a.find_element(*self.button).click()
        self.a.find_element(*self.name).send_keys(country_name)
        wait = WebDriverWait(self.a, 5)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.a.find_element(*self.drop).click()
        self.a.find_element(*self.chkbox).click()
        self.a.find_element(*self.cnf).click()
        print(self.a.find_element(*self.alert).text)


