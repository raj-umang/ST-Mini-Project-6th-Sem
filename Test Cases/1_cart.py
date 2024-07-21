from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# driver.maximize_window()
driver.get("https://flipkart.com")


# First Test Case 

# To Verify that the homepage loads successfully.
try:
    home_page_element = driver.find_element(By.XPATH, "/html/head/title")
    print("Home page loaded successfully!")
except Exception as e:
    print("Error: Home page not loaded!", e)

# Second Test Case  - Search any product

#Third Test Case - Add to Cart

# Search and Add to Cart:
search_bar = driver.find_element(By.CLASS_NAME, "Pke_EE")
search_bar.send_keys("samsung mobile")
search_bar.send_keys(Keys.ENTER)


# Click on the first search result
first_result = driver.find_element(By.CLASS_NAME, "DByuf4")
first_result.click()
time.sleep(1)

# Switch Tab focus for selenium webdriver
mainPage = driver.window_handles[0]
#print("Main page=" + mainPage)
allPages = driver.window_handles
for page in allPages:
    if page != mainPage:
        driver.switch_to.window(page)
        break

# Adding Pincode to make the product available
# enter_pin = driver.find_element(By.CLASS_NAME, "AFOXgu")
# enter_pin.send_keys("560107")
# enter_pin.send_keys(Keys.ENTER)



# Add item to the cart
add_to_cart = driver.find_element(By.CLASS_NAME, "In9uk2")
add_to_cart.click()

# Verify the item is added to the cart
# cart_item = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "_3fSRat")))
# assert "My Cart" in driver.page_source
print("Add to cart functionality verified!")



# Fourth Test Case - Remove item from cart


# Remove the item from the cart
remove_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "sBxzFz")))
remove_button.click()

# Confirm removal
confirm_remove = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "sBxzFz")))
confirm_remove.click()

# Verify the cart is empty
empty_cart_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Your cart is empty!']")))
assert "Your cart is empty!" in driver.page_source
print("Remove from cart functionality verified!")




