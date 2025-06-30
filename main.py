import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

GROUP_NAME = "Team QMS"
MESSAGE = "Reminder to upload today's Khatm-e-kamali content on YouTube."

options = uc.ChromeOptions()
options.headless = True
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--user-data-dir=./user_data")  # persistent session folder

driver = uc.Chrome(options=options)

driver.get("https://web.whatsapp.com")

print("Waiting for WhatsApp Web to load (you must login once)...")

# Wait long enough for QR scan & login, or check login status
time.sleep(30)  # Increase if needed

# Search and open group
search_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@data-tab='3']")
search_box.click()
time.sleep(1)
search_box.send_keys(GROUP_NAME)
time.sleep(2)
search_box.send_keys(Keys.ENTER)

# Send message
msg_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@data-tab='10']")
msg_box.click()
time.sleep(1)
msg_box.send_keys(MESSAGE)
msg_box.send_keys(Keys.ENTER)

print("✅ Message sent!")

time.sleep(5)
driver.quit()
