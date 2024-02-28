from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Firefox driver
firefox_options = FirefoxOptions()
firefox_options.headless = False  # Set to True for a headless browser
driver = webdriver.Firefox(options=firefox_options)

def send_whatsapp_message(phone_number, message, driver):
    chat_url = f"https://web.whatsapp.com/send?phone={phone_number}"
    driver.get(chat_url)
    
    try:
        # Wait for the chat window to load
        chat_window = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div._1G3Wr'))
        )
        
        # Check for the unconfirmed number message
        unconfirmed_button = chat_window.find_element(By.XPATH, "//div[@title='Send message']/button")
        unconfirmed_button.click()
        return False  # Move to the next number
    except NoSuchElementException:
        try:
            # Check if the message input box is available
            message_input = driver.find_element(By.CSS_SELECTOR, 'div._3uMse>div._1awRl>div._1awRl>div.copyable-text')
            message_input.click()
            message_input.send_keys(message)

            send_button = driver.find_element(By.CSS_SELECTOR, 'button._4sWnG>span[data-icon="send"]')
            send_button.click()

            time.sleep(1)  # Wait for the message to be sent

            return True
        except NoSuchElementException:
            time.sleep(1)  # Wait for the message input box to be available
    
    return False  # Move to the next number due to timeout

if __name__ == "__main__":
    phone_numbers = ["+212636359603", "+212708252614"]  # Replace with your numbers
    message_to_send = "Hello, this is an automated message from Python!"
    
    try:
        driver.get("https://web.whatsapp.com/")
        input("Press Enter after scanning the QR code and logging in…")
        
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
