
# Modern Web Scraping with Python

This repository showcases the web scraping project developed by following the **"Modern Web Scraping with Python using Scrapy, Splash, and Selenium"** course from Udemy. It demonstrates scraping techniques for both static and dynamic websites, handling JavaScript-heavy content, and interacting with web elements.

## Features

- **Scrapy**: For high-performance, scalable web scraping
- **Splash**: For rendering JavaScript-heavy websites to scrape dynamic content
- **Selenium**: For interacting with dynamic web elements like forms and login pages
- **Proxy Management**: Rotating proxies and user agents to avoid detection and reduce the chances of getting blocked
- **Data Storage**: Storing scraped data into **PostgreSQL** or **MongoDB** for easy analysis
- **CAPTCHA Handling**: Implementing solutions for scraping CAPTCHA-protected websites

## Project Setup

### Prerequisites

- **Python 3.x**
- **Scrapy**
- **Splash**
- **Selenium**
- **PostgreSQL** or **MongoDB** for data storage
- **Docker** (for Splash setup)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/devodriqroberts/Modern-Web-Scraping-with-Python.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Modern-Web-Scraping-with-Python
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up **Splash** using Docker:

   ```bash
   docker run -p 8050:8050 scrapinghub/splash
   ```

5. (Optional) Configure the database connection:

   - For **PostgreSQL** or **MongoDB**, set the connection string in your environment variables.

### Running the Scraper

1. Start the **Splash** server (if scraping JavaScript-heavy websites):

   ```bash
   docker start splash
   ```

2. Run the Scrapy spider:

   ```bash
   scrapy crawl spider_name
   ```

3. (Optional) Store data in a database:

   - Configure the spider to output data directly into **PostgreSQL** or **MongoDB** by adjusting the pipeline settings in `settings.py`.

### Scrapy Pipelines

Data can be saved to different formats, including:
- **JSON**
- **CSV**
- **SQL Databases** (e.g., PostgreSQL, MongoDB)

### API Usage (Optional)

Integrate the scraper into an API using **Flask** or **FastAPI**, allowing you to trigger the scraping process and fetch the results programmatically.

## Project Highlights

- Scraped dynamic content from JavaScript-heavy websites using **Splash**
- Interacted with complex web elements like forms and drop-downs using **Selenium**
- Implemented **proxy rotation** and **user-agent rotation** to avoid scraping restrictions
- Efficiently stored and processed scraped data in structured databases for further analysis

## Acknowledgments

This project is based on **"Modern Web Scraping with Python using Scrapy, Splash, and Selenium"** from Udemy, instructed by **Ahmed Rafik**.

## License

This project is licensed under the MIT License.
