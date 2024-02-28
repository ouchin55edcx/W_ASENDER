from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

def send_whatsapp_message(phone_number, message, driver):
    chat_url = f"https://web.whatsapp.com/send?phone={phone_number}"
    driver.get(chat_url)
    
    time.sleep(5)  # Initial wait
    
    max_resolve_time = 60  # Maximum time to resolve the chat in seconds
    start_time = time.time()
    
    while time.time() - start_time < max_resolve_time:
        try:
            # Check for the unconfirmed number message
            unconfirmed_button = driver.find_element(By.XPATH, "//div[@class='_2Bw3Q']")
            unconfirmed_button.click()
            return False  # Move to the next number
        except NoSuchElementException:
            try:
                # Check if the message input box is available
                message_input = driver.find_element(By.XPATH, "//div[@contenteditable='true']")
                message_input.click()
                message_input.send_keys(message)

                send_button = driver.find_element(By.XPATH, "//span[@data-icon='send']")
                send_button.click()

                time.sleep(1)  
                return True
            except NoSuchElementException:
                time.sleep(1)  
                continue
    
    return False 

if __name__ == "__main__":
    firefox_options = Options()
    # firefox_options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'  # Replace with your Firefox binary path
    driver = webdriver.Firefox(options=firefox_options)
    
    try:
        phone_numbers_input = input("Enter the phone numbers separated by commas: ")
        phone_numbers = phone_numbers_input.split(',')
        
        driver.get("https://web.whatsapp.com/")
        input("Press Enter after scanning the QR code and logging in…")
        
        message_to_send = input("Enter the message you want to send: ")
        
        sent_count = 0
        
        for phone_number in phone_numbers:
            phone_number = phone_number.strip()
            
            if send_whatsapp_message(phone_number, message_to_send, driver):
                print(f"Message sent to {phone_number}")
                sent_count += 1
            else:
                print(f"Could not send message to {phone_number}")
                
            time.sleep(1)  # Wait before moving to the next number
        
        print("Message sending complete.")
        print(f"Total messages sent: {sent_count}")
        
    finally:
        driver.quit()
