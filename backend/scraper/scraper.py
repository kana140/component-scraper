import requests, bs4
import lxml #faster parser than lxml
import smtplib
from email.message import EmailMessage
from scraper.config import USER_AGENTS, SCRAPE_URLS
# from scraper.config import EMAILS
import random
import re

# TO DO:
# refactor scraping code for modularity

def scrape(searchQuery):
    try:
        headers = {
                "authority": "www.google.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "Content-Type": "application/json",
    "User-Agent": random.choice(USER_AGENTS)
}
        data = {}
        for key, value in SCRAPE_URLS.items():
            url = value[0]
            scrape_function = globals().get(value[1])
            try:
                res = requests.get(url + searchQuery, headers=headers)
                res.raise_for_status() 
            except: 
                print("scraping failed for:", key)
            finally:
                yummySoup = bs4.BeautifulSoup(res.text, 'lxml')
                jsonResult = scrape_function(yummySoup)
                jsonResult = clean_data(jsonResult)
                data[key] = {}
                data[key]["products"] = list(jsonResult.values())[0]
                data[key]["websiteLink"] = url + searchQuery 
    except Exception as exc:
        print('There was a problem: $s' % (exc))
    return data


def clean_data(data):
    filteredData = []
    # Removes data with 0 stock and removes non numerical characters 
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
    jsonResult = []
    partElems = data.find_all('div', class_='distributor-results')
    for part in partElems:
        offers = part.find_all("tr", class_="row")
        if (len(offers) != 0):
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

def scrape_octopart(data):
    jsonResult = []
    partElems = data.find_all('div', attrs={'data-sentry-component':'Part'})
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



def scrape_icsource(data):
    jsonResult = []
    partElems = data.find_all('tr', class_='rgRow')
    for part in partElems:
        cells = part.find_all("td")
        jsonResult.append({
        "Part Number": cells[0].get_text(strip=True),
        "manufacturer": cells[1].get_text(strip=True),
        "year": cells[2].get_text(strip=True),
        "stock": cells[3].get_text(strip=True),
        })
    icsourceJSON = {}
    icsourceJSON["ICSource.com"] = jsonResult
    return icsourceJSON

def scrape_findchips(data):
    rowElems = data.find_all('tr', class_='row')
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

