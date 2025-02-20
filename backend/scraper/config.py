SCRAPE_URLS = {
        "findChips.com" : ["https://www.findchips.com/search/", "scrape_findchips"], 
        "Octopart.com" : ["https://octopart.com/search?q=", "scrape_octopart"],
        "ICSource.com": ["https://www.icsource.com/Home/SampleSearch.aspx?part=", "scrape_icsource"],
        "oemsTrade.com": ["https://www.oemstrade.com/search/", "scrape_oemtrade"]

}

USER_AGENTS = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'
]

# DB_URI = "mongodb://localhost:27017/"
DB_URI = "mongodb+srv://keitelwinslet:R8Q7ajJxT9COeQIQ@net-components.kcrfz.mongodb.net/?retryWrites=true&w=majority&appName=net-components"
DB_NAME = "netComponentsDB"
DB_USER = ""
DB_PASSWORD = ""


# EMAILS = ["keitelwinslet@gmail.com"]