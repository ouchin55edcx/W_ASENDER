import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# Set the path to the Chrome WebDriver executable
chrome_driver_path = r'"C:\Users\youco\Desktop\chromedriver-win64\chromedriver.exe"'

# Initialize WebDriver using the Service module
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Take input from the user for the country and category
country = input("Enter the country name: ")
category = input("Enter the category (e.g., doctor, restaurant, etc.): ")

# Construct the Google Maps URL based on the user's input
url = f"https://www.google.com/maps/search/{category}+in+{country}"
driver.get(url)

# Wait for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# Scroll down to load more results
scroll_pause_time = 2  # Adjust this as needed
scroll_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)
    new_scroll_height = driver.execute_script("return document.body.scrollHeight")
    if new_scroll_height == scroll_height:
        break
    scroll_height = new_scroll_height

# Get the page source
page_source = driver.page_source

# Find phone numbers using regular expression
phone_numbers = re.findall(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b', page_source)

# Close the WebDriver
driver.quit()

# Print the extracted phone numbers
if phone_numbers:
    print("Extracted Phone Numbers:")
    for number in phone_numbers:
        print(number)
else:
    print("No phone numbers found.")
