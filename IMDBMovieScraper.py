# Getting information from IMDBs list of top 250 movies. 
# I want to save the data in either .txt file or convert to csv file. 
# Author: Simon Søborg
# For educational purposes

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv

def main():
    
    titles = []
    ratings = []
    releasedates = []
    
    titles, ratings, releasedates = collect(titles, ratings, releasedates)
    saveData(titles, ratings, releasedates)
        
def collect(titles, ratings, releasedates):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
    
    findTitles = driver.find_elements(By.XPATH, '//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr/td[2]/a')
    for title in findTitles:
        titles.append(title.text)
    
    findRatings = driver.find_elements(By.XPATH, '//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr/td[3]/strong')
    for rating in findRatings:
        ratings.append(rating.text)
    
    findDates = driver.find_elements(By.XPATH, '//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr/td[2]/span')
    for releasedate in findDates:
        releasedates.append(releasedate.text)
        
    return titles, ratings, releasedates

def saveData(titles, ratings, releasedates):
    header = ['Title', 'Rating', 'ReleaseYear']
    with open('IMDBTop250.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i in range(len(titles)):
            data = [titles[i], ratings[i], releasedates[i]]
            writer.writerow(data)
            

if __name__ == "__main__":
    main()