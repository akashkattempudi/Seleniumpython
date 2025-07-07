import json
import time


from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest

from Login import Loginpage
path = "test_t.json"
with open(path) as p:
    data = json.load(p)
    lista= data["data"]
@pytest.mark.smoke
@pytest.mark.parametrize("z",lista)
def test_1(sample,z):
    a = sample
    a.get("https://rahulshettyacademy.com/loginpagePractise/")
    Loginpage(a).login(z["id"],z["password"])
    Loginpage(a).cart(z["name"])
    Loginpage(a).checkout(z["country_name"])




