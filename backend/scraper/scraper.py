import requests, bs4
import lxml #faster parser than lxml
import smtplib
from email.message import EmailMessage
from scraper.config import USER_AGENTS
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
    #for findchips
    # yummySoup = bs4.BeautifulSoup(res.text, 'lxml')
    # rowElems = yummySoup.find_all('tr', class_='row')
    # jsonResult = []
    # for i in rowElems:
    #     manufacturer = i.select('td.td-mfg')[0].get_text(strip=True)
    #     stock = i.select('td.td-stock')[0].get_text(strip=True)
    #     price = i.select('td.td-price-range')[0].get_text(strip=True)
    #     jsonResult.append({
    #     "manufacturer": manufacturer,
    #     "stock": stock,
    #     "price": price
    #     })

    #for octopart
    yummySoup = bs4.BeautifulSoup(res.text, 'lxml')
    rowElems = yummySoup.find_all('tr', attrs={'data-testid':'offer-row'})
    jsonResult = []
    for i in rowElems:
        distributor = i.select_one('[data-sentry-component="Distributor"]').get_text(strip=True)
        stock = i.select_one('[data-sentry-component="Stock"]').get_text(strip=True)
        price = i.select_one('[data-sentry-component="PriceAtQty"]').get_text(strip=True)
        link = i.select_one('[data-sentry-component="Sku"]').find('a')['href']
        jsonResult.append({
        "distributor": distributor,
        "stock": stock,
        "price": price,
        "link": link
        })
    print(jsonResult)
    return jsonResult

def send_email(subject, body, to_email):
    email = EmailMessage()
    email['Subject'] = subject
    email['From'] = "your-email@example.com"
    email['To'] = to_email
    email.set_content(body)

    with smtplib.SMTP_SSL('smtp.example.com', 465) as smtp:
        smtp.login("your-email@example.com", "your-password")
        smtp.send_message(email)

