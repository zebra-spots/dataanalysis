#! /usr/bin/python
# Name: webscrapeproject.py
# Author: Chris
# Revision v1.0
# Description: This web scraper works on static HTML job sites
# and will look for and print all python jobs.
"""
    Docstring: 

Requires the following modules:

python -m pip install requests
python -m pip install beautifulsoup4
"""
import sys
import requests
from bs4 import BeautifulSoup

def main():
    """ main program overview """
    
    # Variables
    URL = "https://remote.co/remote-jobs/developer/"
    page = requests.get(URL)
    #print(page.text) # Test request

    soup = BeautifulSoup(page.content, "html.parser")
    #print(soup.prettify()) # Test soup

    #Can't figure how to get the correct div
    results = soup.div.div.div.div
    print(results)

    # class="job-Types"?

    # job name: class="m-0"
    # Company name: class="m-0 text-secondary"

    
    return None


if __name__ == "__main__":
    main()
    sys.exit(0)
