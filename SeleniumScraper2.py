# This bot can check if a wordpress website is using default wordpress login credentials. 
# User has to provide the URL
# I use keys to enter values into the input form on the wordpress wp-admin login site. 
# First we enter in the default username "admin" into the user_login input field
# then we enter the default password "password" into the pass_login input field
# then we send the enter key on the submit button.
# if we receive login error on the site
# Author: Simon Søborg
# For educational purpose only. 

from turtle import color
from attr import define
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class bcolors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'

_DEFAULT_USER = "admin"
_DEFAULT_PASS = "password"

def main():
    url = input("Enter your Wordpress URL: ")
    url = "http://" + url + "/wp-admin/"
    if(url != None):
        run(url)

def run(url):
    print(bcolors.YELLOW + url + "\n" + bcolors.ENDC)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    loginInput = driver.find_element(By.XPATH, '//*[@id="user_login"]')
    loginInput.send_keys(_DEFAULT_USER)
    passInput = driver.find_element(By.XPATH, '//*[@id="user_pass"]')
    passInput.send_keys(_DEFAULT_PASS)
    submitBtn = driver.find_element(By.XPATH, '//*[@id="wp-submit"]')
    submitBtn.send_keys(Keys.ENTER)
    
    if(driver.find_element(By.XPATH, '//*[@id="login_error"]') != None):
        print(bcolors.GREEN + "Site is secure" + bcolors.ENDC)
        driver.quit()
    else:
        print(bcolors.RED + "Site is vulnerable" + bcolors.ENDC)
        driver.quit()

if __name__ == "__main__":
    main()