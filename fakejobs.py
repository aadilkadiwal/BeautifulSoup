import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

print(results.prettify())   # prettify <-- It will show the content in proper way

job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements:
    # print(job_element, end="\n"*3)

    # Job Designation
    title_element = job_element.find("h2", class_="title is-5")
    # Company Name 
    company_element = job_element.find("h3", class_="subtitle is-6 company")
    # Location
    location_element = job_element.find("p", class_="location")
    print("Designation : ",title_element.text.strip())
    print("Company Name : ",company_element.text.strip())
    print("Location : ",location_element.text.strip())
    print()

# Finding a Python jobs

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_element in python_job_elements:

    # Learn Links
    learn_links = job_element.find_all("a")[0]["href"]
    # Apply Links
    apply_links = job_element.find_all("a")[1]["href"]
    print(f"Learn here : {learn_links}\n")
    print(f"Apply here : {apply_links}\n")