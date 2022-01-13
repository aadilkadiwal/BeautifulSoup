import requests
from bs4 import BeautifulSoup

# Job in Mumbai Location
URL = "https://in.indeed.com/jobs?q=&l=Mumbai"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# Grabbing the data which we want (Designation, Company_name, Company_location)
results = soup.find(id="mosaic-zone-jobcards")
job_elements = soup.find_all("td", class_="resultContent")

# This list is used to make a csv file
designation = list()
company_name = list()
company_location = list()

for job_element in job_elements:
    title_elements = job_element.find("h2", class_="jobTitle jobTitle-color-purple jobTitle-newJob")
    company_elements = job_element.find("span", class_="companyName")
    location_elements = job_element.find("div", class_="companyLocation")
    if title_elements is None:
        continue
    else:    
        # Get a designation
        title_element = title_elements.text.strip()
        # Get a company_name
        company_element = company_elements.text.strip()
        # Get a company_location
        location_element = location_elements.text.strip()
        # Adding designation in a list
        designation.append(title_element)
        # Adding company_name in a list
        company_name.append(company_element)
        # Adding company_location in a list
        company_location.append(location_element)

'''
Whatever data get it from a website, I convert into csv file format with the help of pandas library 
'''        

import pandas as pd

# dictionaries of list
dict = {"designation": designation, "company_name": company_name, "company_location": company_location}

df = pd.DataFrame(dict)

# saving the dataframe in indeed.csv file
df.to_csv('indeed.csv')