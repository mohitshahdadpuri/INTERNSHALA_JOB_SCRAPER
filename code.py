from time import time
from bs4 import BeautifulSoup
import requests
import time
# from selenium import webdriver
# chrome_driver = "chromedriver.exe"
# driver = webdriver.Chrome("chromedriver.exe")


# print(soup.find("span",{"class":"b-catalogList__itmBrand fsm txtDark uc js-catalogProductTitle"}).get_text().strip())
# print(soup.find("span", {'class': 'b-catalogList__itmPrice old'}).get_text().strip())
# print(soup.find("em",{"class":"b-catalogList__itmTitle fss"}).get_text().strip())
def find_internships():
    internshala_html= requests.get('https://internshala.com/internships/').text
    soup = BeautifulSoup(internshala_html,'lxml')
    jobs = soup.find_all('div', class_='container-fluid individual_internship visibilityTrackerItem')
    # print(jobs)
    # tag1=soup.find_all('div',class_='status-container')
    for index, job in enumerate(jobs):
        
        try:
            published_time=job.find('div', class_='status status-small status-success').text
            if 'Just' in published_time or '1' in published_time or '2' in published_time:
                company_name= job.find('a',class_="link_display_like_text view_detail_button").text.replace(' ','')
                status= job.find('div','status status-small status-inactive').text.replace(' ','')
                # print(company_name)
                # print(status)
                more_info=job.div.div.div.div.a['href']
                with open(f'Jobs/{index}.txt','w') as f:
                    f.write(f'Company Name:{company_name.strip()}  \n')
                    f.write(f'Status:{status.strip()} \n')
                    f.write(f'Published time:{published_time} \n') 
                    f.write(f'More info:{more_info}')   
                    # print('')
                print(f'Saved: {index}')
        except:
            continue
    # try:
    #     published_time=job.find('div', class_='status status-small status-success').text
    #     # published_time=job.find("i",class_="ic-16-reschedule").next_sibling
    #     # published_time=soup.select_one('.ic-i6-reschedule').next_sibling
    #     # https://stackoverflow.com/questions/56721617/how-do-i-extract-text-after-i-class-tag
    #     print("published time: "+published_time)
    # except:
    #     print("published time:NA")

if __name__=='__main__':
    while True:
        find_internships()
        time_wait= 10
        print(f'Waiting {time_wait} minutes')
        time.sleep(time_wait * 60)
