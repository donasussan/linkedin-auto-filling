import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/dona/Documents/chromedriver"
phno =""
chrome_options = Options()
chrome_options.location = chrome_driver_path
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3658011229&f_AL=true&f_E=2&f_TPR=r604800&f_WT=1&geoId=106215326&keywords=communications%20specialist&location=Bangladesh&refresh=true")
username = ''
password = ''

signup_btn = driver.find_element(By.LINK_TEXT, 'Sign in')
signup_btn.click()

email_id = driver.find_element(By.ID, 'username')
email_id.click()
email_id.send_keys(username)

pwd = driver.find_element(By.ID,'password')
pwd.send_keys(password)
pwd.send_keys(Keys.ENTER)
time.sleep(20)

click_easy_apply = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card button").click()

#phone = driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3656363954-9-phoneNumber-nationalNumber"]')
#hone.send_keys(phno)
#phone.send_keys(Keys.ENTER)

# Click the button
submit = driver.find_element(By.CSS_SELECTOR, '.justify-flex-end button')
submit.click()

time.sleep(200)
# Perform further actions on the element


driver.quit()
