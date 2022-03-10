# Simple Websraping tool, that looks at the boxgrid on politi.dk and gives me the titles of each box and the href link
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://politi.dk/kontakt-politiet")

# Get all the links for the boxes
list1 = []
links = driver.find_elements(By.XPATH, '//*[@id="main-body-content"]/div/div/div/div/a')
for link in links:
    href = link.get_attribute('href')
    #print(href)
    list1.append(href);

# Get all the box titles
list2 = []
titles = driver.find_elements(By.XPATH, '//*[@id="main-body-content"]/div/div/div/div/a/h4')
for title in titles:
    #print(title.text)
    list2.append(title.text)

# Print all the data
# for i in range(len(list2)):
#     print(list2[i] + ": " + list1[i])

print(driver.title)
    
driver.close()