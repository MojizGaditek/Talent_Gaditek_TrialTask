# ScriptName : Login.py
from selenium import webdriver

url = "https://talent.gaditek.com/"
Email = "smojizmehdi@gmail.com"
password = "mojizmehdi1"

xpaths = {'EmailTxtBox': "//*[@id='username']",
          'passwordTxtBox': "//*[@id='candidate_password']",
          'submitButton':   "/html/body/section/div/div/div/form/div[3]/i/input"}

mydriver = webdriver.Firefox()
mydriver.get(url)
# mydriver.maximize_window()

# Clear Username TextBox if already allowed "Remember Me"
mydriver.find_element_by_xpath(xpaths['EmailTxtBox']).clear()

# Write Username in Username TextBox
mydriver.find_element_by_xpath(xpaths['EmailTxtBox']).send_keys(Email)

# Clear Password TextBox if already allowed "Remember Me"
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).clear()

# Write Password in password TextBox
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)

# Click Login button
mydriver.find_element_by_xpath(xpaths['submitButton']).click()

