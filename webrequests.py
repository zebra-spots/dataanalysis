#!/bin/bash
"""
This web scraper works on static HTML job sites
and will look for and print all python jobs.

Requires the following dependents:

python -m pip install requests
python -m pip install beautifulsoup4

"""
import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# Find id in HTML page to narrow the data
results = soup.find(id="ResultsContainer")

job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements:
    #print(job_element, end="\n"*2)
    title_element = job_element.find("h2", class_="title is-5")
    subtitle_element = job_element.find("h3", class_="subtitle is-6 company")
    location_element = job_element.find("p", class_="location")
    #print(title_element.text.strip())
    #print(subtitle_element.text.strip())
    #print(location_element.text.strip())
    #print()

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
#print(python_jobs)

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title is-5")
    subtitle_element = job_element.find("h3", class_="subtitle is-6 company")
    location_element = job_element.find("p", class_="location")
    #links = job_element.find_all("a")
    link_url = job_element.find_all("a")[1]["href"]
    

    print(title_element.text.strip())
    print(subtitle_element.text.strip())
    print(location_element.text.strip())
    print(f"Apply here: {link_url}\n")


    #for link in links:
        #link_url = link["href"]
        #print(f"Apply here:", link_url)
        #print(link.text.strip())
        #print()

