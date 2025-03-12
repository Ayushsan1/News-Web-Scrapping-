from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import time
from threading import Thread

app = Flask(__name__)

headlines = []

def scrape_headlines():
    while True:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Connection': 'keep-alive',
            }
            
            url = "https://www.hindustantimes.com/india-news"
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            news_items = soup.select('h2.hdg3, div.cartHolder h2, .headingfour, .headline, .top-news h2')
            
            global headlines
            temp_headlines = []
            
            for item in news_items:
                try:
                    headline_text = ''
                    if item.find('a'):
                        headline_text = item.find('a').text.strip()
                    else:
                        headline_text = item.text.strip()
                        
                    if headline_text and len(headline_text) > 10:
                        temp_headlines.append(headline_text)
                except Exception as e:
                    print(f"Error processing headline: {e}")
                    continue
            
            if temp_headlines:
                headlines = temp_headlines[:10]
                print(f"Successfully scraped {len(headlines)} headlines")
            else:
                print("No headlines found in the current scrape")
            
        except Exception as e:
            print(f"Error during scraping: {e}")
        
        time.sleep(300)

@app.route('/')
def home():
    return render_template('index.html', headlines=headlines)

def start_scraping():
    scrape_headlines()  # Initial scrape
    scraper_thread = Thread(target=scrape_headlines, daemon=True)
    scraper_thread.start()

if __name__ == "__main__":
    # Start scraping in a separate thread
    scraper_thread = Thread(target=start_scraping)
    scraper_thread.start()
    
    # Run Flask app
    app.run(host='127.0.0.1', port=5000, debug=True)