import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from PageObject.locator import elem
from PageObject.locator import link
import baseLogin

class TestCart(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    def test_cart_success(self):
        # steps
        #login
        driver = self.browser #buka web browser
        baseLogin.positive_login(driver)
        #login.test_a_login_success(self)

        #cart
        driver.find_element(By.CSS_SELECTOR, elem.addProduk).click()
        time.sleep(1)
        driver.find_element(By.ID, elem.cart).click()
        time.sleep(2)

        #validasi
        response_url = driver.current_url
        self.assertEqual(response_url, link.cart)
        
if __name__ == "__main__":
    unittest.main()