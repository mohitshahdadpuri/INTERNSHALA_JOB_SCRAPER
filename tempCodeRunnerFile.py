from bs4 import BeautifulSoup
import requests
# from selenium import webdriver
# chrome_driver = "chromedriver.exe"
# driver = webdriver.Chrome("chromedriver.exe")


# print(soup.find("span",{"class":"b-catalogList__itmBrand fsm txtDark uc js-catalogProductTitle"}).get_text().strip())
# print(soup.find("span", {'class': 'b-catalogList__itmPrice old'}).get_text().strip())
# print(soup.find("em",{"class":"b-catalogList__itmTitle fss"}).get_text().strip())

internshala_html= requests.get('https://internshala.com/internships/matching-preferences/').text
soup = BeautifulSoup(internshala_html,'lxml')
jobs = soup.find_all('div', class_='container-fluid individual_internship visibilityTrackerItem')
print(jobs)