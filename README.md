scraper python 3, beautiful soup
scraper rotates user agents from USER_AGENTS in config.py file

Component Scraper Website

A modular web scraping tool designed for retrieving component information from various distributor websites, cleaning the data, and presenting it in a structured format.

Table of Contents

About the Project

Features

Installation

Usage

Configuration

Technologies Used

Contributing

License

Contact

About the Project

The Component Scraper Website is a scraping solution that extracts real-time stock, pricing, and distributor data for electronic components. Designed for flexibility and ease of use, it supports multiple distributor sites by utilizing reusable scraping configurations.

Why This Project?

- Streamline component data aggregation for manufacturers and hobbyists.

- Enable seamless integration of scraped data into inventory management systems.

- Demonstrate modular scraping with Python and BeautifulSoup.

Features

- Modular scraping functions with configurable CSS selectors for multiple websites.

- Automated cleaning of scraped data (e.g., removing zero-stock items).

- Flexible support for adding new distributor websites.

- Optimized for error handling and debugging.

Installation

Clone the repository:

git clone https://github.com/kana140/component-scraper.git

Navigate to the project directory:

cd component-scraper\backend

Install required dependencies:

pip install -r requirements.txt

Add user agents and other configurations to config.py.

Usage

To scrape data, use the following command:

python app.py

The results will be cleaned and saved in JSON format.

Example Output
{
"data": {
"ICSource.com": {
"products": [
{
"Part Number": "TH8056KDC-AAA-014-RE",
"manufacturer": "MELEXIS",
"stock": "760912",
"year": "21+"
}
],
"websiteLink": "https://www.icsource.com/Home/SampleSearch.aspx?part=TH8056KDC-AAA-014-RE"
},
"Octopart.com": {
"products": [
{
"distributor": "DigiKey",
"link": "https://octopart.com/opatz8j6/a1?t=AszL1gb0e8ESP6D4fdex1nBEzs0P0bEvmZaJDSrYoF_RZg8zVcFXRKXmbGwpd_YJpNgDg2vfB9txvfrkWDbM3kC3SmQzZR44uVn2-0M3QXuuNF8IwE5uW_W7yrmTB_s20S3UQHZY257c3UIFc51pNilob5-i68CyZuB4Xtf6PezgEcBb0LZrvU00G2I037NwGJkvqgALaQqK4Mlfrop0O41iqnBGQ-2mX8_hhIH0GU8ss_JIu0ocYjxI0k1BKiKbf1JSUuGO1K1fGhZRMh7vEw",
"manufacturer": "Melexis",
"price": "1.970",
"stock": "14591"
}
],
"websiteLink": "https://octopart.com/search?q=TH8056KDC-AAA-014-RE"
},
"findChips.com": {
"products": [
{
"manufacturer": "Melexis Microelectronic Integrated Systems",
"price": "$0.9704 / $1.9700",
"stock": "14591"
}
],
"websiteLink": "https://www.findchips.com/search/TH8056KDC-AAA-014-RE"
},
"oemsTrade.com": {
"products": [
{
"distributor": "Mouser ElectronicsECIA (NEDA) Member  Authorized Distributor",
"manufacturer": "Melexis Microelectronic Integrated Systems",
"price": "1$1.970010$1.6800100$1.4300250$1.3400500$1.17001000$0.97003000$0.90306000$0.86909000$0.8360Show All",
"stock": "8994"
}
],
"websiteLink": "https://www.oemstrade.com/search/TH8056KDC-AAA-014-RE"
}
},
"searchQuery": "TH8056KDC-AAA-014-RE"
}

Configuration

Selectors for Scraping: Add CSS selectors for each distributor in config.py.

Headers: Update USER_AGENTS in config.py for dynamic user-agent rotation.

Error Handling: Set retries and timeouts in scraper.py.

Technologies Used

Python: Core programming language for scraping.

BeautifulSoup: For HTML parsing and data extraction.

Requests: To handle HTTP requests.

Regex: For cleaning and filtering scraped data.

JSON: To format and store output data.

React Javascript: To dynamically render data using MUI in a readable and presentable format

Contributing

Contributions are welcome! Follow these steps to contribute:

Fork the repository.

Create a new branch:

git checkout -b feature/YourFeatureName

Commit your changes:

git commit -m "Add a new scraping function"

Push to the branch:

git push origin feature/YourFeatureName

Open a pull request.

License

Distributed under the MIT License. See LICENSE for more information.

Contact

Keitel Anana - keitelwinslet@gmail.com

Project Link: https://github.com/kana140/component-scraper
