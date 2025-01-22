# CraftBook-Scraper
A Python script to extract book data from a website and save it to an Excel file

## Herron Books Scraper

This Python project is designed to scrape book data from the **Herron Books** website. It extracts information such as book titles, authors, descriptions, ISBNs, prices, and more. The scraped data is stored in an Excel file for further use.

## Features

- Scrapes book information including:
  - **Name**  
  - **Author**  
  - **Short Description**  
  - **ISBN**  
  - **Price**  
  - **Image URL**  
  - **Details Page URL**  
- Stores the scraped data in an organized Excel file (`craft_books.xlsx`).
- Simple and efficient structure for web scraping.

## Requirements

Ensure you have the following installed:

- Python 3.10+  
- Required libraries:
  - `requests`
  - `beautifulsoup4`
  - `pandas`
  - `openpyxl` (for Excel export)

Install dependencies with pip:

```bash
pip install requests beautifulsoup4 pandas openpyxl
