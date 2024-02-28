from selenium import webdriver
import time

def check_whatsapp_registration(phone_number, driver):
    driver.get("https://web.whatsapp.com/")
    input("Press Enter after scanning the QR code and logging in…")

    # Navigate to the WhatsApp Web search page
    driver.get(f"https://web.whatsapp.com/send?phone={phone_number}")
    time.sleep(10)  # wait for the page to load

    # Check if the phone number is registered on WhatsApp
    message_button_xpath = "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]"
    if driver.find_elements_by_xpath(message_button_xpath):
        print(f"{phone_number} - Registered on WhatsApp")
    else:
        print(f"{phone_number} - Not registered on WhatsApp")

if __name__ == "__main__":
    chrome_driver_path = r'C:\Users\HP\Desktop\chromedriver-win64\chromedriver.exe'
    
    # Specify Chrome options to avoid SSL and session creation issues
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")  # Only use this option if needed
    chrome_options.add_argument("--ignore-certificate-errors")  # Ignore SSL errors
    
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    
    try:
        phone_numbers_input = input("Enter the phone numbers separated by commas: ")
        phone_numbers = phone_numbers_input.split(',')
        
        for phone_number in phone_numbers:
            phone_number = phone_number.strip()  # Remove leading/trailing whitespace
            check_whatsapp_registration(phone_number, driver)
    finally:
        driver.quit()

