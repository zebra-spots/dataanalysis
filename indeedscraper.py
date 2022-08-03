#! /usr/bin/python
# Name: indeedscraper.py
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
    URL = "https://uk.indeed.com/jobs?q=developer&l=Cardiff%2C%20Cardiff&from=searchOnHP&redirected=1&vjk=81b07546d17bf129"
    page = requests.get(URL)
    # Test requests
    #print(page.text) 
    #print(page.content)
    #print(page.url)
    #print(page.status_code)

    soup = BeautifulSoup(page.content, "html.parser")
    #print(soup.prettify()) # Test soup

    # Get title tag
    #print(soup.title)
    # Get name of title tag
    #print(soup.title.name)
    # Get name of parent tag
    #print(soup.title.parent.name)


    s = soup.find('div', class_='mosaic-zone')
    content = s.find_all('li')
    #print(content)

    s1 = soup.find('div', id='mosaic-zone-jobcards')
    print(s1)




    
    return None


if __name__ == "__main__":
    main()
    sys.exit(0)
