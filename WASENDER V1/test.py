from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
from random import randint

# Initialize the Firefox driver
driver = webdriver.Firefox()

class WhatsAppSender:
    def __init__(self):
        # Initialize your class attributes here
        self.Numbers = []  # Replace with your list of phone numbers
        self.sleepMin = 1  # Replace with your desired sleep values
        self.sleepMax = 5
        self.text = "Hello, this is an automated message from Python!"  # Replace with your message text

    def send_whatsapp_messages(self):
        logr.debug("Sending messages")

        i = 0
        f = 0
        nf = 0

        for num in self.Numbers:
            log = ""
            try:
                driver.get(f"https://web.whatsapp.com/send?phone={num}")

                # Wait for the QR code to be scanned manually
                input("Press Enter after scanning the QR code...")

                # Wait for the page to load
                time.sleep(5)

                # Locate the input field for the message
                textBox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"]')))
                
                # Clear the input field before sending the message
                textBox.clear()
                
                # Enter the message
                textBox.send_keys(self.text)
                
                # Press Enter to send the message
                textBox.send_keys(Keys.RETURN)
                f += 1
                log = f"Number::{num} => Sent."

                # Add a 5-second delay here
                time.sleep(5)

            except:
                log = f"Error To Number = {num}"
                continue
            finally:
                i += 1
                logr.debug(log)
        
        logr.debug("End sending messages")

if __name__ == "__main__":
    phone_numbers = ["+212636359603", "+212708252614"]  # Replace with your numbers
    logr = logging.getLogger('my_logger')  # Create or configure your logger as needed
    logr.setLevel(logging.DEBUG)
    
    try:
        sender = WhatsAppSender()
        sender.Numbers = phone_numbers
        sender.send_whatsapp_messages()
        
        print("Message sending complete.")
        
    finally:
        driver.quit()
