from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class SignIn(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.service = Service('C:/Users/jacke/OneDrive/Desktop/ST Lab/chromedriver.exe')
        cls.driver = webdriver.Chrome(service=cls.service)

    def test_login_valid(self):
        # valid username and password
        self.driver.get('https://www.flipkart.com/')
        self.driver.find_element(By.CLASS_NAME, "_2IX_2-").send_keys("7351650033")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input").send_keys("parasgulati")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button").click()

    def test_login_invalid_password(self):
        # Invalid password
        self.driver.get('https://www.flipkart.com/')
        self.driver.find_element(By.CLASS_NAME, "_2IX_2-").send_keys("7351650033")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input").send_keys("para")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button").click()
        error_msg_actual = 'Your username or password is incorrect'
        self.driver.implicitly_wait(10)
        temp = self.driver.find_element(By.CLASS_NAME, 'ZAtlA-').get_attribute('innerHTML')
        error_msg_got = temp.lstrip("<span>").rstrip("</span>")
        self.assertEqual(error_msg_got, error_msg_actual)

    def test_login_invalid_username(self):
        # Invalid username
        self.driver.get('https://www.flipkart.com/')
        self.driver.find_element(By.CLASS_NAME, "_2IX_2-").send_keys("parasgulati7100@gmail.com")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input").send_keys("parasgulati")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button").click()
        error_msg_actual = 'You are not registered with us. Please sign up.'
        self.driver.implicitly_wait(5)
        error_msg_got = self.driver.find_element(By.CLASS_NAME, 'JAUzCh').get_attribute('innerHTML')
        self.assertEqual(error_msg_got, error_msg_actual)

    def test_login_invalid_username_password(self):
        # Invalid username and password
        self.driver.get('https://www.flipkart.com/')
        self.driver.find_element(By.CLASS_NAME, "_2IX_2-").send_keys("parasgulati7100@gmail.com")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input").send_keys("paral")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button").click()
        error_msg_actual = 'You are not registered with us. Please sign up.'
        self.driver.implicitly_wait(5)
        error_msg_got = self.driver.find_element(By.CLASS_NAME, 'JAUzCh').get_attribute('innerHTML')
        self.assertEqual(error_msg_got, error_msg_actual)

    def test_login_invalid_username_specialSymbol(self):
        # Invalid special symbol in username
        self.driver.get('https://www.flipkart.com/')
        self.driver.find_element(By.CLASS_NAME, "_2IX_2-").send_keys("@#parasgulati&^...")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input").send_keys("parasgulati")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button").click()
        error_msg_actual = 'Please enter valid Email ID/Mobile number'
        self.driver.implicitly_wait(10)
        temp = self.driver.find_element(By.CLASS_NAME, 'ZAtlA-').get_attribute('innerHTML')
        error_msg_got = temp.lstrip("<span>").rstrip("</span>")
        self.assertEqual(error_msg_got, error_msg_actual)

    def test_login_invalid_large_length_username_or_password(self):
        # Large length username or password
        input_str = 'pafrdddhdngirmcspdfgkrkfa'*100
        self.driver.get('https://www.flipkart.com/')
        self.driver.find_element(By.CLASS_NAME, "_2IX_2-").send_keys(input_str)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input").send_keys(input_str)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button").click()
        error_msg_actual = 'Please enter valid Email ID/Mobile number'
        self.driver.implicitly_wait(10)
        temp = self.driver.find_element(By.CLASS_NAME, 'ZAtlA-').get_attribute('innerHTML')
        error_msg_got = temp.lstrip("<span>").rstrip("</span>")
        self.assertEqual(error_msg_got, error_msg_actual)
    
    def test_search_and_view_item(self):
        # valid username and password
        self.driver.get('https://www.flipkart.com/')
        self.driver.find_element(By.CLASS_NAME, "_2IX_2-").send_keys("7351650033")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input").send_keys("parasgulati")
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button").click()

        # Search shoes in search item
        self.driver.find_element(By.CLASS_NAME, 'LM6RPg').send_keys('shoes', Keys.ENTER)
        self.driver.implicitly_wait(10)

        # Select first shoes in the list and view complete product
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[1]/div/a/div[1]/div/div[1]/div').click()
        self.driver.implicitly_wait(20)
        allTabs = self.driver.window_handles
        self.driver.switch_to.window(allTabs[1])
        page = self.driver.find_element(By.TAG_NAME, 'html')
        page.send_keys(Keys.END)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
