from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

'''# Chrome options for headless mode and disabling the GPU
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
'''
# Path to your Chrome driver
chrome_driver_path = r"C:\Users\allen\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Initialize Chrome driver with options
driver = webdriver.Chrome(chrome_driver_path, chrome_options)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")
print("Scan the QR code and press Enter")
input()

# Your contact's name and message
contact_name = "+917200511101"
message = "Your automated message goes here!"

# Locating the contact by title (you may need to adjust the selector)
try:
    contact = driver.find_element_by_xpath(f'//span[@title="{contact_name}"]')
    contact.click()
    time.sleep(2)  # Allow some time for the chat to load

    # Typing and sending the message
    input_box = driver.find_element_by_xpath('//div[@contenteditable="true"]')
    input_box.send_keys(message)
    time.sleep(1)
    input_box.send_keys('\ue007')  # Press Enter key

    print(f"Message sent to {contact_name}!")

except Exception as e:
    print(f"Failed to send a message: {str(e)}")

# Close the browser
driver.quit()
