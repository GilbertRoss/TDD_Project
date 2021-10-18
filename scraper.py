from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from bs4 import BeautifulSoup


def loadPage(author, name):
    if(len(author) == 0 or len(name) == 0):
        raise Exception('Name or Author is empty!')
    url = 'https://genius.com/'+ author.replace(' ', '-') + '-' + name.replace(' ', '-') + '-lyrics'
    options = FirefoxOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    
    driver.get(url)
    html = driver.page_source
    driver.quit()
    return html


def parsePage(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = [item.get_text().strip() for item in soup.select('.lyrics')]
    if(len(items) == 0):
      items = [item.text for item in soup.select('.Lyrics__Container-sc-1ynbvzw-10.cvsIWi')]
      
    return items[0]
