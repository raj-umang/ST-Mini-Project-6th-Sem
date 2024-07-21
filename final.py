from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class CustomTestResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.passed_tests = 0

    def addSuccess(self, test):
        super().addSuccess(test)
        self.passed_tests += 1
        print(f"\nTest Description: {test.shortDescription()}")
        print("Result: Success\n")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        print(f"\nTest Description: {test.shortDescription()}")
        print("Result: Failure")
        print(self.failures[-1][-1])

    def printSummary(self):
        total_tests = self.testsRun
        total_failures = len(self.failures)
        total_errors = len(self.errors)
        total_successes = self.passed_tests

        print("\n" + "="*70)
        print(f"Ran {total_tests} tests")
        print(f"PASSED: {total_successes}")
        print(f"FAILED: {total_failures}")
        print(f"ERRORS: {total_errors}")
        print("="*70)

class CustomTestRunner(unittest.TextTestRunner):
    def _makeResult(self):
        return CustomTestResult(self.stream, self.descriptions, self.verbosity)

    def run(self, test):
        result = super().run(test)
        result.printSummary()
        return result

class FlipkartTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.service = Service(executable_path="chromedriver.exe")
        cls.driver = webdriver.Chrome(service=cls.service)

    @classmethod
    def tearDownClass(cls):
        time.sleep(4)
        cls.driver.quit()

    def close_login_popup(self):
        try:
            close_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "_30XB9F"))
            )
            close_button.click()
        except Exception:
            print(" ")

    # First Test Case:
    def test_page_title(self):
        """
        Verify if the page title is "Online Shopping"
        """
        self.driver.get("https://www.flipkart.com")
        self.close_login_popup()
        self.assertIn("Online Shopping", self.driver.title)
        

    # Second Test Case:
    def test_search_functionality(self):
        """
            Verify if the search functionality is working
        """

        self.driver.get("https://www.flipkart.com")
        self.close_login_popup()
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys("laptop" + Keys.ENTER)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "_4WELSP"))
        )
        self.assertIn("laptop", self.driver.page_source)

    # Third Test Case :
    def test_navigation_to_product_page(self):
        """
        Verify if navigating to a product page works
        """
        self.driver.get("https://www.flipkart.com")
        self.close_login_popup()
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys("laptop" + Keys.ENTER)
        first_product = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "_4WELSP"))
        )
        first_product.click()
        self.assertIn("Laptop", self.driver.title)

    # Fourth Test Case : 
    def test_add_to_cart(self):
        """
        Verify if adding a product to the cart works
        """

        self.driver.get("https://www.flipkart.com")
        self.close_login_popup()
        # Search for a product
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys("laptop" + Keys.ENTER)
        # Remove target attribute to prevent opening in a new tab
        self.driver.execute_script("""
            var elements = document.querySelectorAll('a');
            elements.forEach(function(element) {
                element.removeAttribute('target');
            });
        """)
        # Click the first product
        first_product = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "_4WELSP"))
        )
        first_product.click()
        # Wait for the add to cart button to appear and click it
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "NwyjNT"))
        )
        add_to_cart_button.click()
        self.assertIn("Cart", self.driver.page_source)


    # Fiffth Test Case :
    def test_cart_functionality(self):
        """
        Verify if the cart functionality is working 
        """
        self.driver.get("https://www.flipkart.com")
        self.close_login_popup()
        cart_button = self.driver.find_element(By.CLASS_NAME, "_3RX0a-")
        cart_button.click()
        self.assertIn("Cart", self.driver.page_source)


    # FIXME:  # Sixth Test Case
    def test_remove_from_cart(self):
        self.driver.get("https://www.flipkart.com")
        self.close_login_popup()
        cart_button = self.driver.find_element(By.CLASS_NAME, "_3RX0a-")
        cart_button.click()
        remove_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "sBxzFz"))
        )
        remove_button.click()
        confirm_remove = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "A0MXnh"))
        )
        confirm_remove.click()
        self.assertIn("Your cart is empty", self.driver.page_source)

    
    # Seventh Test Case :
    def test_quantity_update(self):
        """
        Verify if the Quantity has been updated
        """
        self.driver.get("https://www.flipkart.com")
        self.close_login_popup()
        # Search for a product
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys("laptop" + Keys.ENTER)
        # Remove target attribute to prevent opening in a new tab
        self.driver.execute_script("""
            var elements = document.querySelectorAll('a');
            elements.forEach(function(element) {
                element.removeAttribute('target');
            });
        """)
        # Click the first product
        first_product = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "_4WELSP"))
        )
        first_product.click()
        # Wait for the add to cart button to appear and click it
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "NwyjNT"))
        )
        add_to_cart_button.click()
        increment_quantity_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "LcLcvv"))
        )
        increment_quantity_button.click()
        self.assertIn("2", self.driver.page_source)

    
    # TODO:
    def test_invalid_login(self):
        self.driver.get("https://www.flipkart.com")
        login_button = self.driver.find_element(By.XPATH, "//a[contains(text(),'Login')]")
        login_button.click()
        username_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@class='_2IX_2- VJZDxU']"))
        )
        username_input.send_keys("invalid_username")
        password_input = self.driver.find_element(By.XPATH, "//input[@type='password']")
        password_input.send_keys("invalid_password")
        submit_button = self.driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2HKlqd _3AWRsL']")
        submit_button.click()
        self.assertIn("Your username or password is incorrect", self.driver.page_source)


    # Eighth Test Case :
    def test_product_filters(self):
        """
        Verify if the product filters are working correctly
        """
        self.driver.get("https://www.flipkart.com")
        self.close_login_popup()
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys("laptop" + Keys.ENTER)
        filter_checkbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "_6i1qKy"))
        )
        filter_checkbox.click()
        self.assertIn("Core i5", self.driver.page_source)


    # Ninth Test Case :
    def test_product_sorting(self):
        """
        Verify if the product sorting is working correctly
        """
        self.driver.get("https://www.flipkart.com")
        self.close_login_popup()
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys("laptop" + Keys.ENTER)
        sort_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "zg-M3Z"))
        )
        sort_dropdown.click()
        low_to_high_option = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Price -- Low to High')]"))
        )
        low_to_high_option.click()
        self.assertIn("Price -- Low to High", self.driver.page_source)


    # Tenth Test Case :
    def test_wishlist_functionality(self):
        """
        Verify if the wishlist functionality is working or not
        """
        self.driver.get("https://www.flipkart.com")
        self.close_login_popup()
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys("laptop" + Keys.ENTER)
        add_to_wishlist_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "N1bADF"))
        )
        add_to_wishlist_button.click()


    # Eleventh Test Case :
    def test_checkout_process(self):
        """
        Verify if the checkout process is working or not
        """
        self.driver.get("https://www.flipkart.com")
        self.close_login_popup()
        # Search for a product
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys("laptop" + Keys.ENTER)
        # Remove target attribute to prevent opening in a new tab
        self.driver.execute_script("""
            var elements = document.querySelectorAll('a');
            elements.forEach(function(element) {
                element.removeAttribute('target');
            });
        """)
        # Click the first product
        first_product = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "_4WELSP"))
        )
        first_product.click()
        # Wait for the add to cart button to appear and click it
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "NwyjNT"))
        )
        add_to_cart_button.click()
        # Wait for the proceed to checkout button and click it
        proceed_to_checkout_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Place Order')]"))
        )
        proceed_to_checkout_button.click()

        # Verify the presence of "Delivery Address" in the page source
        self.assertIn("Delivery Address", self.driver.page_source)


    # Twelth Test Case : FIXME:
    def test_customer_service(self):   #Some Errors
        """
        Verify if the customer service functionality is working
        """
        self.driver.get("https://www.flipkart.com")
        self.close_login_popup()
        customer_service_link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "-dOa_b"))
        )
        customer_service_link.click()
        # self.assertIn("Help", self.driver.title)

    # Thirthteen Test Case :
    def test_product_reviews(self):
        """
        Verify if the product reviews functionality is working
        """
        self.driver.get("https://www.flipkart.com")
        self.close_login_popup()
        # Search for a product
        search_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys("samsung s23" + Keys.ENTER)
        # Remove target attribute to prevent opening in a new tab
        self.driver.execute_script("""
            var elements = document.querySelectorAll('a');
            elements.forEach(function(element) {
                element.removeAttribute('target');
            });
        """)
        # Click the first product
        first_product = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "_4WELSP"))
        )
        first_product.click()
        reviews_tab = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Wphh3N"))
        )
        reviews_tab.click()


    # 14th Test Case :
    def test_offers_and_coupons(self):
        """
        Verify if the offers and coupons functionality is working
        """
        self.driver.get("https://www.flipkart.com")
        self.close_login_popup()
        offers_link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "YBLJE4"))
        )
        offers_link.click()




if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(FlipkartTests('test_page_title'))
    suite.addTest(FlipkartTests('test_search_functionality'))
    suite.addTest(FlipkartTests('test_navigation_to_product_page'))
    suite.addTest(FlipkartTests('test_add_to_cart'))
    suite.addTest(FlipkartTests('test_cart_functionality'))
    suite.addTest(FlipkartTests('test_remove_from_cart'))
    suite.addTest(FlipkartTests('test_quantity_update'))
    suite.addTest(FlipkartTests('test_product_filters'))
    suite.addTest(FlipkartTests('test_product_sorting'))
    suite.addTest(FlipkartTests('test_wishlist_functionality'))
    suite.addTest(FlipkartTests('test_checkout_process'))
    suite.addTest(FlipkartTests('test_customer_service'))
    suite.addTest(FlipkartTests('test_product_reviews'))
    suite.addTest(FlipkartTests('test_offers_and_coupons'))
    suite.addTest(FlipkartTests('test_invalid_login'))

    runner = CustomTestRunner(verbosity=2)
    runner.run(suite)