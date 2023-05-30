
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from PageObject.locator import elem
from PageObject.data import inputan
import baseLogin


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
 
    def test_a_success_login(self): #test case 1
     # steps
        driver = self.browser #buka web browser
        baseLogin.positive_login(driver)
    
    # validasi
        response_data = driver.find_element(By.CLASS_NAME,elem.produk).text
        self.assertIn(inputan.successLogin, response_data)
    
    def  test_b_login_failed_wrong_us(self): #test case 1
     # steps
        driver = self.browser #buka web browser
        baseLogin.negative_login_wrong_usn(driver)
    
    # validasi
        response_data = driver.find_element(By.CSS_SELECTOR,elem.invCreden).text
        self.assertIn(inputan.invalidCredential, response_data)

    def  test_c_login_failed_wrong_pw(self): #test case 1
     # steps
        driver = self.browser #buka web browser
        baseLogin.negative_login_wrong_pw(driver)
    
    # validasi
        response_data = driver.find_element(By.CSS_SELECTOR,elem.invCreden).text
        self.assertIn(inputan.invalidCredential, response_data)

    def test_d_login_failed_blank_usn(self):
        # steps
        driver = self.browser #buka web browser
        baseLogin.negative_login_blank_usn(driver)
        
        # validasi
        response_data = driver.find_element(By.CSS_SELECTOR,elem.invCreden).text
        self.assertIn(inputan.requiredUsn, response_data)

    def test_e_login_failed_blank_pw(self):
        # steps
        driver = self.browser #buka web browser
        baseLogin.negative_login_blank_pw(driver)

        # validasi
        response_data = driver.find_element(By.CSS_SELECTOR,elem.invCreden).text
        self.assertIn(inputan.requiredPw, response_data)

    def test_f_login_failed_blank_all(self):
        # steps
        driver = self.browser #buka web browser
        baseLogin.negative_login_blank_all(driver)

        # validasi
        response_data = driver.find_element(By.CSS_SELECTOR,elem.invCreden).text
        self.assertIn(inputan.requiredUsn, response_data)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()