from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service = Service(ChromeDriverManager().install())
opts = webdriver.ChromeOptions()
opts.add_argument("--window-size=800,600")
driver = webdriver.Chrome(service=service, options=opts)

driver.get("https://www.zeiss.de/")

# Wait for popup to appear and click "All akzeptieren" button
popup_locator = (By.ID, "onetrust-banner-sdk")
popup = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(popup_locator))
all_accept_locator = (By.ID, "onetrust-accept-btn-handler")
all_accept_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(all_accept_locator))
all_accept_button.click()

# Scroll to the bottom of the page and click "Karriere"
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
karriere_locator = (By.XPATH, "//a[@title='Karriere']")
karriere_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(karriere_locator))
karriere_link.click()

time.sleep(7)
driver.quit()
