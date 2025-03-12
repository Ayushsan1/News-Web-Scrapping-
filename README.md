# Hindustan Times News Scraper

## Overview
This project scrapes the **top 10 news headlines** from the Hindustan Times website using **BeautifulSoup** and **Requests**. The scraped data is then served using a **Flask** web application.

## Features
- Scrapes top 10 news headlines from Hindustan Times.
- Uses **BeautifulSoup** to parse HTML content.
- Retrieves data using **Requests**.
- Serves the scraped data via a Flask web API.

## Technologies Used
- Python
- Flask
- BeautifulSoup
- Requests
- thread

## Installation
### 1. Clone the Repository
```bash
https://github.com/Ayushsan1/News-Web-Scrapping-/
```


## Usage
### 1. Run the Flask Server
```bash
python app.py
```

### 2. Access the API
Once the server is running, open the following URL in your browser:
```
http://127.0.0.1:5000/
```
This will return the scraped top 10 news headlines in JSON format.

## Project Structure
```
├── app.py  # Main Flask application
├── index.html #web view
├── README.md  # Project documentation
```

## Example Output
```json
{
  "news": [
    "Headline 1",
    "Headline 2",
    "Headline 3",
    "..."
  ]
}


