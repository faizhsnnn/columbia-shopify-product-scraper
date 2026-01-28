import requests
import pandas as pd
import time

BASE_URL = "https://www.columbiasportswear.co.in"
API_URL = BASE_URL + "/collections/men/products.json"

session = requests.Session()

titles = []
prices = []
links = []
categories = []
vendors = []

page = 1
LIMIT = 50   # Shopify max is usually 50
DELAY = 0.05

while True:
    print(f"Fetching page {page}")

    params = {
        "limit": LIMIT,
        "page": page
    }

    response = session.get(API_URL, params=params)
    data = response.json()

    products = data.get("products", [])

    # STOP condition (VERY IMPORTANT)
    if not products:
        break

    for product in products:
        titles.append(product["title"])

        # Price (first variant)
        price = product["variants"][0]["price"]
        prices.append(float(price))

        # Product URL
        handle = product["handle"]
        links.append(f"{BASE_URL}/products/{handle}")

        # Category / type
        categories.append(product.get("product_type", "Unknown"))

        # Brand
        vendors.append(product.get("vendor", "Unknown"))

        time.sleep(DELAY)

    page += 1
df = pd.DataFrame({
    "title": titles,
    "price": prices,
    "category": categories,
    "vendor": vendors,
    "link": links
})

df.to_csv("columbia_men_products.csv", index=False, encoding="utf-8")
df.to_excel("columbia_men_products.xlsx", index=False)

print("✅ Scraping completed")
print(f"Total products scraped: {len(df)}")