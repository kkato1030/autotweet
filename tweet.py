from selenium import webdriver
import time
import json

# ブラウザを開く
driver = webdriver.Chrome()
# どこのURL開くよ
driver.get('https://twitter.com')
time.sleep(2)

with open('./login.json') as f:
    login = json.load(f)

# login
login_btn = driver.find_element_by_xpath('//a[@href="/login"]')
login_btn.click()
time.sleep(1)
username = driver.find_element_by_xpath('//input[@name="session[username_or_email]"]')
username.send_keys(login['username'])
username = driver.find_element_by_xpath('//input[@name="session[password]"]')
username.send_keys(login['password'])
form = driver.find_element_by_xpath('//form[@action="/sessions"]')
form.submit()
time.sleep(1)

# tweet
element_text = driver.find_element_by_class_name("notranslate")
element_text.click()
element_text.send_keys("Hello Twitter from selenium *for Practive.")
tweet_button = driver.find_element_by_xpath('//*[@data-testid="tweetButtonInline"]')
tweet_button.click()

# driver.close()
