import requests, bs4
import lxml #faster parser than lxml
import smtplib
from email.message import EmailMessage
from scraper.config import USER_AGENTS
# from scraper.config import EMAILS
import random

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
    
    match url:
        case "https://www.findchips.com/search/":
            jsonResult = scrape_findchips(res)
        case "https://octopart.com/search?q=":
            jsonResult = scrape_octopart(res)
    jsonResult = clean_data(jsonResult)
    return jsonResult


def clean_data(data):

    return data


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

