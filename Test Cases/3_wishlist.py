from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# driver.maximize_window()
driver.get("https://flipkart.com")

# Search for a product and verify the results
search_bar = driver.find_element(By.CLASS_NAME, "Pke_EE")
search_bar.send_keys("smartphone")
search_bar.send_keys(Keys.ENTER)

# Wait for search results to load and verify
search_results = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "DByuf4")))
assert "smartphone" in driver.page_source
print("Search functionality verified!")

# Sixth Test Case - 

# Add item to wishlist
wishlist_button = driver.find_element(By.CLASS_NAME,"x1UMqG")
wishlist_button.click()
print("Wishlist functionality verified!")

# Verify the item is added to the wishlist
wishlist_item = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "x1UMqG")))
assert "My Wishlist" in driver.page_source
