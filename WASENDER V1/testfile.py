import time
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

class WhatsAppSender:
    def __init__(self, driver, numbers, message):
        self.driver = driver
        self.numbers = numbers
        self.message = message

    def send_messages(self):
        for number in self.numbers:
            try:
                if not self.is_valid_whatsapp_number(number):
                    print(f"Invalid WhatsApp number: {number}")
                    continue

                chat_url = f"https://web.whatsapp.com/send?phone={number}&text={self.message}"
                self.driver.get(chat_url)
                time.sleep(1)

                inp_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
                input_box = WebDriverWait(self.driver, 40).until(
                    expected_conditions.presence_of_element_located((By.XPATH, inp_xpath))
                )
                input_box.send_keys(Keys.ENTER)

                print(f"Message sent to {number}")
                time.sleep(1)  # Adjust this delay between each message
            except Exception as e:
                print(f"Error sending message to {number}: {e}")
                pass

    def is_valid_whatsapp_number(self, number):
        # You can implement your own logic to check if the number is valid for WhatsApp
        # For example, you can check if the number starts with a certain prefix
        # or if it's a valid phone number format
        return True

def main():
    chrome_options = Options()
    chrome_options.add_argument("start-maximized")
    user_data_dir = ''.join(random.choices(string.ascii_letters, k=8))
    chrome_options.add_argument("--user-data-dir=/tmp/chrome-data/" + user_data_dir)
    chrome_options.add_argument("--incognito")

    chrome_driver_path = r'C:\Users\HP\Desktop\chromedriver-win64\chromedriver.exe'
    browser = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

    message = "Your message goes here"  # Replace with your message

    country_code = "+33"  # Replace with your desired country code

    phone_numbers = [
     
    "+212 617-187392",
    "+212 706-409921",
    "+212 704-948191",
    "+212 691-072494",
    "+212 696-862779",
    "+212 697-485748",
    "+212 636-359598"
]

    whatsapp_sender = WhatsAppSender(browser, phone_numbers, message)
    whatsapp_sender.send_messages()

    browser.quit()

if __name__ == "__main__":
    main()
