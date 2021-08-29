import time
from logging import error
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# UnSAFE Bank Credentials
username = "BNK04391"
password = "Rubal@123"

#username = "BNK38278"
#password = "Rubal@1234"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# initialize the Chrome driver
driver = webdriver.Chrome("chromedriver",chrome_options=chrome_options)

# head to UnSAFE Bank login page
driver.get("http://165.22.209.118:3000")

# check the status of the login page
response = driver.find_element_by_css_selector("h1.display-3.text-lg-left.text-center.mb-3.font-weight-bold").text
if response == "Login to your account":
    print("[+] Login page is opening successfully")
else:
    print("[!] Login page failed to open")

# find username field and send the username itself to the input field
driver.find_element_by_id("username").send_keys(username)

# find password input field and insert password as well
driver.find_element_by_id("password").send_keys(password)

# click login button
driver.find_element_by_xpath('//button[normalize-space()="Login"]').click()

# wait for the ready state to be complete
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
time.sleep(10)

# check if user is able to login successfully
response = driver.find_element_by_class_name("app-page-title--description").text
print (response)
if response == "This is your Dashboard":
    print("[+] User logged in successfully")
else:
    print("[!] Login failed")

# close the driver
driver.close()
