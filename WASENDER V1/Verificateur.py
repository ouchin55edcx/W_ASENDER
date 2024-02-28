
# this code write by : MOUSLIM ABDELFATTAH.

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def check_whatsapp_registration(phone_number, driver):
    # Navigate to the WhatsApp Web search page
    driver.get(f"https://web.whatsapp.com/send?phone={phone_number}")
    
    message_button_xpath = "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]"
    invalid_number_xpath = "//*[@id='app']/div/span[2]/div/span/div/div/div/div/div/div[2]/div/button"
    
    # Set maximum wait time in seconds
    max_wait_time = 60
    current_wait_time = 0
    
    while current_wait_time < max_wait_time:
        if driver.find_elements(By.XPATH, message_button_xpath):
            return True  # Registered
        elif driver.find_elements(By.XPATH, invalid_number_xpath):
            return False  # Invalid number
        time.sleep(1)
        current_wait_time += 1
    
    return None  # Unable to determine

if __name__ == "__main__":
    chrome_driver_path = r'C:\Users\fettah-cach\Desktop\chromedriver-win64\chromedriver.exe'
    chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'  # Path to Chrome executable
    
    # Create a service object with the ChromeDriver executable path
    service = Service(chrome_driver_path)
    
    chrome_options = Options()
    chrome_options.binary_location = chrome_path
    
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        phone_numbers_input = input("Enter the phone numbers separated by commas: ")
        phone_numbers = phone_numbers_input.split(',')
        
        driver.get("https://web.whatsapp.com/")
        input("Press Enter after scanning the QR code and logging in…")
        
        registered_count = 0
        not_registered_count = 0
        
        for phone_number in phone_numbers:
            phone_number = phone_number.strip()  # Remove leading/trailing whitespace
            
            is_registered = check_whatsapp_registration(phone_number, driver)
            
            if is_registered is None:
                print(f"{phone_number} - Unable to determine")
            elif is_registered:
                print(f"{phone_number} - Registered on WhatsApp")
                registered_count += 1
            else:
                print(f"{phone_number} - Not registered on WhatsApp")
                not_registered_count += 1
            
    finally:
        driver.quit()
        
    print("Statistics:")
    print(f"Registered numbers: {registered_count}")
    print(f"Not registered numbers: {not_registered_count}")
