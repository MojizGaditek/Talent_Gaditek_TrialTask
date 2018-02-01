# ScriptName : SignUp.py
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

url = "https://talent.gaditek.com/"
FirstName = "Mojiz"
LastName = "Mehdi"
Email = "mojiz.gaditek@gmail.com"
password = "mojizmehdi1"
Confirmpassword = "mojizmehdi1"

elem = {'FirstNameTxtBox': "first_name",
          'LastNameTxtBox' : "last_name",
          'EmailTxtBox': "email",
          'passwordTxtBox': "password",
          'PasswordConfirmationTxtBox' : "password_confirmation",
          'NewApplicant' : "/html/body/section/div/div/div/form/div[3]/a",
        'SignupButton' : "/html/body/section/div/div/form/div[6]/i/input"}

mydriver = webdriver.Firefox()
mydriver.get(url)

# Click New Applicant button twice because it is an error in website using firefox that sign up button has to click twice
mydriver.find_element_by_xpath(elem['NewApplicant']).click()
mydriver.find_element_by_xpath(elem['NewApplicant']).click()



# I tried below try and except method to click twice on New Applicant button, It worked fine but gave some exception error thats why i commented it out
#link = None
#while not link:
#    try:
#        link = mydriver.find_element_by_xpath('/html/body/section/div/div/div/form/div[3]/a').click()
#    except NoSuchElementException:
#        link = mydriver.find_element_by_xpath('/html/body/section/div/div/div/form/div[3]/a').click()

# Write Username in Username TextBox
mydriver.find_element_by_id(elem['FirstNameTxtBox']).send_keys(FirstName)

# Write Username in Username TextBox
mydriver.find_element_by_id(elem['LastNameTxtBox']).send_keys(LastName)

# Write Username in Username TextBox
mydriver.find_element_by_id(elem['EmailTxtBox']).send_keys(Email)

# Write Password in password TextBox
mydriver.find_element_by_id(elem['passwordTxtBox']).send_keys(password)

# Write Confrim Password in Confirm password TextBox
mydriver.find_element_by_id(elem['PasswordConfirmationTxtBox']).send_keys(Confirmpassword)

#Click New Applicant button
mydriver.find_element_by_xpath(elem['SignupButton']).click()




