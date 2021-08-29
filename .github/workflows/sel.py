from logging import error
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# Github credentials
username = "tomsmith"
password = "SuperSecretPassword!"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
# initialize the Chrome driver
driver = webdriver.Chrome("chromedriver",chrome_options=chrome_options)
# head to github login page
driver.get("http://the-internet.herokuapp.com/login")
#driver.get("https://68.183.85.157:3000")
# find username/email field and send the username itself to the input field
driver.find_element_by_id("username").send_keys(username)
# find password input field and insert password as well
driver.find_element_by_id("password").send_keys(password)
# click login button
driver.find_element_by_xpath('//button[normalize-space()="Login"]').click()
#driver.find_element_by_name("button").click()
# wait the ready state to be complete
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error_message = "Your password is invalid!"
# get the errors (if there are)
errors = driver.find_elements_by_id("flash")
# print the errors optionally
for e in errors:
     print(e.text)
# if we find that error message within errors, then login is failed
if any(error_message in e.text for e in errors):
    print("[!] Login failed")
else:
    print("[+] Login successful")

# close the driver
driver.close()
