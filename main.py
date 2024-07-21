from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class FlipkartTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.service = Service(executable_path="chromedriver.exe")
        cls.driver = webdriver.Chrome(service=cls.service)

    def close_login_popup(self):
        try:
            close_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'✕')]"))
            )
            close_button.click()
        except Exception as e:
            print("Login popup did not appear or could not be closed: ", e)

    def test_page_title(self):
        self.driver.get("https://www.flipkart.com")
        self.close_login_popup()
        self.assertIn("Flipkart", self.driver.title)

    # def test_search_functionality(self):
    #     self.driver.get("https://www.flipkart.com")
    #     self.close_login_popup()
    #     search_box = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.NAME, "q"))
    #     )
    #     search_box.send_keys("laptop" + Keys.ENTER)
    #     WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "_4rR01T"))
    #     )
    #     self.assertIn("laptop", self.driver.page_source)

    # def test_login_popup(self):
    #     self.driver.get("https://www.flipkart.com")
    #     try:
    #         close_button = WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'✕')]"))
    #         )
    #         close_button.click()
    #         self.assertTrue(True)
    #     except Exception as e:
    #         self.fail(f"Login popup did not appear or could not be closed: {e}")

    # def test_navigation_to_product_page(self):
    #     self.driver.get("https://www.flipkart.com")
    #     self.close_login_popup()
    #     search_box = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.NAME, "q"))
    #     )
    #     search_box.send_keys("laptop" + Keys.ENTER)
    #     first_product = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "_4rR01T"))
    #     )
    #     first_product.click()
    #     self.assertIn("Laptop", self.driver.title)

    # def test_add_to_cart(self):
    #     self.driver.get("https://www.flipkart.com")
    #     self.close_login_popup()
    #     search_box = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.NAME, "q"))
    #     )
    #     search_box.send_keys("laptop" + Keys.ENTER)
    #     first_product = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "_4rR01T"))
    #     )
    #     first_product.click()
    #     add_to_cart_button = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'ADD TO CART')]"))
    #     )
    #     add_to_cart_button.click()
    #     self.assertIn("Cart", self.driver.page_source)

    # def test_cart_functionality(self):
    #     self.driver.get("https://www.flipkart.com")
    #     self.close_login_popup()
    #     cart_button = self.driver.find_element(By.XPATH, "//span[contains(text(),'Cart')]")
    #     cart_button.click()
    #     self.assertIn("Cart", self.driver.page_source)

    # def test_remove_from_cart(self):
    #     self.driver.get("https://www.flipkart.com")
    #     self.close_login_popup()
    #     cart_button = self.driver.find_element(By.XPATH, "//span[contains(text(),'Cart')]")
    #     cart_button.click()
    #     remove_button = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Remove')]"))
    #     )
    #     remove_button.click()
    #     confirm_remove = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Remove')]"))
    #     )
    #     confirm_remove.click()
    #     self.assertIn("Your cart is empty", self.driver.page_source)

    # def test_quantity_update(self):
    #     self.driver.get("https://www.flipkart.com")
    #     self.close_login_popup()
    #     search_box = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.NAME, "q"))
    #     )
    #     search_box.send_keys("laptop" + Keys.ENTER)
    #     first_product = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "_4rR01T"))
    #     )
    #     first_product.click()
    #     add_to_cart_button = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'ADD TO CART')]"))
    #     )
    #     add_to_cart_button.click()
    #     increment_quantity_button = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//button[contains(@class, '_23FHuj')]"))
    #     )
    #     increment_quantity_button.click()
    #     self.assertIn("2", self.driver.page_source)

    # def test_login_functionality(self):
    #     self.driver.get("https://www.flipkart.com")
    #     login_button = self.driver.find_element(By.XPATH, "//a[contains(text(),'Login')]")
    #     login_button.click()
    #     username_input = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//input[@class='_2IX_2- VJZDxU']"))
    #     )
    #     username_input.send_keys("your_username")
    #     password_input = self.driver.find_element(By.XPATH, "//input[@type='password']")
    #     password_input.send_keys("your_password")
    #     submit_button = self.driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2HKlqd _3AWRsL']")
    #     submit_button.click()
    #     self.assertIn("My Account", self.driver.page_source)

    # def test_invalid_login(self):
    #     self.driver.get("https://www.flipkart.com")
    #     login_button = self.driver.find_element(By.XPATH, "//a[contains(text(),'Login')]")
    #     login_button.click()
    #     username_input = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//input[@class='_2IX_2- VJZDxU']"))
    #     )
    #     username_input.send_keys("invalid_username")
    #     password_input = self.driver.find_element(By.XPATH, "//input[@type='password']")
    #     password_input.send_keys("invalid_password")
    #     submit_button = self.driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2HKlqd _3AWRsL']")
    #     submit_button.click()
    #     self.assertIn("Your username or password is incorrect", self.driver.page_source)

    # def test_product_filters(self):
    #     self.driver.get("https://www.flipkart.com")
    #     self.close_login_popup()
    #     search_box = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.NAME, "q"))
    #     )
    #     search_box.send_keys("laptop" + Keys.ENTER)
    #     filter_checkbox = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'HP')]//preceding-sibling::div//input"))
    #     )
    #     filter_checkbox.click()
    #     self.assertIn("HP", self.driver.page_source)

    # def test_product_sorting(self):
    #     self.driver.get("https://www.flipkart.com")
    #     self.close_login_popup()
    #     search_box = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.NAME, "q"))
    #     )
    #     search_box.send_keys("laptop" + Keys.ENTER)
    #     sort_dropdown = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//div[@class='_1YAKP4']"))
    #     )
    #     sort_dropdown.click()
    #     low_to_high_option = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Price -- Low to High')]"))
    #     )
    #     low_to_high_option.click()
    #     self.assertIn("Price -- Low to High", self.driver.page_source)

    # def test_wishlist_functionality(self):
    #     self.driver.get("https://www.flipkart.com")
    #     self.close_login_popup()
    #     search_box = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.NAME, "q"))
    #     )
    #     search_box.send_keys("laptop" + Keys.ENTER)
    #     first_product = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "_4rR01T"))
    #     )
    #     first_product.click()
    #     add_to_wishlist_button = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Add to Wishlist')]"))
    #     )
    #     add_to_wishlist_button.click()
    #     self.assertIn("Wishlist", self.driver.page_source)

    # def test_checkout_process(self):
    #     self.driver.get("https://www.flipkart.com")
    #     self.close_login_popup()
    #     search_box = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.NAME, "q"))
    #     )
    #     search_box.send_keys("laptop" + Keys.ENTER)
    #     first_product = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "_4rR01T"))
    #     )
    #     first_product.click()
    #     add_to_cart_button = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'ADD TO CART')]"))
    #     )
    #     add_to_cart_button.click()
    #     proceed_to_checkout_button = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Place Order')]"))
    #     )
    #     proceed_to_checkout_button.click()
    #     self.assertIn("Delivery Address", self.driver.page_source)

    # def test_customer_service(self):
    #     self.driver.get("https://www.flipkart.com")
    #     self.close_login_popup()
    #     customer_service_link = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Contact Us')]"))
    #     )
    #     customer_service_link.click()
    #     self.assertIn("Contact Us", self.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
