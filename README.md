# Columbia Shopify Product Scraper

A production-style Python data extraction script that retrieves structured product data from a Shopify-powered e-commerce store and exports it into CSV and Excel formats for analytics, reporting, and downstream processing.

---

## 📌 Project Overview

This project demonstrates real-world API-based data extraction using Python.  
It fetches men’s product data from a Shopify Products API, handles pagination, normalizes JSON responses, and generates business-ready datasets.

The script is designed with scalability and clarity in mind, closely resembling data engineering and backend automation workflows used in industry.

---

## ⚙️ Features

- API-based data extraction (no HTML parsing)

- Shopify pagination handling

- Session-based HTTP requests for efficiency

- Structured data normalization

- CSV and Excel export

- Lightweight rate limiting for stability

---

## 🧠 Data Collected

- Product Title  

- Price  

- Category / Product Type  

- Vendor / Brand  

- Product URL  

---

## 🛠️ Tech Stack

- Python 3

- Requests

- Pandas

- OpenPyXL (Excel export)

---

## 📂 Project Structure
```
columbia-shopify-product-scraper/
│
├── main.py
├── README.md
├── requirements.txt
├── columbia_men_products.csv
└── columbia_men_products.xlsx
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```
git clone https://github.com/yourusername/columbia-shopify-product-scraper.git
cd columbia-shopify-product-scraper
```
## 2️⃣ Create Virtual Environment (Optional but Recommended)
```
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```
## 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
## 4️⃣ Run the Script
```
python main.py
```
## 📤 Output
After execution, the script generates:

columbia_men_products.csv

columbia_men_products.xlsx

Both files contain clean, structured product data ready for analysis or reporting.

---
## ⚠️ Notes
This script uses publicly accessible Shopify product endpoints.

Includes a small delay between requests to reduce server load.

Intended for educational, analytical, and portfolio purposes.

---
## 📈 Use Cases
Market price analysis

Product catalog monitoring

Competitive research

Data engineering portfolios

Automation and ETL demonstrations

---
## 👤 Author
Faiz Hasan

Python Developer | Data Automation | API Integration


---
## 📜 License
This project is provided for educational and portfolio use only.
