import requests, bs4
import lxml #faster parser than lxml
import smtplib
from email.message import EmailMessage
from scraper.config import USER_AGENTS
# from scraper.config import EMAILS
import random
import re

# TO DO:
# refactor scraping code for modularity

def scrape(url, searchQuery):
    print(url + searchQuery)
    try:
        headers = {
                "authority": "www.google.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "Content-Type": "application/json",
    "User-Agent": random.choice(USER_AGENTS)
}
        res = requests.get(url + searchQuery, headers=headers) 
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem: $s' % (exc))
    #this really bad cause it means that if the search url has a url in the config.py then an error is thrown :| BAD BAD BAD
    match url:
        case "https://www.findchips.com/search/":
            jsonResult = scrape_findchips(res)
        case "https://octopart.com/search?q=":
            jsonResult = scrape_octopart(res)
        case "https://www.icsource.com/Home/SampleSearch.aspx?part=":
            jsonResult = scrape_icsource(res)
        case "https://www.oemstrade.com/search/":
            jsonResult = scrape_oemtrade(res)
    jsonResult = clean_data(jsonResult)
    return jsonResult


def clean_data(data):
    filteredData = []
    # Removes data with 0 stock
    dictKey = list(data.keys())[0]
    items = data[dictKey]
    for part in items:
        stock = part["stock"]
        if stock.isnumeric() != True:
            part["stock"] = re.sub(r'\D', '', stock)
        if int(part["stock"]) != 0: 
            filteredData.append(part)
    data[dictKey] = filteredData
    return data


def scrape_oemtrade(data):
    yummySoup = bs4.BeautifulSoup(data.text, 'lxml')
    jsonResult = []
    partElems = yummySoup.find_all('div', class_='distributor-results')
    for part in partElems:
        offers = part.find_all("tr", class_="row")
        for offer in offers:
            distributor = part.find('h2', class_='distributor-title').get_text(strip=True)
            manufacturer = offer.find('td', class_='td-distributor-name').get_text(strip=True)
            stock = offer.find('td', class_='td-stock').get_text(strip=True)
            price = offer.find('td', class_="td-price").get_text(strip=True)
            jsonResult.append({
            "distributor": distributor,
            "manufacturer": manufacturer,
            "stock": stock,
            "price": price
            })
    oemsTrade = {}
    oemsTrade["oemstrade.com"] = jsonResult
    return oemsTrade

#not implemented, need selenium or something
# data rendered using javascript, need to scrape from the api call instead
# put this separately into function that scrapes via api call 
def scrape_oemsecrets(data): 

    oemsecretsJSON = {}
    oemsecretsJSON["oemsecrets.com"] = jsonResult
    return oemsecretsJSON


def scrape_icsource(data):
    yummySoup = bs4.BeautifulSoup(data.text, 'lxml')
    jsonResult = []
    partElems = yummySoup.find_all('tr', class_='rgRow')
    for part in partElems:
        cells = part.find_all("td")
        # manufacturer = .selpartect('td.td-mfg')[0].get_text(strip=True)
        # stock = part.select('td.td-stock')[0].get_text(strip=True)
        # price = part.select('td.td-price-range')[0].get_text(strip=True)
        jsonResult.append({
        "Part Number": cells[0].get_text(strip=True),
        "manufacturer": cells[1].get_text(strip=True),
        "year": cells[2].get_text(strip=True),
        "stock": cells[3].get_text(strip=True),
        # "Details Link": cells[4].find("a")["href"] if cells[4].find("a") else None,
        })
    icsourceJSON = {}
    icsourceJSON["ICSource.com"] = jsonResult
    return icsourceJSON

def scrape_findchips(data):
    yummySoup = bs4.BeautifulSoup(data.text, 'lxml')
    rowElems = yummySoup.find_all('tr', class_='row')
    jsonResult = []
    for i in rowElems:
        manufacturer = i.select('td.td-mfg')[0].get_text(strip=True)
        stock = i.select('td.td-stock')[0].get_text(strip=True)
        price = i.select('td.td-price-range')[0].get_text(strip=True)
        jsonResult.append({
        "manufacturer": manufacturer,
        "stock": stock,
        "price": price
        })
    findChipsJSON = {}
    findChipsJSON["Findchips.com"] = jsonResult
    return findChipsJSON

def scrape_octopart(data):
    yummySoup = bs4.BeautifulSoup(data.text, 'lxml')
    # rowElems = yummySoup.find_all('tr', attrs={'data-testid':'offer-row'})
    partElems = yummySoup.find_all('div', attrs={'data-sentry-component':'Part'})
    jsonResult = []
    for part in partElems:
        offers = part.find_all('tr', attrs={'data-testid':'offer-row'})
        if (len(offers) != 0):
            manufacturer = part.select_one('[data-testid="serp-part-header-manufacturer"]').get_text(strip=True)
            for offer in offers:
                distributor = offer.select_one('[data-sentry-component="Distributor"]').get_text(strip=True)
                stock = offer.select_one('[data-sentry-component="Stock"]').get_text(strip=True)
                price = offer.select_one('[data-sentry-component="PriceAtQty"]').get_text(strip=True)
                link = offer.select_one('[data-sentry-component="Sku"]').find('a')['href']
                jsonResult.append({
                "distributor": distributor,
                "stock": stock,
                "price": price,
                "link": link,
                "manufacturer": manufacturer
                })
    octopartJSON = {}
    octopartJSON["Octopart.com"] = jsonResult
    return octopartJSON



def send_email(subject, body):
    for recipient in EMAILS:
        email = EmailMessage()
        email['Subject'] = subject
        email['From'] = "your-email@example.com"
        email['To'] = recipient
        email.set_content(body)

        with smtplib.SMTP_SSL('smtp.example.com', 465) as smtp:
            smtp.login("your-email@example.com", "your-password")
            smtp.send_message(email)

